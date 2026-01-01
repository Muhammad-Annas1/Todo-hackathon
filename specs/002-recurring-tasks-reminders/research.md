# Research Summary: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders

## Decision: Date/Time Parsing Strategy
**Rationale**: The feature requires flexible date/time input parsing to handle formats like "tomorrow 3pm", "next monday 9:00", "in 2 hours", etc. The most robust solution is to use the `dateutil.parser` library which can handle many natural language formats.
**Alternatives considered**: 
- Manual parsing with regex (complex and limited)
- Using datetime.strptime (requires specific formats, not flexible)
- dateutil.parser (recommended, handles natural language well)

## Decision: Recurrence Calculation Algorithm
**Rationale**: For recurring tasks, we need to calculate the next occurrence based on the recurrence pattern. Using Python's `dateutil.rrule` or implementing custom logic with `timedelta` operations provides the necessary functionality for daily, weekly, monthly, and yearly recurrences.
**Alternatives considered**:
- dateutil.rrule (powerful but potentially overkill)
- Custom timedelta logic (simpler for basic patterns)
- Third-party recurrence libraries (adds complexity)

## Decision: Visual Indicators for Overdue/Upcoming Tasks
**Rationale**: To highlight overdue and upcoming tasks, we'll use the `rich` library which provides color formatting, bold text, and other visual enhancements for console applications.
**Alternatives considered**:
- ANSI escape codes (works but less maintainable)
- Rich library (recommended, clean and feature-rich)
- Colorama library (alternative for cross-platform color support)

## Decision: Task Model Enhancement
**Rationale**: The existing task model needs to be extended to include due_datetime, recurrence pattern, and next_occurrence fields. This requires updating the Task class/data structure.
**Alternatives considered**:
- Adding fields to existing dictionary structure (simple but less structured)
- Creating a proper Task class with methods (recommended, more maintainable)

## Decision: Storage Strategy
**Rationale**: Maintaining the in-memory constraint while adding new fields to tasks. The existing list/dictionary approach can accommodate new fields without persistence.
**Alternatives considered**:
- Continue with in-memory list of dictionaries (maintains existing approach)
- In-memory Task objects (more structured, better for complex features)