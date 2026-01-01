# Todo - Advanced In-Memory Python Console Todo App

An advanced, menu-driven console todo application that stores tasks only in memory. Built for Hackathon to demonstrate core and advanced task management features with clean code and spec-driven development. Includes support for recurring tasks, due dates with time, and visual indicators for overdue and upcoming tasks.

## Features

- Add new tasks with title and description
- View all tasks with ID, title, description, and completion status
- Update existing task details (title or description)
- Delete tasks by ID
- Mark tasks as complete/incomplete (toggle status)
- Set due dates with time support (with flexible input formats like "tomorrow 3pm", "next monday 9:00", "in 2 hours")
- Create recurring tasks with various patterns (daily, weekly, monthly, yearly, custom intervals)
- Visual indicators for overdue (red/bold) and upcoming tasks (highlighted)
- Dedicated views for overdue and upcoming tasks
- Automatic creation of next occurrence for completed recurring tasks
- Flexible date/time input parsing using natural language

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
Advanced Todo CLI App
1. Add new task - With prompts for due date/time and recurrence
2. View all tasks - Enhanced with due dates and recurrence indicators
3. Update existing task - With options to change due date/time and recurrence
4. Delete task
5. Mark task as complete/incomplete
6. Show overdue tasks - Dedicated view for overdue items
7. Show upcoming tasks - Dedicated view for upcoming items
0. Quit
Enter your choice:
```

### Adding a Task
1. Select option 1
2. Enter the task title when prompted
3. Optionally enter a task description
4. Optionally enter a due date/time (supports flexible formats like "tomorrow 3pm", "next monday 9:00", "in 2 hours")
5. Optionally enter a recurrence pattern (e.g., "daily", "weekly", "monthly", "every 3 days")
6. The task will be added with a unique ID

### Viewing Tasks
1. Select option 2
2. All tasks will be displayed in a table format with ID, title, description, completion status, due date (with visual indicators for overdue/upcoming tasks), and recurrence pattern

### Updating a Task
1. Select option 3
2. Enter the task ID you want to update
3. Enter the new title (or press Enter to keep current)
4. Enter the new description (or press Enter to keep current)
5. Optionally enter a new due date/time (or press Enter to keep current)
6. Optionally enter a new recurrence pattern (or press Enter to keep current)

### Deleting a Task
1. Select option 4
2. Enter the task ID you want to delete
3. Confirm the deletion if prompted

### Marking Task Complete/Incomplete
1. Select option 5
2. Enter the task ID you want to toggle
3. The completion status will be toggled
4. If the task is recurring, a new occurrence will be automatically created with an updated due date

### Viewing Overdue Tasks
1. Select option 6
2. All overdue tasks will be displayed with special highlighting (red/bold)

### Viewing Upcoming Tasks
1. Select option 7
2. All tasks due within the next 24 hours will be displayed with special highlighting

### Quitting the Application
1. Select option 0
2. The application will exit

## Error Handling

The application handles various error conditions gracefully:
- Invalid menu options will show an error message and return to the main menu
- Invalid task IDs will show an error message
- Empty titles will be rejected when adding tasks
- Invalid date/time formats will show an error message
- Invalid recurrence patterns will show an error message
- Other invalid inputs will be handled with appropriate error messages

## Development

This project was built using Spec-Driven Development methodology with Qwen AI assistance. All specifications, plans, and tasks are preserved in the `specs/` directory for auditability.

## License

This project is open source and available under the MIT License.