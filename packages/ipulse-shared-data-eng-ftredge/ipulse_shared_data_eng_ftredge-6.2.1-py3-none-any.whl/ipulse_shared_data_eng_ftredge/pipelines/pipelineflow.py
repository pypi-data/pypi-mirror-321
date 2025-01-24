""" Shared pipeline configuration utility. """
import uuid
from datetime import datetime, timezone
from typing import List, Optional, Dict, Union,Tuple
import copy
from ipulse_shared_base_ftredge import (StatusCounts,
                                        StatusTrackingMixin,
                                        eval_statuses,
                                        Action,
                                        DataResource,
                                        ProgressStatus)
from .function_result import FunctionResult



###############################################################################################
########################################   DEPENDENCY   ########################################

class DependencyType:
    """Requirements for dependency resolution"""
    TO_CLOSED = "to_closed"  # Must be in closed statuses
    TO_SUCCESS = "to_success"  # Must be in success statuses
    TO_SUCCESS_OR_SKIPPED = "to_success_or_skipped"  # Must be in success or skipped statuses
    TO_AT_LEAST_STARTED = "to_at_least_started"  # Must be at least started (not in NOT_STARTED)
    TO_FAILURE = "to_failure"  # Must be in failure statuses

    @staticmethod
    def validate_status(status: ProgressStatus, requirement: str) -> bool:
        """Check if status meets requirement"""
        if requirement == DependencyType.TO_CLOSED:
            return status in ProgressStatus.closed_statuses()
        elif requirement == DependencyType.TO_SUCCESS:
            return status in ProgressStatus.success_statuses()
        elif requirement == DependencyType.TO_SUCCESS_OR_SKIPPED:
            return status in ProgressStatus.success_statuses() or status in ProgressStatus.skipped_statuses()
        elif requirement == DependencyType.TO_AT_LEAST_STARTED:
            return status not in ({ProgressStatus.NOT_STARTED, ProgressStatus.BLOCKED_BY_UNRESOLVED_DEPENDENCY} or ProgressStatus.pending_statuses())
        elif requirement == DependencyType.TO_CLOSED:
            return status in ProgressStatus.closed_statuses()
        elif requirement == DependencyType.TO_FAILURE:
            return status in ProgressStatus.failure_statuses()
        return False

class Dependency:
    """Represents a dependency between pipeline steps"""
    
    def __init__(self,
                 step_name: str,
                 requirement: str = DependencyType.TO_SUCCESS_OR_SKIPPED,
                 optional: bool = False,
                 timeout_s: Optional[int] = None):
        self.step_name = step_name
        self.requirement = requirement
        self.optional = optional
        self.timeout_s = timeout_s
        self._start_time = None
        
    def start_timeout(self):
        """Start timeout tracking"""
        if self.timeout_s:
            self._start_time = datetime.now()
            
    def is_timeout(self) -> bool:
        """Check if dependency has timed out"""
        if not self.timeout_s or not self._start_time:
            return False
        elapsed = (datetime.now() - self._start_time).total_seconds()
        return elapsed > self.timeout_s

    def check_satisfied(self, step: 'Step') -> bool:
        """Check if dependency is satisfied by step's progress status"""
        # if self.is_timeout():
        #     return False
            
        return DependencyType.validate_status(step.progress_status, self.requirement)

    def __str__(self):
        return f"Dependency({self.step_name}, req={self.requirement}, optional={self.optional})"


