# Function Contracts: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders

## Core Task Management Functions

### Task Creation
```python
def add_task(title: str, description: str = "", due_datetime: datetime | None = None, recurrence: str | None = None) -> Task:
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
```

### Task Completion
```python
def toggle_task_completion(task_id: int) -> bool:
    """
    Toggles the completion status of a task.
    If the task is recurring, creates the next occurrence when marked complete.
    
    Args:
        task_id: The ID of the task to toggle
    
    Returns:
        True if the operation was successful, False otherwise
    """
```

### Task Update
```python
def update_task(task_id: int, title: str | None = None, description: str | None = None, 
                due_datetime: datetime | None = None, recurrence: str | None = None) -> bool:
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
```

## Recurrence Management Functions

### Calculate Next Occurrence
```python
def calculate_next_occurrence(current_date: datetime, recurrence_pattern: str) -> datetime:
    """
    Calculates the next occurrence date based on the current date and recurrence pattern.
    
    Args:
        current_date: The current occurrence date
        recurrence_pattern: The recurrence pattern (e.g., "daily", "weekly", "every 3 days")
    
    Returns:
        The calculated next occurrence date
    """
```

### Create Next Occurrence
```python
def create_next_occurrence(task: Task) -> Task | None:
    """
    Creates the next occurrence of a recurring task.
    
    Args:
        task: The completed recurring task
    
    Returns:
        The new Task object for the next occurrence, or None if not recurring
    """
```

## Date/Time Parsing Functions

### Parse Flexible Date
```python
def parse_flexible_date(date_string: str) -> datetime | None:
    """
    Parses a flexible date string into a datetime object.
    Supports formats like "tomorrow 3pm", "next monday 9:00", "in 2 hours", etc.
    
    Args:
        date_string: The date string to parse
    
    Returns:
        The parsed datetime object, or None if parsing fails
    """
```

## Reminder/Awareness Functions

### Get Overdue Tasks
```python
def get_overdue_tasks() -> list[Task]:
    """
    Returns all tasks that are past their due date and not completed.
    
    Returns:
        List of overdue Task objects
    """
```

### Get Upcoming Tasks
```python
def get_upcoming_tasks(hours: int = 24) -> list[Task]:
    """
    Returns all tasks due within the specified number of hours.
    
    Args:
        hours: Number of hours to look ahead (default: 24)
    
    Returns:
        List of upcoming Task objects
    """
```

## CLI Interface Functions

### Display Task List
```python
def display_task_list(tasks: list[Task]) -> None:
    """
    Displays a list of tasks with visual indicators for due dates and recurrence.
    
    Args:
        tasks: List of tasks to display
    """
```

### Display Overdue Tasks
```python
def display_overdue_tasks() -> None:
    """
    Displays all overdue tasks with special highlighting.
    """
```

### Display Upcoming Tasks
```python
def display_upcoming_tasks(hours: int = 24) -> None:
    """
    Displays all tasks due within the specified number of hours with special highlighting.
    
    Args:
        hours: Number of hours to look ahead (default: 24)
    """
```