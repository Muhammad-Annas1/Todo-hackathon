"""
Task management service
"""
from datetime import datetime
from typing import List, Optional
from models.task import Task


class TaskManager:
    """
    Manages a collection of tasks with functionality for CRUD operations
    and handling of recurring tasks.
    """
    
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: str = "", 
                 due_datetime: Optional[datetime] = None, 
                 recurrence: Optional[str] = None) -> Task:
        """
        Creates a new task with optional due date and recurrence pattern.

        Args:
            title: The task title
            description: Optional detailed description
            due_datetime: Optional due date and time
            recurrence: Optional recurrence pattern

        Returns:
            The created Task object
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            due_datetime=due_datetime,
            recurrence=recurrence
        )
        
        self.tasks.append(task)
        self._next_id += 1
        
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, 
                    description: Optional[str] = None,
                    due_datetime: Optional[datetime] = None, 
                    recurrence: Optional[str] = None) -> bool:
        """
        Updates an existing task with new values.

        Args:
            task_id: The ID of the task to update
            title: New title (if updating)
            description: New description (if updating)
            due_datetime: New due date/time (if updating)
            recurrence: New recurrence pattern (if updating)

        Returns:
            True if the operation was successful, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_datetime is not None:
            task.due_datetime = due_datetime
        if recurrence is not None:
            task.recurrence = recurrence
        
        # Re-validate the task after updates
        try:
            task.validate()
        except ValueError:
            # If validation fails, revert the changes
            return False
        
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the operation was successful, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        return True
    
    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggles the completion status of a task.
        If the task is recurring, creates the next occurrence when marked complete.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if the operation was successful, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        
        # Toggle completion status
        task.completed = not task.completed
        
        # If the task was marked as complete and is recurring, create the next occurrence
        if task.completed and task.is_recurring():
            from .recurrence import create_next_occurrence
            next_task = create_next_occurrence(task)
            if next_task:
                # Set the next_id for the new task to be the current max ID + 1
                next_task.id = self._next_id
                self._next_id += 1
                self.tasks.append(next_task)
        
        return True
    
    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks.

        Returns:
            List of all Task objects
        """
        return self.tasks[:]
    
    def get_completed_tasks(self) -> List[Task]:
        """
        Returns all completed tasks.

        Returns:
            List of completed Task objects
        """
        return [task for task in self.tasks if task.completed]
    
    def get_pending_tasks(self) -> List[Task]:
        """
        Returns all pending (not completed) tasks.

        Returns:
            List of pending Task objects
        """
        return [task for task in self.tasks if not task.completed]