###############################################################################################
########################################   STEP   #############################################
class Step:
    """Base class for all pipeline steps - contains only core pipeline functionality"""
    
    def __init__(self, name: str,
                 disabled: bool = False,
                 dependencies: Optional[List[Union[str, Dependency, Dict[str,DependencyType]]]] = None,
                 config: Optional[Dict] = None,
                 issues_allowed: bool = True):
        self.id = uuid.uuid4()
        self._name = name
        self._issues_allowed = issues_allowed # Allow issues by default
        self._dependencies = self._normalize_dependencies(dependencies or [])
        self._disabled = disabled
        self._progress_status = ProgressStatus.DISABLED if disabled else ProgressStatus.NOT_STARTED
        self._pipeline_flow = None
        self._config = config or {}
        self._start_time: Optional[datetime] = None
        self._duration_s: float = 0.0

    @property
    def duration_s(self) -> float:
        """Get execution duration in seconds"""
        if not self._start_time:
            return 0.0
        if self.is_closed_or_skipped:
            return self._duration_s
        return (datetime.now(timezone.utc) - self._start_time).total_seconds()

    def calculate_duration(self) -> None:
        """Calculate and store final duration"""
        if self._start_time:
            self._duration_s = (datetime.now(timezone.utc) - self._start_time).total_seconds()

    @property
    def name(self) -> str:
        """Get name"""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Set name"""
        self._name = value


    @property
    def issues_allowed(self) -> bool:
        """Check if issues are allowed"""
        return self._issues_allowed
    
    @issues_allowed.setter
    def issues_allowed(self, value: bool):
        """Set whether issues are allowed"""
        self._issues_allowed = value

    @property
    def pipeline_flow(self) -> 'PipelineFlow':
        """Get pipeline flow"""
        return self._pipeline_flow
    

    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow'):
        """Set pipeline flow for step, which is used for dependency resolution. As dependencies status is updated during execution this has to be referenced."""
        self._pipeline_flow = pipeline_flow

    @property
    def dependencies(self) -> List[Dependency]:
        """Get dependencies"""
        return self._dependencies
    
    @dependencies.setter
    def dependencies(self, value: List[Union[str, Dependency, Dict[str,DependencyType]]]):
        """Set dependencies"""
        self._dependencies = self._normalize_dependencies(value)

    @property
    def config(self) -> Dict:
        return self._config
    
    @config.setter
    def config(self, value: Dict):
        if not isinstance(value, dict):
            raise ValueError("Config must be a dictionary")
        self._config = value

    @property
    def progress_status(self) -> ProgressStatus:
        """Get progress status"""
        return self._progress_status
        
    @progress_status.setter 
    def progress_status(self, value: ProgressStatus):
        self._progress_status = value

    @property
    def disabled(self) -> bool:
        """Check if step is disabled"""
        return self._disabled
    
    @disabled.setter
    def disabled(self, value: bool):
        """
        Set disabled status.
        If step is disabled, status is set to DISABLE
        """
        self._disabled = value
        if value:
            self.progress_status = ProgressStatus.DISABLED

    @property
    def is_success(self) -> bool:
        return self.progress_status in ProgressStatus.success_statuses()
    
    @property
    def is_success_or_skipped(self) -> bool:
        return self.progress_status in ProgressStatus.success_statuses() or self.progress_status in ProgressStatus.skipped_statuses()
    
    @property
    def is_closed_or_skipped(self) -> bool:
        return self.progress_status in ProgressStatus.closed_statuses() or self.progress_status in ProgressStatus.skipped_statuses()
    
    @property
    def is_failure(self) -> bool:
        return self.progress_status in ProgressStatus.failure_statuses()
    
    @property
    def is_pending(self) -> bool:
        return self.progress_status in ProgressStatus.pending_statuses()
    
    @property
    def has_issues(self) -> bool:
        return self.progress_status in ProgressStatus.issue_statuses()

    # ------------------
    # Dependencies
    # ------------------
    def _normalize_dependencies(self, deps: List[Union[str, Dependency, Dict[str,DependencyType]]]) -> List[Dependency]:
        """Convert string dependencies to Dependency objects"""
        normalized = []
        for dep in deps:
            if isinstance(dep, str):
                normalized.append(Dependency(dep))
            elif isinstance(dep, Dependency):
                normalized.append(dep)
            elif isinstance(dep, dict):
                for step_name, dep_type in dep.items():
                    normalized.append(Dependency(step_name, dep_type))
            else:
                raise ValueError(f"Invalid dependency type: {type(dep)}")
        return normalized

    # ------------------
    # Validation Functions
    # ------------------
    def validate_dependencies(self, sequence_ref: Optional[Union[int, str]] = None) -> Tuple[bool, Optional[str]]:
        """
        Validate all dependencies are satisfied.
        Returns (is_satisfied, reason_if_not)
        """
        if not self.dependencies:
            return True, None

        if not self._pipeline_flow:
            # If pipeline_flow isn't set, skip or raise an error
            return True, None
            
        unsatisfied = []
        for dep in self.dependencies:
            if isinstance(dep, str):
                    dep = Dependency(dep)
            if not dep.optional:
                try:
                    dep_step = self._pipeline_flow.get_step(dep.step_name, sequence_ref)
                    if not dep.check_satisfied(dep_step):
                        unsatisfied.append(f"{str(dep)} : {dep_step.progress_status}")
                except KeyError:
                    unsatisfied.append(f"Missing dependency: {dep.step_name}")
                    
        if unsatisfied:
            return False, f"Unsatisfied dependencies: {', '.join(unsatisfied)}"
            
        return True, None

    def validate_and_start(self, set_status: Optional[ProgressStatus]=ProgressStatus.IN_PROGRESS,
                      sequence_ref: Optional[Union[int, str]]=None) -> Tuple[bool, Optional[str]]:
        """Validate and start step execution"""
        # Prevent restarting completed steps
        if self.is_closed_or_skipped:
            return False, f"Step already completed with status {self.progress_status}"
            
        if self.disabled:
            self.progress_status = ProgressStatus.DISABLED
            return False, "Step is disabled"
            
        if self.progress_status in ProgressStatus.skipped_statuses():
            self.progress_status = ProgressStatus.INTENTIONALLY_SKIPPED
            return False, "Step is skipped"

        deps_ok, reason = self.validate_dependencies(sequence_ref)
        if not deps_ok:
            self.progress_status = ProgressStatus.BLOCKED_BY_UNRESOLVED_DEPENDENCY
            return False, reason

        # Start execution tracking
        self._start_time = datetime.now(timezone.utc)
        self.progress_status = set_status
        return True, None

    def nb_tasks(self) -> int:
        """Get number of tasks - Each subclas must implement its own version"""
        raise NotImplementedError

###############################################################################################
########################################   PipelineTask   #############################################

class PipelineTask(Step, StatusTrackingMixin):
    """Represents a single task in a pipeline with full status tracking capabilities"""
    
    def __init__(
        self,
        n: str,
        a: Optional[Action] = None,
        s: Optional[DataResource] = None,
        d: Optional[DataResource] = None,
        dependencies: Optional[List[Union[str, Dependency]]] = None,
        disabled: bool = False,
        config: Optional[Dict] = None,
        issues_allowed: bool = True
    ):
        """Initialize PipelineTask with both Step and StatusTracking capabilities"""
        Step.__init__(self, name=n,
                      disabled=disabled,
                      dependencies=dependencies,
                      config=config,
                      issues_allowed=issues_allowed)
        StatusTrackingMixin.__init__(self)
        self._action = a
        self._source = s
        self._destination = d
        self._final_report = None

    @property
    def action(self) -> Optional[Action]:
        """Get action"""
        return self._action
    
    @property
    def source(self) -> Optional[DataResource]:
        """Get source"""
        return self._source
    
    @property
    def destination(self) -> Optional[DataResource]:
        """Get destination"""
        return self._destination

    def incorporate_function_result(self, result: FunctionResult, issues_allowed:bool=True) -> None:
        """Incorporate function result and update status"""
        self.integrate_status_tracker(
            next=result,
            skip_metadata=False,
            issues_allowed=issues_allowed,
            name=f"Function Result {result.name}"
        )
        
        # Update status based on result if not already finalized
        if not self.is_closed:
            self.progress_status = result.progress_status

    def nb_tasks(self) -> int:
        return 1

    @property
    def final_report(self) -> Optional[str]:
        """Get task completion report including status tracking details"""
        if not self._final_report and self.is_closed_or_skipped:
            self._generate_final_report()
        return self._final_report

    def _generate_final_report(self) -> None:
        """Generate detailed task execution report"""
        if not self.is_closed_or_skipped:
            return

        report_parts = [
            f"Task {self.name} Final Report",
            f"Status: {self.progress_status.name}",
            f"Duration: {self.duration_s:.2f}s",
            f"Action: {self.action.name if self.action else 'None'}",
            f"Source: {self.source.name if self.source else 'None'}",
            f"Destination: {self.destination.name if self.destination else 'None'}"
        ]

        # Add status tracking info
        if self.issues:
            report_parts.append("\nIssues:")
            report_parts.extend(f"  {issue}" for issue in self.issues)
            
        if self.warnings:
            report_parts.append("\nWarnings:")
            report_parts.extend(f"  {warning}" for warning in self.warnings)
            
        if self.notices:
            report_parts.append("\nNotices:")
            report_parts.extend(f"  {notice}" for notice in self.notices)

        # Add execution state
        if self.execution_state:
            report_parts.append("\nExecution State:")
            report_parts.extend(f"  {state}" for state in self.execution_state)

        self._final_report = "\n".join(report_parts)

    def final(self) -> None:
        """Calculate final status and generate report"""
        
        self.calculate_duration()
        # Any task-specific finalization logic
        self._generate_final_report()

        if self.is_closed_or_skipped:
            return

    def __str__(self):
        if self.is_success:
            status_symbol = "✔"
        elif self.progress_status in ProgressStatus.failure_statuses():
            status_symbol = "✖"
        elif self.progress_status in ProgressStatus.pending_statuses():
            status_symbol = "..."
        elif self.progress_status in ProgressStatus.skipped_statuses():
            status_symbol = "//"
        else:
            status_symbol = "?"

        parts = [f">> {self.name}"]
        if self._action:
            parts.append(str(self._action))
        if self._source:
            parts.append(f"from {str(self._source)}")
        if self._destination:
            parts.append(f"to {str(self._destination)}")
        
        parts.append(f"[Status: {status_symbol} {self.progress_status.name}] ")
        return f"{' :: '.join(parts)}"


###############################################################################################
########################################   PipelineSequenceTemplate   #############################################
class PipelineSequenceTemplate:
    """
    Template for creating sequences of steps.
    Handles any Step-based classes including tasks, sequences, and iterators.
    """
    def __init__(self, steps:List[Step]):
        """
        Initialize template with steps.

        Args:
            steps: List of steps that can be:
                - Any Step-based instance (Task, Sequence, Iterator)
        """
        self.steps: Dict[str, Step] = {}
        self._process_steps(steps)

    def _process_steps(self, steps: List[Step]) -> None:
        """Process and normalize different types of step inputs"""
        for step in steps:
            if isinstance(step, Step):
                # Direct Step instance (Task, Sequence, Iterator.)
                self.steps[step.name] = step
            else:
                raise ValueError(f"Invalid step type: {type(step)}")

    def clone_steps(self) -> Dict[str, Step]:
        """Create a deep copy of all steps"""
        return {name: copy.deepcopy(step) for name, step in self.steps.items()}
    
    @property
    def nb_tasks(self) -> int:
        """Get total number of tasks across all steps"""
        return sum(
            step.nb_tasks() 
            for step in self.steps.values() 
            if not step.disabled
        )
    
    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow') -> None:
        """Associate all steps with the pipeline flow"""
        for step in self.steps.values():
            step.set_pipeline_flow(pipeline_flow)

    def __str__(self) -> str:
        """String representation showing all steps"""
        return "\n".join(f"    {str(step)}" for step in self.steps.values())




###############################################################################################
########################################   PipelineSequence   #############################################

class PipelineSequence(Step):
    """Represents a sequence of steps that can be initialized from a template or direct steps"""

    def __init__(self,
                 sequence_ref: Union[int, str],
                 sequence_template: Optional[PipelineSequenceTemplate] = None,
                 steps: Optional[List[Union[PipelineTask, 'PipelineDynamicIterator']]] = None,
                 dependencies: Optional[List[Union[str, Dependency]]] = None,
                 issues_allowed: bool = True,
                 disabled: bool = False,
                  config: Optional[Dict] = None):
        """Initialize sequence with Step base class and status tracking"""
        super().__init__(name=f"sequence_{sequence_ref}",
                         dependencies=dependencies,
                         issues_allowed=issues_allowed,
                         disabled=disabled,
                         config=config)
        self.sequence_ref = sequence_ref
        self._status_counts = StatusCounts()
        self._final_report = None

        # Initialize steps either from template or direct list
        if sequence_template is not None:
            self.steps = sequence_template.clone_steps()
        elif steps is not None:
            self.steps = {step.name: step for step in steps}
        else:
            self.steps = {}

    @property
    def status_counts(self) -> StatusCounts:
        """Get status counts object"""
        return self._status_counts
    
    def add_step(self, step: Union[PipelineTask, 'PipelineDynamicIterator']) -> None:
        """Add a step to the sequence"""
        if step.name in self.steps:
            raise ValueError(f"Step {step.name} already exists in sequence {self.sequence_ref}")
        self.steps[step.name] = step
        if self._pipeline_flow:
            step.set_pipeline_flow(self._pipeline_flow)

    def add_steps(self, steps: List[Union[PipelineTask, 'PipelineDynamicIterator']]) -> None:
        """Add multiple steps to the sequence"""
        for step in steps:
            self.add_step(step)

    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow'):
        """Associate the sequence's tasks with the pipeline flow."""
        super().set_pipeline_flow(pipeline_flow)
        for step in self.steps.values():
            step.set_pipeline_flow(pipeline_flow)

    def collect_status_counts(self) -> StatusCounts:
        """Collect status counts from steps without modifying them"""
        counts = StatusCounts()
        if not self.steps:
            return counts
            
        for step in self.steps.values():
            if not step.disabled:
                counts.add_status(step.progress_status)
                
        return counts

    def update_status_counts_and_progress_status(self, final: bool) -> None:
        """Update own status based on current step statuses"""
        counts = self.collect_status_counts()
        self._status_counts = counts  # Store for reporting
        
        # Update own status based on counts
        self.progress_status = eval_statuses(
            counts,
            final=final,
            issues_allowed=self.issues_allowed
        )

    def final(self, force_if_closed:bool=False) -> None:
        """
        Finalize sequence using current step statuses.
        Does not modify child steps - assumes their statuses are already final or will be evaluated as FAILED
        """
        if self.is_closed_or_skipped and not force_if_closed:
            return
            
        # Calculate own duration and status based on current step statuses
        self.calculate_duration()
        self.update_status_counts_and_progress_status(final=True)
        self._generate_final_report()

    def _generate_final_report(self) -> None:
        """Generate a detailed report of sequence execution"""
        if not self.is_closed_or_skipped:
            return
            
        report_parts = [
            f"Sequence {self.sequence_ref} Final Report",
            f"Status: {self.progress_status.name}",
            f"Duration: {self.duration_s:.2f}s",
            f"Total Steps: {len(self.steps)}",
            f"Status Summary: {self._status_counts.get_summary()}"
        ]
        
        # Add step details
        if self.steps:
            report_parts.append("\nStep Details:")
            for step in self.steps.values():
                if not step.disabled:
                    report_parts.append(f"  {step}")
                    
        self._final_report = "\n".join(report_parts)

    @property
    def final_report(self) -> Optional[str]:
        """Get sequence completion report"""
        if not self._final_report and self.is_closed_or_skipped:
            self._generate_final_report()
        return self._final_report

    def nb_tasks(self) -> int:
        """
        Get total number of tasks in sequence.
        Only counts enabled tasks.
        """
        if not self.steps:
            return 0
            
        return sum(
            step.nb_tasks() 
            for step in self.steps.values() 
            if not step.disabled and hasattr(step, 'nb_tasks')
        )

    def __str__(self):
        """Generate string representation with status info"""
        sequence_status = f"[Sequence {self.sequence_ref} :: Status: {self.progress_status.name}]"
        
        if self._status_counts.total_count > 0:
            sequence_status += f" [{self._status_counts.get_summary()}]"
            
        steps_str = "\n".join(f"    {str(step)}" for step in self.steps.values())
        return f"{sequence_status}\n{steps_str}"

    
