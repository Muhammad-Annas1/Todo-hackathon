# API Contracts: Console Todo App

## Function Interfaces

### add_task(title: str, description: str = "") -> None
**Purpose**: Add a new task to the todo list
**Parameters**:
- title (str): The task title (required, non-empty)
- description (str): The task description (optional)
**Returns**: None
**Side Effects**: Adds a new task to the global tasks list with a unique ID and incomplete status

### view_tasks() -> None
**Purpose**: Display all tasks in a formatted table
**Parameters**: None
**Returns**: None
**Side Effects**: Prints the task list to stdout

### update_task(task_id: int, new_title: str | None = None, new_desc: str | None = None) -> bool
**Purpose**: Update an existing task's title or description
**Parameters**:
- task_id (int): The ID of the task to update
- new_title (str | None): New title for the task (optional)
- new_desc (str | None): New description for the task (optional)
**Returns**: True if update was successful, False otherwise
**Side Effects**: Modifies the specified task in the global tasks list

### delete_task(task_id: int) -> bool
**Purpose**: Remove a task from the todo list
**Parameters**:
- task_id (int): The ID of the task to delete
**Returns**: True if deletion was successful, False otherwise
**Side Effects**: Removes the specified task from the global tasks list

### toggle_complete(task_id: int) -> bool
**Purpose**: Toggle the completion status of a task
**Parameters**:
- task_id (int): The ID of the task to toggle
**Returns**: True if toggle was successful, False otherwise
**Side Effects**: Changes the completion status of the specified task

### find_task_by_id(task_id: int) -> dict | None
**Purpose**: Find a task by its ID
**Parameters**:
- task_id (int): The ID of the task to find
**Returns**: The task dictionary if found, None otherwise
**Side Effects**: None

### generate_next_id() -> int
**Purpose**: Generate the next available task ID
**Parameters**: None
**Returns**: The next available integer ID
**Side Effects**: None (pure function)