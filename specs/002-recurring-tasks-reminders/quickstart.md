# Quickstart Guide: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders

## Prerequisites

- Python 3.13 or higher
- Optional: `rich` library for enhanced visual formatting
- Optional: `python-dateutil` for advanced date parsing

## Installation

1. Clone or navigate to the project directory
2. Install dependencies (if using optional libraries):
   ```bash
   pip install rich python-dateutil
   ```
3. Run the application:
   ```bash
   python src/todo.py
   ```

## New Features Overview

### 1. Setting Due Dates with Time

When adding or updating tasks, you can now specify due dates using flexible formats:
- "2026-01-15 14:30" - Specific date and time
- "tomorrow 3pm" - Tomorrow at 3 PM
- "next monday 9:00" - Next Monday at 9 AM
- "in 2 hours" - 2 hours from now
- "in 30 minutes" - 30 minutes from now

### 2. Creating Recurring Tasks

When adding or updating tasks, specify a recurrence pattern:
- "daily" - Every day
- "weekly" - Every week
- "monthly" - Every month
- "yearly" - Every year
- "every 3 days" - Every 3 days
- "every 2 weeks" - Every 2 weeks

### 3. Visual Indicators

- **Overdue tasks**: Displayed in red/bold
- **Upcoming tasks** (due within 24 hours): Highlighted or italicized
- **Recurring tasks**: Show recurrence indicator (e.g., "↻ weekly")

## Using the Enhanced CLI

The menu now includes these options:
1. Add new task - With prompts for due date/time and recurrence
2. View all tasks - Enhanced with due dates and recurrence indicators
3. Update existing task - With options to change due date/time and recurrence
4. Delete task
5. Mark task as complete/incomplete
6. Show overdue tasks - Dedicated view for overdue items
7. Show upcoming tasks - Dedicated view for upcoming items
0. Quit

## Example Usage

1. Add a recurring weekly task:
   - Select "Add new task"
   - Enter title: "Weekly team meeting"
   - Enter description: "Attend team sync"
   - Enter due date/time: "next monday 10am"
   - Enter recurrence: "weekly"

2. View tasks with visual indicators:
   - Select "View all tasks"
   - Overdue tasks will appear in red/bold
   - Upcoming tasks will be highlighted
   - Recurring tasks will show the recurrence pattern

3. Complete a recurring task:
   - Select "Mark task as complete/incomplete"
   - Enter the task ID
   - The system will automatically create the next occurrence based on the recurrence pattern