"""
Reminder/overdue awareness service
"""
from datetime import datetime, timedelta
from typing import List
from models.task import Task


def get_overdue_tasks(tasks: List[Task]) -> List[Task]:
    """
    Returns all tasks that are past their due date and not completed.

    Returns:
        List of overdue Task objects
    """
    overdue_tasks = []
    now = datetime.now()
    
    for task in tasks:
        if not task.completed and task.due_datetime and task.due_datetime < now:
            overdue_tasks.append(task)
    
    return overdue_tasks


def get_upcoming_tasks(tasks: List[Task], hours: int = 24) -> List[Task]:
    """
    Returns all tasks due within the specified number of hours.

    Args:
        tasks: List of all tasks
        hours: Number of hours to look ahead (default: 24)

    Returns:
        List of upcoming Task objects
    """
    upcoming_tasks = []
    now = datetime.now()
    future_limit = now + timedelta(hours=hours)
    
    for task in tasks:
        if (not task.completed and 
            task.due_datetime and 
            now < task.due_datetime <= future_limit):
            upcoming_tasks.append(task)
    
    return upcoming_tasks


def get_tasks_by_recurrence_pattern(tasks: List[Task], pattern: str) -> List[Task]:
    """
    Returns all tasks with a specific recurrence pattern.

    Args:
        tasks: List of all tasks
        pattern: The recurrence pattern to filter by

    Returns:
        List of tasks with the specified recurrence pattern
    """
    matching_tasks = []
    
    for task in tasks:
        if task.recurrence and task.recurrence.lower() == pattern.lower():
            matching_tasks.append(task)
    
    return matching_tasks