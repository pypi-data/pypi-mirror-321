import pytest
from datetime import datetime, timezone, timedelta
from ipulse_shared_base_ftredge import ProgressStatus, Action, DataResource
from ipulse_shared_data_eng_ftredge.pipelines.pipelineflow import (
    Dependency, DependencyType, Step, PipelineTask, PipelineSequence,
    PipelineDynamicIterator, PipelineFlow, PipelineSequenceTemplate
)

# -------------------- Fixtures --------------------
@pytest.fixture
def simple_task():
    return PipelineTask("test_task", Action.READ, DataResource.FILE)

@pytest.fixture
def simple_sequence():
    return PipelineSequence("seq1", steps=[
        PipelineTask("task1", Action.READ, DataResource.FILE),
        PipelineTask("task2", Action.PERSIST_WRITE, DataResource.FILE)
    ])

@pytest.fixture
def template_with_tasks():
    tasks = [
        PipelineTask("template_task1", Action.READ, DataResource.FILE),
        PipelineTask("template_task2", Action.PERSIST_WRITE, DataResource.FILE)
    ]
    return PipelineSequenceTemplate(tasks)

# -------------------- Dependency Tests --------------------
class TestDependency:
    def test_init(self):
        dep = Dependency("step1", DependencyType.TO_SUCCESS)
        assert dep.step_name == "step1"
        assert dep.requirement == DependencyType.TO_SUCCESS
        assert not dep.optional
        assert dep.timeout_s is None

    def test_start_timeout(self):
        dep = Dependency("step1", timeout_s=10)
        before = datetime.now()
        dep.start_timeout()
        assert isinstance(dep._start_time, datetime)
        assert before <= dep._start_time <= datetime.now()

    def test_is_timeout(self):
        dep = Dependency("step1", timeout_s=1)
        dep.start_timeout()
        assert not dep.is_timeout()
        # Wait for timeout
        import time
        time.sleep(1.1)
        assert dep.is_timeout()

    def test_check_satisfied(self, simple_task):
        dep = Dependency("step1", DependencyType.TO_SUCCESS)
        simple_task.progress_status = ProgressStatus.DONE
        assert dep.check_satisfied(simple_task)

        simple_task.progress_status = ProgressStatus.FAILED
        assert not dep.check_satisfied(simple_task)

# -------------------- Step Tests --------------------
class TestStep:
    def test_init(self):
        step = Step("test_step")
        assert step.name == "test_step"
        assert not step.disabled
        assert step.progress_status == ProgressStatus.NOT_STARTED
        assert step.dependencies == []

    def test_validate_and_start(self):
        step = Step("test_step")
        success, reason = step.validate_and_start()
        assert success
        assert step.progress_status == ProgressStatus.IN_PROGRESS

    def test_disabled_step(self):
        step = Step("test_step", disabled=True)
        success, reason = step.validate_and_start()
        assert not success
        assert step.progress_status == ProgressStatus.DISABLED

    def test_duration_tracking(self):
        step = Step("test_step")
        step.validate_and_start()
        assert step.duration_s > 0
        step.calculate_duration()
        assert isinstance(step.duration_s, float)

# -------------------- PipelineTask Tests --------------------
class TestPipelineTask:
    def test_init(self):
        task = PipelineTask("task1", Action.READ, DataResource.FILE)
        assert task.name == "task1"
        assert task.action == Action.READ
        assert task.source == DataResource.FILE
        assert task.nb_tasks() == 1

    def test_incorporate_function_result(self):
        from ipulse_shared_data_eng_ftredge.pipelines.function_result import FunctionResult
        task = PipelineTask("task1")
        result = FunctionResult()
        result.progress_status = ProgressStatus.DONE
        task.incorporate_function_result(result)
        assert task.progress_status == ProgressStatus.DONE

# -------------------- PipelineSequence Tests --------------------
class TestPipelineSequence:
    def test_init(self):
        sequence = PipelineSequence("seq1")
        assert sequence.sequence_ref == "seq1"
        assert sequence.steps == {}

    def test_add_step(self, simple_task):
        sequence = PipelineSequence("seq1")
        sequence.add_step(simple_task)
        assert "test_task" in sequence.steps
        assert sequence.nb_tasks() == 1

    def test_collect_status_counts(self, simple_sequence):
        counts = simple_sequence.collect_status_counts()
        assert counts.total_count == 2
        assert counts.get_category_count('pending_statuses') == 2

    def test_update_status_counts_and_progress_status(self, simple_sequence):
        for step in simple_sequence.steps.values():
            step.progress_status = ProgressStatus.DONE
        simple_sequence.update_status_counts_and_progress_status(final=True)
        assert simple_sequence.progress_status == ProgressStatus.DONE