###############################################################################################
########################################   PipelineDynamicIterator   ########################################
class PipelineDynamicIterator(Step):
    def __init__(self,
                 name: str,
                 iteration_template: PipelineSequenceTemplate,
                 dependencies: Optional[List[Union[str, Dependency]]] = None,
                 disabled: bool = False,
                 max_iterations_allowed: Optional[int] = 100,
                 max_issues_allowed: Optional[int] = 3,
                 max_warnings_allowed: Optional[int] = 3):
        super().__init__(name=name, disabled=disabled, dependencies=dependencies, issues_allowed=max_issues_allowed>0)
        self._iteration_template = iteration_template
        self._iterations: Dict[Union[int, str], PipelineSequence] = {}
        self._max_iterations_allowed = max_iterations_allowed
        self._max_issues_allowed = max_issues_allowed
        self._max_warnings_allowed = max_warnings_allowed
        self._status_counts = StatusCounts()
        self._final_report = None
        self._iteration_reports: Dict[Union[int, str], str] = {}

    @property
    def iteration_template(self) -> PipelineSequenceTemplate:
        return self._iteration_template

    @property
    def iterations(self) -> Dict[Union[int, str], PipelineSequence]:
        return self._iterations

    @property
    def total_iterations(self) -> int:
        return len(self._iterations)
        
    @property
    def status_counts(self) -> StatusCounts:
        return self._status_counts

    @property
    def max_iterations_allowed(self) -> int:
        return self._max_iterations_allowed
    
    @max_iterations_allowed.setter
    def max_iterations_allowed(self, value: int) -> None:
        if value < 0:
            raise ValueError("Max iterations must be positive")
        self._max_iterations_allowed = value

    @property
    def max_issues_allowed(self) -> int:
        return self._max_issues_allowed
    
    @max_issues_allowed.setter
    def max_issues_allowed(self, value: int) -> None:
        if value < 0:
            raise ValueError("Max issues must be positive")
        self._max_issues_allowed = value

    @property
    def max_warnings_allowed(self) -> int:
        return self._max_warnings_allowed
    
    @max_warnings_allowed.setter
    def max_warnings_allowed(self, value: int) -> None:
        if value < 0:
            raise ValueError("Max warnings must be positive")
        self._max_warnings_allowed = value

    def can_continue(self) -> Tuple[bool, Optional[str]]:
        """
        Check if iterator can continue based on status counts and limits.
        Returns tuple of (can_continue, reason_if_cannot)
        """
        if self.is_closed_or_skipped:
            return False, f"Iterator is already closed with status {self.progress_status}"
            
        if self.total_iterations == 0:
            return False, "No iterations configured"
            
        # Use status counts to check limits
        failures_count = self.status_counts.get_category_count('failure_statuses')
        if failures_count > self.max_issues_allowed:
            return False, f"Max issues exceeded: {failures_count} > {self.max_issues_allowed}"
            
        warning_count = self.status_counts.count_statuses(ProgressStatus.DONE_WITH_WARNINGS)
        if warning_count > self.max_warnings_allowed:
            return False, f"Max warnings exceeded: {warning_count} > {self.max_warnings_allowed}"
            
        # Check if we've hit max iterations
        if self.total_iterations >= self.max_iterations_allowed:
            return False, f"Max iterations reached: {self.total_iterations} >= {self.max_iterations_allowed}"
            
        return True, None

    def set_iterations_from_refs(self, iteration_refs: List[Union[int, str]]) -> None:
        """Set up iterations for given references"""
        if len(iteration_refs) > self.max_iterations_allowed:
            raise ValueError(f"Cannot set {len(iteration_refs)} iterations - exceeds max_iterations {self.max_iterations_allowed}")
        
        self._iterations = {}
        for ref in iteration_refs:
            self.add_iteration_from_ref(ref)

    def add_iteration_from_ref(self, iteration_ref: Union[int, str]) -> None:
        """Add a single iteration if limits not exceeded"""
            
        sequence = PipelineSequence(
            sequence_ref=iteration_ref,
            sequence_template=self.iteration_template
        )
        if self._pipeline_flow:
            sequence.set_pipeline_flow(self._pipeline_flow)
        self._iterations[iteration_ref] = sequence

    def remove_iteration(self, iteration_ref: Union[int, str]):
        """Remove an iteration by reference"""
        if iteration_ref in self._iterations:
            del self._iterations[iteration_ref]

    def clear_iterations(self):
        """Remove all iterations"""
        self._iterations.clear()

    def get_iteration(self, iteration_ref: Union[int, str]) -> Optional[PipelineSequence]:
        """Get iteration by reference"""
        if iteration_ref not in self._iterations:
            raise KeyError(f"Iteration {iteration_ref} not found in {self.name}")
        return self._iterations[iteration_ref]

    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow'):
        """Set pipeline flow for self and all iterations"""
        super().set_pipeline_flow(pipeline_flow)
        for iteration in self._iterations.values():
            iteration.set_pipeline_flow(pipeline_flow)

    def validate_and_start(self, set_status: Optional[ProgressStatus]=ProgressStatus.IN_PROGRESS,
                      sequence_ref: Optional[Union[int, str]]=None) -> Tuple[bool, Optional[str]]:
        """
        Enhanced validation for dynamic iterator including iteration checks.
        """
        # First validate common step requirements
        is_valid, error = super().validate_and_start(set_status, sequence_ref)
        if not is_valid:
            return False, error

        # Validate iterator-specific requirements
        if self.total_iterations == 0:
            self.progress_status = ProgressStatus.INTENTIONALLY_SKIPPED
            return False, "No iterations configured"

        if self._max_iterations_allowed < self.total_iterations:
            self.progress_status = ProgressStatus.FAILED
            err_msg = f"Total iterations {self.total_iterations} exceeds max {self._max_iterations_allowed}"
            return False, err_msg

        self.progress_status = set_status
        return True, None
    

    def nb_tasks(self) -> int:
        """
        Get total number of tasks across all iterations.
        Accounts for disabled steps.
        """
        if not self.iteration_template or not self.iterations:
            return 0
            
        template_tasks = sum(
            step.nb_tasks() if hasattr(step, 'nb_tasks') else 1
            for step in self.iteration_template.steps.values()
            if not step.disabled
        )
        
        return template_tasks * self.total_iterations

    def collect_status_counts(self) -> StatusCounts:
        """Collect status counts from iterations without modifying them"""
        counts = StatusCounts()
        if not self.iterations:
            return counts
            
        for iteration in self.iterations.values():
            if not iteration.disabled:
                counts.add_status(iteration.progress_status)
                
        return counts

    def update_status_counts_and_progress_status(self, final: bool) -> None:
        """Update own status based on current iteration statuses"""
        counts = self.collect_status_counts()
        self._status_counts = counts  # Store for reporting
        
        # Update own status based on counts
        self.progress_status = eval_statuses(
            counts,
            final=final,
            issues_allowed=self.issues_allowed
        )

    def final(self, force_if_closed:bool=False) -> None:
        """
        Finalize iterator using current iteration statuses.
        Does not modify child iterations - assumes their statuses are already final or will be evaluated as FAILED
        """
        if self.is_closed_or_skipped and not force_if_closed:
            return
            
        # Calculate own duration and status based on current iteration statuses
        self.calculate_duration()
        self.update_status_counts_and_progress_status(final=True)
        self._generate_final_report()


    def get_status_counts_across_iterations_for_step(self, step_name: str) -> Union[Dict[str, int], StatusCounts]:
        """
        Get status counts for a specific step across all iterations.
        
        Args:
            step_name: Name of the step to analyze
            
        Returns:
            StatusCounts object containing aggregated status info
            
        Raises:
            KeyError: If step not found in template
            ValueError: If no iterations exist
        """
        if step_name not in self.iteration_template.steps:
            raise KeyError(f"Step {step_name} not found in template")
            
        counts = StatusCounts()
        
        # Early return if no iterations
        if not self.iterations:
            return counts

        # Count statuses across iterations
        for iteration in self.iterations.values():
            if step_name in iteration.steps and not iteration.steps[step_name].disabled:
                counts.add_status(iteration.steps[step_name].progress_status)
                
        return counts

    @property
    def final_report(self) -> Optional[str]:
        """Get iterator completion report"""
        if not self._final_report and self.is_closed_or_skipped:
            self._generate_final_report()
        return self._final_report
        
    @property
    def iteration_reports(self) -> Dict[Union[int, str], str]:
        """Get individual iteration reports"""
        return self._iteration_reports

    def _generate_final_report(self) -> None:
        """Generate a detailed report of iterator execution"""
        if not self.is_closed_or_skipped:
            return

        report_parts = [
            f"Iterator {self.name} Final Report",
            f"Status: {self.progress_status.name}",
            f"Duration: {self.duration_s:.2f}s",
            f"Total Iterations: {self.total_iterations}",
            f"Status Summary: {self._status_counts.get_summary()}\n"
        ]

        # Add step status summaries across iterations
        if self.iteration_template.steps:
            report_parts.append("Step Status Summary Across Iterations:")
            for step_name in self.iteration_template.steps:
                step_counts = self.get_status_counts_across_iterations_for_step(step_name)
                report_parts.append(f"  {step_name}: {step_counts.get_summary()}")

        # Store individual iteration reports
        if self.iterations:
            report_parts.append("\nIteration Reports:")
            for ref, iteration in self.iterations.items():
                if iteration.final_report:
                    self._iteration_reports[ref] = iteration.final_report
                    report_parts.append(f"\n  Iteration {ref}:")
                    report_parts.extend(f"    {line}" for line in iteration.final_report.splitlines())

        self._final_report = "\n".join(report_parts)


    def __str__(self):
        indent=0
        header = f"{' ' * indent}**  {self.name} [Status: {self.progress_status.name}]"
        if self.iterations:
            if not self.status_counts:
                self.update_status_counts_and_progress_status(final=False)

            iteration_info = (f"Total Iterations: {self.total_iterations}, Total_Statuses: {self.status_counts.total_count}, "
                                + ", ".join(f"{status}: {count}" for status, count in self.status_counts.by_status_count if count > 0))
            header += f" [{iteration_info}]"
        else:
            header += " [No iterations yet]"

        # Template tasks with their aggregated statuses
        template_flow = []
        for step_name in self._iteration_template.steps:
            if self.iterations:
                step_status_counts = self.get_status_counts_across_iterations_for_step(step_name=step_name)
                step_info =  (f"[Total Iterations: {self.total_iterations}, "
                                + ", ".join(f"{status}: {count}" for status, count in step_status_counts.by_status_count if count > 0))
                template_flow.append(
                    f"{' ' * (indent + 2)}>> {step_name} {step_info}"
                )
            else:
                template_flow.append(
                    f"{' ' * (indent + 2)}>> {step_name} [No iterations yet]"
                )
        return f"{header}\n{chr(10).join(template_flow)}" if template_flow else header


