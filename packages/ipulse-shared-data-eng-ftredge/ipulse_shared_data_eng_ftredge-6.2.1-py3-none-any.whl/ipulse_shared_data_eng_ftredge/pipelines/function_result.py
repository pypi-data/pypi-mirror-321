from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Union, List
from datetime import datetime, timezone
import json
import uuid
from ipulse_shared_base_ftredge import (ProgressStatus,
                                        StatusTrackingMixin,
                                        to_enum)

@dataclass
class FunctionResult(StatusTrackingMixin):
    """Base class for function results with status tracking"""
    name: str = field(default_factory=lambda: str(uuid.uuid4()))
    _data: Any = None
    _start_time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    _duration_s: float = 0.0

    def __post_init__(self):
        super().__init__()
        # Set initial status to IN_PROGRESS
        self.progress_status = ProgressStatus.IN_PROGRESS

    @property
    def data(self) -> Any:
        """Get data"""
        return self._data
    
    @data.setter
    def data(self, value: Any) -> None:
        """Set data"""
        self._data = value

    def add_data(self, values: Any, name: str) -> None:
        """Add data to a dict with a name"""
        if not self.data:
            self.data = {}
        elif not isinstance(self.data, dict):
            raise ValueError("Data must be a dictionary to add more values")
        self.data[name] = values

    @property
    def execution_state(self) -> List[str]:
        """Get execution state"""
        return self._execution_state

    @property
    def execution_state_str(self) -> Optional[str]:
        """Get execution state as a formatted string"""
        if not self._execution_state:
            return None
        return "\n".join(f">>[[{entry}]]" for entry in self._execution_state)

    def add_state(self, state: str) -> None:
        """Add execution state with a timestamp"""
        timestamp = datetime.now(timezone.utc).isoformat()
        self._execution_state.append(f"[t:{timestamp}]--{state}")

    @property
    def issues(self) -> List[Any]:
        """Get issues"""
        return self._issues

    @property
    def issues_str(self) -> Optional[str]:
        """Get issues as a string"""
        if not self._issues:
            return None
        return "\n".join(f">>[i:{issue}]" for issue in self._issues)

    def add_issue(self, issue: Any, update_state:bool=True) -> None:
        """Add issue"""
        if issue:
            self._issues.append(issue)
            if update_state:
                self.add_state(f"Issue: {issue}")

    @property
    def warnings(self) -> List[Any]:
        """Get warnings"""
        return self._warnings

    @property
    def warnings_str(self) -> Optional[str]:
        """Get warnings as a string"""
        if not self._warnings:
            return None
        return "\n".join(f">>[w:{warning}]" for warning in self._warnings)

    def add_warning(self, warning: Any,update_state:bool=True) -> None:
        """Add warning"""
        if warning:
            self._warnings.append(warning)
            if update_state:
                self.add_state(f"Warning: {warning}")

    @property
    def notices(self) -> List[Any]:
        """Get notices"""
        return self._notices

    @property
    def notices_str(self) -> Optional[str]:
        """Get notices as a string"""
        if not self._notices:
            return None
        return "\n".join(f">>[n:{notice}]" for notice in self._notices)

    def add_notice(self, notice: Any,update_state:bool=True ) -> None:
        """Add notice"""
        if notice:
            self._notices.append(notice)
            if update_state:
                self.add_state(f"Notice: {notice}")

    def get_notes(self, exclude_none: bool = True) -> str:
        """Get all notes"""
        notes = {
            "ISSUES": self.issues_str,
            "WARNINGS": self.warnings_str,
            "NOTICES": self.notices_str
        }
        if exclude_none:
            notes = {k: v for k, v in notes.items() if v is not None}
        
        if not notes:
            return ""
            
        return "\n".join(f">>{k}: {v}" for k, v in notes.items())
    
    # ------------------
    # Metadata
    # ------------------
    @property
    def metadata(self) -> Dict[str, Any]:
        """Get metadata"""
        return self._metadata
    
    @metadata.setter
    def metadata(self, value: Dict[str, Any]) -> None:
        """Set metadata"""
        self._metadata = value

    def add_metadata(self, **kwargs) -> None:
        """Add metadata key-value pairs"""

        self.metadata.update(kwargs)

    def add_metadata_from_dict(self, metadata: Dict[str, Any]) -> None:
        """Add metadata from a dictionary"""
        self.metadata.update(metadata)

    # ------------------
    # Timing
    # ------------------
    @property
    def start_time(self) -> datetime:
        """Get start time"""
        return self._start_time

    @property
    def duration_s(self) -> float:
        """Get duration in seconds"""
        return self._duration_s
    
    @duration_s.setter
    def duration_s(self, value: float) -> None:
        """Set duration in seconds"""
        self._duration_s = value

    def calculate_duration(self) -> None:
        """Set final duration in seconds"""
        self._duration_s = (datetime.now(timezone.utc) - self.start_time).total_seconds()

    # ------------------
    # Aggregation
    # ------------------

    def integrate_result(self, child_result: "FunctionResult", issues_allowed:bool=True, combine_status=True, final:bool=False,
                          skip_data: bool = True, skip_metadata: bool = True) -> None:
        """Integrate a child operation result into this result"""
        # Integrate status tracking including metadata handling
        self.integrate_status_tracker(
            next=child_result,
            combine_status=combine_status,
            skip_metadata=skip_metadata,
            issues_allowed=issues_allowed,
            name=f"Child {child_result.name}"
        )

        # Handle data
        if not skip_data and child_result.data:
            if self._data is None:
                self._data = child_result.data
            elif isinstance(self._data, dict) and isinstance(child_result.data, dict):
                self._data.update(child_result.data)

    # ------------------
    # Closing / Finalizing
    # ------------------

    def final(self, status: Optional[ProgressStatus] = None, force_if_closed: bool = True, issues_allowed:bool=False,raise_issue_on_unknown: bool = True) -> None:
        """Mark operation as complete"""

        if self.is_closed:
            if force_if_closed:
                if status:
                    if self.progress_status in ProgressStatus.failure_statuses():
                        self.warnings.append(f"Operation is already closed at value {self.progress_status}, forcing status to {status}")
                    else:
                        self.notices.append(f"Operation is already closed at value {self.progress_status}, forcing status to {status}")
                    self.progress_status = to_enum(value=status, enum_class=ProgressStatus, required=True, default=ProgressStatus.UNKNOWN)
            else:
                self.notices.append(f"Operation is already closed, not changing status to {status} because force_if_closed is False")
        elif status:
            self.progress_status = to_enum(value=status, enum_class=ProgressStatus, required=True, default=ProgressStatus.UNKNOWN)
            if self.progress_status == ProgressStatus.UNKNOWN:
                if raise_issue_on_unknown:
                    raise ValueError("Invalid final Progress Status provided")
                else:
                    self.warnings.append(f"Invalid final Progress Status provided: {status}")
        elif self.issues or self.progress_status==ProgressStatus.IN_PROGRESS_WITH_ISSUES:
            if issues_allowed:
                self.progress_status = ProgressStatus.FINISHED_WITH_ISSUES
            else:
                self.progress_status = ProgressStatus.FAILED
        elif self.warnings or self.progress_status==ProgressStatus.IN_PROGRESS_WITH_WARNINGS:
            self.progress_status = ProgressStatus.DONE_WITH_WARNINGS
        elif self.notices or self.progress_status==ProgressStatus.IN_PROGRESS_WITH_NOTICES:
            self.progress_status = ProgressStatus.DONE_WITH_NOTICES
        else:
            self.progress_status = ProgressStatus.DONE
        if self.progress_status == ProgressStatus.UNKNOWN and raise_issue_on_unknown:
            raise ValueError("Invalid final Progress Status provided")
        self.calculate_duration()
        self.add_state("CLOSED STATUS")

    def get_status_report(self, exclude_none: bool = True) -> str:
        """Get all information as a JSON string"""
        # Start with parent class status info
        info_dict = json.loads(super().get_status_report(exclude_none=False)) # Will be filtered once at the end for all fields
        
        # Add FunctionResult specific fields
        info_dict.update({
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "duration_s": self.duration_s
        })
        
        if exclude_none:
            info_dict = {k: v for k, v in info_dict.items() if v is not None}
            
        return json.dumps(info_dict, default=str, indent=2)

    def to_dict(self, infos_as_str: bool = True, exclude_none: bool = True) -> Dict[str, Any]:
        """Convert to dictionary format"""
        # Get base status dict from parent
        status_dict = super().to_dict(infos_as_str=infos_as_str, exclude_none=False) # Will be filtered once at the end for all fields
        
        # Add FunctionResult specific fields
        status_dict.update({
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "duration_s": self.duration_s
        })
        
        if exclude_none:
            status_dict = {k: v for k, v in status_dict.items() if v is not None}

        result = {
            "data": self.data,
            "status": status_dict
        }
        
        if exclude_none and result["data"] is None:
            result.pop("data")
            
        return result

    # Can remove __str__ since it's inherited from mixin