# -------------------- PipelineDynamicIterator Tests --------------------
class TestPipelineDynamicIterator:
    def test_init(self, template_with_tasks):
        iterator = PipelineDynamicIterator("iterator1", template_with_tasks)
        assert iterator.name == "iterator1"
        assert iterator.total_iterations == 0
        assert iterator.max_iterations_allowed == 100

    def test_set_iterations_from_refs(self, template_with_tasks):
        iterator = PipelineDynamicIterator("iterator1", template_with_tasks)
        iterator.set_iterations_from_refs([1, 2, 3])
        assert iterator.total_iterations == 3
        assert all(ref in iterator.iterations for ref in [1, 2, 3])

    def test_max_iterations_limit(self, template_with_tasks):
        iterator = PipelineDynamicIterator("iterator1", template_with_tasks, max_iterations_allowed=2)
        with pytest.raises(ValueError):
            iterator.set_iterations_from_refs([1, 2, 3])

    def test_can_continue(self, template_with_tasks):
        iterator = PipelineDynamicIterator("iterator1", template_with_tasks)
        iterator.set_iterations_from_refs([1])
        can_continue, reason = iterator.can_continue()
        assert can_continue
        
        # Test max issues
        iterator._status_counts.add_status(ProgressStatus.FAILED)
        iterator._status_counts.add_status(ProgressStatus.FAILED)
        iterator._status_counts.add_status(ProgressStatus.FAILED)
        iterator._status_counts.add_status(ProgressStatus.FAILED)
        can_continue, reason = iterator.can_continue()
        assert not can_continue
        assert "Max issues exceeded" in reason

# -------------------- PipelineFlow Tests --------------------
class TestPipelineFlow:
    def test_init(self):
        flow = PipelineFlow("test_pipeline")
        assert flow.base_context == "test_pipeline"
        assert flow.completion_percentage == 0.0

    def test_add_step(self, simple_task):
        flow = PipelineFlow("test_pipeline")
        assert flow.add_step(simple_task)
        assert simple_task.name in flow.steps
        assert flow._total_tasks == 1

    def test_update_task_completion(self):
        flow = PipelineFlow("test_pipeline")
        flow._total_tasks = 10
        flow.update_task_completion(3)
        assert flow._closed_tasks == 3
        assert flow.completion_percentage == 30.0

    def test_get_step(self, simple_task):
        flow = PipelineFlow("test_pipeline")
        flow.add_step(simple_task)
        assert flow.get_step(simple_task.name) == simple_task
        with pytest.raises(KeyError):
            flow.get_step("nonexistent_step")

    def test_validate_steps_dependencies_exist(self):
        flow = PipelineFlow("test_pipeline")
        task1 = PipelineTask("task1")
        task2 = PipelineTask("task2", dependencies=[Dependency("task1")])
        flow.add_step(task1)
        flow.add_step(task2)
        assert flow.validate_steps_dependencies_exist()

        # Test missing dependency
        flow = PipelineFlow("test_pipeline")
        task_with_missing_dep = PipelineTask("task1", dependencies=[Dependency("nonexistent")])
        flow.add_step(task_with_missing_dep)
        with pytest.raises(ValueError):
            flow.validate_steps_dependencies_exist()

    def test_final_report_generation(self, simple_sequence):
        flow = PipelineFlow("test_pipeline")
        flow.add_step(simple_sequence)
        for step in simple_sequence.steps.values():
            step.progress_status = ProgressStatus.DONE
        flow.final()
        report = flow.final_report
        assert isinstance(report, str)
        assert "Pipeline Context: test_pipeline" in report
        assert "Status: DONE" in report

    def test_completion_tracking(self, simple_task):
        """Test that completion percentage updates correctly as tasks complete"""
        flow = PipelineFlow("test_pipeline")
        flow.add_step(simple_task)
        
        # Initially 0%
        assert flow.completion_percentage == 0.0
        assert flow._closed_tasks == 0
        
        # Update task status to DONE
        simple_task.progress_status = ProgressStatus.DONE
        flow.update_status_counts_and_progress_status(final=True)
        
        # Should now be 100% as the only task is complete
        print("FLOW STATUSSSS", flow.final_report)
        assert flow._closed_tasks == 1
        assert flow.completion_percentage == 100.0

    def test_completion_tracking_multiple_tasks(self, simple_sequence):
        """Test completion tracking with multiple tasks"""
        flow = PipelineFlow("test_pipeline")
        flow.add_step(simple_sequence)  # Contains 2 tasks
        
        # Initially 0%
        assert flow.completion_percentage == 0.0
        assert flow._closed_tasks == 0
        
        # Complete first task
        tasks = list(simple_sequence.steps.values())
        tasks[0].progress_status = ProgressStatus.DONE
        flow.update_status_counts_and_progress_status(final=False)
        
        # Should be 50% complete
        assert flow._closed_tasks == 1
        assert flow.completion_percentage == 50.0
        
        # Complete second task
        tasks[1].progress_status = ProgressStatus.DONE
        flow.update_status_counts_and_progress_status(final=False)
        
        # Should now be 100%
        assert flow._closed_tasks == 2
        assert flow.completion_percentage == 100.0

    def test_completion_with_skipped_tasks(self, simple_sequence):
        """Test completion tracking handles skipped tasks correctly"""
        flow = PipelineFlow("test_pipeline")
        flow.add_step(simple_sequence)
        
        # Skip one task, complete another
        tasks = list(simple_sequence.steps.values())
        tasks[0].progress_status = ProgressStatus.INTENTIONALLY_SKIPPED
        tasks[1].progress_status = ProgressStatus.DONE
        flow.update_status_counts_and_progress_status(final=False)
        
        # Both skipped and completed tasks count toward completion
        assert flow._closed_tasks == 2
        assert flow.completion_percentage == 100.0
