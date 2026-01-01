# Data Model: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders

## Task Entity

The Task entity will be enhanced to support recurring tasks and due dates with time.

### Fields

- **id**: `int` - Unique identifier for the task (auto-incremented)
- **title**: `str` - The task title/description
- **description**: `str` - Detailed description of the task (optional)
- **completed**: `bool` - Whether the task is completed (default: False)
- **due_datetime**: `datetime | None` - The due date and time for the task (default: None)
- **recurrence**: `str | None` - The recurrence pattern (e.g., "daily", "weekly", "monthly", "yearly", "every 3 days") (default: None)
- **next_occurrence**: `datetime | None` - The next occurrence date for recurring tasks (default: None)
- **created_at**: `datetime` - The timestamp when the task was created

### Relationships

- No direct relationships with other entities (standalone entity)

### Validation Rules

- `id` must be unique across all tasks
- `title` must not be empty
- `due_datetime` must be a valid datetime if provided
- `recurrence` must be one of the allowed patterns if provided
- `next_occurrence` must be a valid datetime if provided

### State Transitions

- When a recurring task is marked as complete:
  - Calculate the next occurrence based on the recurrence pattern
  - Create a new task with the same title and description but updated due date
  - Update the `next_occurrence` field of the original task
- When a task is marked as incomplete:
  - No special action required

## RecurrencePattern Value Object

### Definition

A value object representing the recurrence pattern for a task.

### Allowed Values

- "daily" - Recurs every day
- "weekly" - Recurs every week
- "monthly" - Recurs every month
- "yearly" - Recurs every year
- "every X days" - Recurs every X days (where X is a positive integer)
- "every X weeks" - Recurs every X weeks (where X is a positive integer)
- "every X months" - Recurs every X months (where X is a positive integer)
- "every X years" - Recurs every X years (where X is a positive integer)

### Constraints

- Custom patterns must follow the format "every [positive integer] [time unit]"
- Time units must be one of: "days", "weeks", "months", "years"