def _validate_step_name(name: str) -> bool:
    """Validate step name format"""
    if not isinstance(name, str):
        raise ValueError("Step name must be a string")
    if not name.strip():
        raise ValueError("Step name cannot be empty")
    if len(name) > 128:
        raise ValueError("Step name too long (max 128 chars)")
    return True


###############################################################################################
########################################   PipelineFlow   ########################################

class PipelineFlow(PipelineSequence):
    """Top-level pipeline sequence that manages the entire pipeline execution"""
    
    def __init__(self,
                 base_context_name: str, 
                 steps: Optional[List[Step]] = None,
                 disabled: bool = False,
                 config: Optional[Dict] = None,
                 issues_allowed: bool = True,
                 dependencies: Optional[List[Union[str, Dependency]]] = None):
        super().__init__(
            sequence_ref=base_context_name,
            steps=steps,
            dependencies=dependencies,
            issues_allowed=issues_allowed,
            disabled=disabled,
            config=config
        )
        self.base_context = base_context_name
        self._pipelineflow_id=uuid.uuid4()
        self.set_pipeline_flow(self)# Self-reference for consistent step access
      
        
        # Task tracking
        self._total_tasks = sum(step.nb_tasks() for step in (steps or []))
        self._closed_tasks = 0


    @property
    def completion_percentage(self) -> float:
        """Get completion percentage based on tasks"""
        if self._total_tasks == 0:
            return 0.0
        return round((self._closed_tasks / self._total_tasks) * 100, 2)

    def update_task_completion(self, completed: int):
        """Update completed task count"""
        self._closed_tasks = min(
            self._closed_tasks + completed,
            self._total_tasks
        )

    def add_step(self, step: Step) -> bool:
        """Add a step to the pipeline with validation.
        
        Returns:
            bool: True if step was added, False if disabled or already exists
        """
        if step.disabled:
            return False

        _validate_step_name(step.name)
        
        if step.name in self.steps:
            raise ValueError(f"Step with name '{step.name}' already exists")

        self.steps[step.name] = step
        step.set_pipeline_flow(self)
        self._total_tasks += step.nb_tasks()
        return True
    

    def validate_and_start(self, set_status: Optional[ProgressStatus]=ProgressStatus.IN_PROGRESS) -> Tuple[bool, Optional[str]]:
        """Validate and start pipeline execution"""
        # First check disabled state
        if self.disabled:
            self.progress_status = ProgressStatus.DISABLED
            return False, "Pipeline is disabled"
            
        # Validate pipeline dependencies
        try:
            self.validate_steps_dependencies_exist()
        except ValueError as e:
            self.progress_status = ProgressStatus.FAILED
            return False, str(e)
        
        # Start execution tracking
        self._start_time = datetime.now(timezone.utc)
        self.progress_status = set_status
        return True, None

    def final(self, force_if_closed:bool=False) -> None:
        """Finalize entire pipeline"""
        if self.is_closed_or_skipped and not force_if_closed:
            return
            
        # First finalize all steps
        for step in self.steps.values():
            if not step.disabled:
                step.final()
                
        # Then finalize pipeline
        self.calculate_duration()
        self.update_status_counts_and_progress_status(final=True)
        self._generate_final_report()

    def _generate_final_report(self) -> None:
        """Generate detailed pipeline execution report"""
        if not self.is_closed_or_skipped:
            return
            
        report_parts = [
            f"Pipeline Context: {self.base_context}",
            f"Pipelineflow_ID: {self._pipelineflow_id}",
            f"Status: {self.progress_status.name}",
            f"Duration: {self.duration_s:.2f}s",
            f"Progress: {self.completion_percentage:.1f}%",
            f"Tasks: {self._closed_tasks}/{self._total_tasks}",
            f"\nStatus Summary: {self._status_counts.get_summary()}"
        ]
        
        # Add individual step reports
        if self.steps:
            report_parts.append("\nStep Details:")
            for step in self.steps.values():
                if hasattr(step, 'final_report') and step.final_report:
                    report_parts.append(f"\n{step.final_report}")
                else:
                    report_parts.append(f"\n{str(step)}")
                    
        self._final_report = "\n".join(report_parts)

    # @property
    # def final_report(self) -> Optional[str]:
    #     """Get pipeline completion report"""
    #     if not self._final_report and self.is_closed_or_skipped:
    #         self._generate_final_report()
    #     return self._final_report

    def get_step(self, name: str, sequence_ref: Optional[Union[int, str]] = None) -> Step:
        """Get step by name with improved error handling."""
        try:
            # First check direct steps
            if name in self.steps:
                return self.steps[name]

            # Search in dynamic iterators
            for step in self.steps.values():
                if isinstance(step, PipelineDynamicIterator):
                    # Check specific iteration if reference provided
                    if sequence_ref is not None and sequence_ref in step.iterations:
                        iteration = step.iterations[sequence_ref]
                        if name in iteration.steps:
                            return iteration.steps[name]
                    # Check template steps
                    elif name in step.iteration_template.steps:
                        return step.iteration_template.steps[name]

            raise KeyError(f"Step '{name}' not found")
        except Exception as e:
            raise KeyError(
                f"Step '{name}' not found in pipeline flow "
                f"{'or specified iteration' if sequence_ref else ''}"
            ) from e

    def get_pipeline_flow_str(self) -> str:
        """Generate detailed pipeline flow string with metrics and status breakdown"""
        status_info = ""
        if self.status_counts:
            status_info = (
                f"Status Breakdown:\n"
                + "\n".join(f"  {status}: {count}" 
                           for status, count in self.status_counts.by_status_count.items()
                           if count > 0)
            )
            
        lines = [
            f"Pipeline: {self.base_context}",
            f"Status: {self.progress_status.name}",
            f"Progress: {self.completion_percentage}%",
            f"Duration: {self.duration_s:.1f}s",
            f"Total Tasks: {self._total_tasks}",
            status_info,
            "Steps:",
            "-------"
        ]

        for step in self.steps.values():
            if not step.disabled:
                lines.append(str(step))

        return "\n".join(lines)

    def validate_steps_dependencies_exist(self) -> bool:
        """Validate all pipeline dependencies"""
        def _validate_step_dependencies(step: Step, path: List[str]) -> None:
            current_path = path + [step.name]

            # Check for circular dependencies
            if len(set(current_path)) != len(current_path):
                cycle = current_path[current_path.index(step.name):]
                raise ValueError(f"Circular dependency detected: {' -> '.join(cycle)}")

            # Validate direct dependencies
            for dep in step.dependencies:
                if isinstance(dep, str):
                    dep = Dependency(dep)
                try:
                    dep_step = self.get_step(dep.step_name)
                    if not dep.optional:
                        _validate_step_dependencies(dep_step, current_path)
                except KeyError as exc:
                    if not dep.optional:
                        raise ValueError(
                            f"Missing required dependency '{dep.step_name}' for step '{step.name}'. "
                            f"Path: {' -> '.join(current_path)}"
                        ) from exc

            # Validate template steps for dynamic iterators
            if isinstance(step, PipelineDynamicIterator):
                for template_step in step._iteration_template.steps.values():
                    _validate_step_dependencies(template_step, current_path)

        # Always validate every step
        for step in self.steps.values():
            _validate_step_dependencies(step, [])

        return True

    def get_pipeline_description(self) -> str:
        """
        Generate the complete pipeline description with base context and pipeline flow.
        :return: String representing the pipeline description.
        """
        return f"{self.base_context}\nflow:\n{self.get_pipeline_flow_str()}"

    @property
    def progress_status(self) -> ProgressStatus:
        """Get progress status"""
        return self._progress_status
        
    @progress_status.setter 
    def progress_status(self, value: ProgressStatus):
        """Set progress status - removed completion tracking from here since it's handled in update_status_counts_and_progress_status"""
        self._progress_status = value
        # Removed the completion tracking from here since it's now handled in update_status_counts_and_progress_status

    def _count_closed_tasks_recursively(self, step: Step) -> int:
        """Recursively count closed tasks in a step and its children"""
        if step.disabled:
            return 0
            
        if isinstance(step, PipelineSequence):
            # For sequences, count tasks in child steps
            return sum(
                self._count_closed_tasks_recursively(child_step)
                for child_step in step.steps.values()
            )
        elif isinstance(step, PipelineDynamicIterator):
            # For iterators, count tasks in iterations
            return sum(
                self._count_closed_tasks_recursively(iteration)
                for iteration in step.iterations.values()
            )
        else:
            # For regular tasks, count if closed or skipped
            return 1 if step.progress_status in ProgressStatus.closed_or_skipped_statuses() else 0

    def update_status_counts_and_progress_status(self, final: bool) -> None:
        """Update own status based on current step statuses and track completions"""
        counts = self.collect_status_counts()
        self._status_counts = counts
        
        # Count completed tasks recursively through all steps and their children
        self._closed_tasks = sum(
            self._count_closed_tasks_recursively(step)
            for step in self.steps.values()
        )
        
        # Update own status based on counts
        self._progress_status = eval_statuses(
            counts,
            final=final,
            issues_allowed=self.issues_allowed
        )