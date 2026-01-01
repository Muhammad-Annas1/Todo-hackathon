# Todo - In-Memory Python Console Todo App

A simple, menu-driven console todo application that stores tasks only in memory. Built for Hackathon Phase I to demonstrate core task management features with clean code and spec-driven development.

## Features

- Add new tasks with title and description
- View all tasks with ID, title, description, and completion status
- Update existing task details (title or description)
- Delete tasks by ID
- Mark tasks as complete/incomplete (toggle status)

## Requirements

- Python 3.13+
- UV package manager (optional, for dependency management)

## Setup

1. Ensure you have Python 3.13+ installed
2. Install UV package manager if not already installed:
   ```bash
   pip install uv
   ```
3. Clone or download this project
4. Navigate to the project directory
5. Install dependencies (if using UV):
   ```bash
   uv sync
   ```
   Or if using standard pip:
   ```bash
   pip install -e .
   ```

## Running the Application

To run the console todo application:

```bash
python src/todo.py
```

## Using the Application

Once the application starts, you'll see a menu with the following options:

```
===== Console Todo App =====
1. Add new task
2. View all tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
0. Quit
Choose an option:
```

### Adding a Task
1. Select option 1
2. Enter the task title when prompted
3. Optionally enter a task description
4. The task will be added with a unique ID

### Viewing Tasks
1. Select option 2
2. All tasks will be displayed in a table format with ID, title, description, and completion status

### Updating a Task
1. Select option 3
2. Enter the task ID you want to update
3. Enter the new title (or press Enter to keep current)
4. Enter the new description (or press Enter to keep current)

### Deleting a Task
1. Select option 4
2. Enter the task ID you want to delete
3. Confirm the deletion if prompted

### Marking Task Complete/Incomplete
1. Select option 5
2. Enter the task ID you want to toggle
3. The completion status will be toggled

### Quitting the Application
1. Select option 0
2. The application will exit

## Error Handling

The application handles various error conditions gracefully:
- Invalid menu options will show an error message and return to the main menu
- Invalid task IDs will show an error message
- Empty titles will be rejected when adding tasks
- Other invalid inputs will be handled with appropriate error messages

## Development

This project was built using Spec-Driven Development methodology with Qwen AI assistance. All specifications, plans, and tasks are preserved in the `specs/` directory for auditability.

## License

This project is open source and available under the MIT License.