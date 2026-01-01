"""
Recurrence calculation service
"""
from datetime import datetime, timedelta
from typing import Optional
import re


def calculate_next_occurrence(current_date: datetime, recurrence_pattern: str) -> datetime:
    """
    Calculates the next occurrence date based on the current date and recurrence pattern.

    Args:
        current_date: The current occurrence date
        recurrence_pattern: The recurrence pattern (e.g., "daily", "weekly", "every 3 days")

    Returns:
        The calculated next occurrence date
    """
    pattern = recurrence_pattern.lower().strip()
    
    # Handle simple patterns
    if pattern == "daily":
        return current_date + timedelta(days=1)
    elif pattern == "weekly":
        return current_date + timedelta(weeks=1)
    elif pattern == "monthly":
        # Handle month-end dates by using the last day of the next month
        next_month = current_date.month + 1
        next_year = current_date.year
        if next_month > 12:
            next_month = 1
            next_year += 1
        
        # Get the last day of the next month to handle month-end dates
        if next_month in [4, 6, 9, 11]:
            max_day = 30
        elif next_month == 2:
            # Check for leap year
            if next_year % 4 == 0 and (next_year % 100 != 0 or next_year % 400 == 0):
                max_day = 29
            else:
                max_day = 28
        else:
            max_day = 31
        
        # Use the minimum of current day and max day for the next month
        day = min(current_date.day, max_day)
        return current_date.replace(year=next_year, month=next_month, day=day)
    elif pattern == "yearly":
        # Handle leap year case for Feb 29
        if current_date.month == 2 and current_date.day == 29:
            # If it's Feb 29 in a leap year, use Feb 28 in the next year
            return current_date.replace(year=current_date.year + 1, day=28)
        else:
            return current_date.replace(year=current_date.year + 1)
    
    # Handle "every X [time_unit]" patterns
    match = re.match(r"every (\d+) (day|days|week|weeks|month|months|year|years)", pattern)
    if match:
        quantity = int(match.group(1))
        unit = match.group(2)
        
        if "day" in unit:
            return current_date + timedelta(days=quantity)
        elif "week" in unit:
            return current_date + timedelta(weeks=quantity)
        elif "month" in unit:
            # Calculate the target month and year
            total_months = current_date.month + quantity
            target_year = current_date.year + (total_months - 1) // 12
            target_month = ((total_months - 1) % 12) + 1
            
            # Handle month-end dates
            if target_month in [4, 6, 9, 11]:
                max_day = 30
            elif target_month == 2:
                # Check for leap year
                if target_year % 4 == 0 and (target_year % 100 != 0 or target_year % 400 == 0):
                    max_day = 29
                else:
                    max_day = 28
            else:
                max_day = 31
            
            # Use the minimum of current day and max day for the target month
            day = min(current_date.day, max_day)
            return current_date.replace(year=target_year, month=target_month, day=day)
        elif "year" in unit:
            # Handle leap year case for Feb 29
            if current_date.month == 2 and current_date.day == 29:
                # If it's Feb 29 in a leap year, use Feb 28 in the target year
                target_year = current_date.year + quantity
                return current_date.replace(year=target_year, day=28)
            else:
                return current_date.replace(year=current_date.year + quantity)
    
    # If pattern doesn't match any known format, return the same date
    # In a real implementation, this would raise an exception
    return current_date


def validate_recurrence_pattern(pattern: str) -> bool:
    """
    Validates if a recurrence pattern is valid.

    Args:
        pattern: The recurrence pattern to validate

    Returns:
        True if the pattern is valid, False otherwise
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


def create_next_occurrence(task) -> Optional[object]:
    """
    Creates the next occurrence of a recurring task.

    Args:
        task: The completed recurring task (with attributes: title, description, recurrence, etc.)

    Returns:
        The new Task object for the next occurrence, or None if not recurring
    """
    if not task.recurrence:
        return None
    
    from models.task import Task  # Import here to avoid circular dependency
    
    next_due_date = calculate_next_occurrence(task.due_datetime or datetime.now(), task.recurrence)
    
    # Create a new task with the same properties but updated due date
    next_task = Task(
        id=task.id + 1000,  # Use a higher ID to avoid conflicts; in a real app, use proper ID generation
        title=task.title,
        description=task.description,
        completed=False,  # New occurrence is not completed
        due_datetime=next_due_date,
        recurrence=task.recurrence,
        next_occurrence=None  # Will be calculated when this task is completed
    )
    
    return next_task