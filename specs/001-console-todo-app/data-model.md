# Data Model: Console Todo App

## Task Entity

**Definition**: Represents a single todo item with ID, title, description, and completion status

**Fields**:
- `id` (int): Auto-generated incremental unique identifier
- `title` (str): Task title provided by the user
- `description` (str): Optional task description provided by the user
- `completed` (bool): Status indicator (True for complete, False for incomplete)

**Validation Rules**:
- `id` must be a positive integer
- `title` must not be empty or None
- `completed` must be a boolean value

**State Transitions**:
- `completed` can transition from False to True (incomplete → complete)
- `completed` can transition from True to False (complete → incomplete)

**Example**:
```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": False
}
```

## Global State

**Definition**: In-memory storage for all tasks

**Structure**: List of Task dictionaries

**Variable Name**: `tasks`

**Initial State**: Empty list `[]`

**Access Pattern**: Direct access to the global variable from all functions that need to read or modify tasks