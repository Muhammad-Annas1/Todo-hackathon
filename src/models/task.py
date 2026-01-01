"""
Task model with due date and recurrence fields
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import re


@dataclass
class Task:
    """
    Represents a single task with properties including title, description,
    status (completed/incomplete), due date and time, recurrence pattern,
    and next occurrence date.
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    due_datetime: Optional[datetime] = None
    recurrence: Optional[str] = None
    next_occurrence: Optional[datetime] = None
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        self.validate()

    def validate(self) -> bool:
        """
        Validates the task according to the defined rules:
        - id must be unique across all tasks (checked at application level)
        - title must not be empty
        - due_datetime must be a valid datetime if provided
        - recurrence must be one of the allowed patterns if provided
        - next_occurrence must be a valid datetime if provided
        """
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")

        if self.due_datetime is not None and not isinstance(self.due_datetime, datetime):
            raise ValueError("due_datetime must be a valid datetime object if provided")

        if self.next_occurrence is not None and not isinstance(self.next_occurrence, datetime):
            raise ValueError("next_occurrence must be a valid datetime object if provided")

        if self.recurrence is not None and not self._is_valid_recurrence_pattern(self.recurrence):
            raise ValueError(f"Invalid recurrence pattern: {self.recurrence}")

        return True

    def _is_valid_recurrence_pattern(self, pattern: str) -> bool:
        """
        Validates if a recurrence pattern is valid.
        """
        if not pattern:
            return True  # None/empty is valid (no recurrence)

        pattern = pattern.lower().strip()

        # Check simple patterns
        if pattern in ["daily", "weekly", "monthly", "yearly"]:
            return True

        # Check "every X [time_unit]" patterns
        match = re.match(r"every (\d+) (day|days|week|weeks|month|months|year|years)", pattern)
        if match:
            quantity = int(match.group(1))
            # Ensure quantity is positive
            return quantity > 0

        return False

    def is_overdue(self) -> bool:
        """Check if the task is overdue (not completed and past due date)"""
        if self.completed or self.due_datetime is None:
            return False
        return datetime.now() > self.due_datetime

    def is_upcoming(self, hours: int = 24) -> bool:
        """Check if the task is upcoming within the specified number of hours"""
        if self.completed or self.due_datetime is None:
            return False
        time_diff = self.due_datetime - datetime.now()
        return 0 < time_diff.total_seconds() <= hours * 3600

    def is_recurring(self) -> bool:
        """Check if the task is recurring"""
        return self.recurrence is not None and self.recurrence.strip() != ""