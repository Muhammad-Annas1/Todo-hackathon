# Feature Specification: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders

**Feature Branch**: `002-recurring-tasks-reminders`
**Created**: 2026-01-01
**Status**: Draft
**Input**: User description: "Advanced Level Specification - Todo CLI App (Intelligent Features) Project: Todo (In-Memory Python Console Todo App) Level: Advanced (builds on Basic + Intermediate) Target model: Qwen (Qwen2.5-Coder preferred) or any strong coding model Goal: Basic + organized todo app ko intelligent aur future-ready banane ke liye recurring tasks aur proper time-based reminders add karna Must-have new features (Advanced level): 1. Recurring Tasks - Support repeating patterns: daily, weekly, monthly, yearly - Optional: every X days/weeks (e.g. every 3 days, every 2 weeks) - When task is marked complete → auto-create next occurrence with updated due date - Show recurrence pattern in view list (e.g. \"↻ weekly\") 2. Due Dates with Time - Full datetime support (date + time) - Input formats: flexible (YYYY-MM-DD HH:MM, tomorrow 3pm, next monday 9:00, in 2 hours, etc.) - Display format in view: relative (\"in 2h\", \"tomorrow 9:00\") + absolute 3. Reminders / Overdue Awareness - In-app reminder system: - When viewing list → show overdue tasks in red/bold (if rich used) - Show upcoming tasks (e.g. due in next 24h) highlighted - Optional stretch: simple timed console notification (thread/timer based) - Note: No real browser/push notifications (CLI limitation) — only in-app visual + audio beep if possible Data Model Changes: - Task fields to add/update: - due_datetime: datetime.datetime | None - recurrence: str | None # e.g. \"weekly\", \"every 3 days\", \"monthly\" - next_occurrence: datetime.datetime | None (for calculation) CLI / UX Changes: - Add task: extra questions for due date/time + recurrence (optional) - Update task: allow changing due date/time + recurrence - View list: enhanced columns → Due (relative), Recurrence - New menu options / sub-menu: - Show upcoming (next 24h/7d) - Show overdue - Auto-reschedule logic when toggling complete on recurring task Important Constraints: - Still 100% in-memory (no persistence in Advanced level either) - Use datetime module + dateutil (if allowed) for parsing flexible dates - Dependencies: - optional rich (strongly recommended now) - optional python-dateutil (for better natural language date parsing) - Keep console responsive — no blocking long timers - Existing basic + intermediate features must remain fully functional Success Criteria: - Can create weekly grocery task → mark complete → next week instance auto appears - Due dates with time show correctly (past/future, relative time) - Overdue tasks clearly visible every time user opens list - Flexible date input works reasonably well - App remains fast & clean even with 50+ tasks Not in scope for Advanced: - File/database persistence (save/load) - Real system notifications / tray icon - Mobile/web sync - AI smart suggestions - Calendar integration Qwen output expectation: - Updated Task data model with new fields - Suggested natural date parsing strategy - Logic for auto-rescheduling recurring tasks - Proposed menu extensions - Key function signatures / pseudo-code for critical parts"

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Create Recurring Tasks (Priority: P1)

As a user, I want to create tasks that repeat on a schedule (daily, weekly, monthly, yearly) so that I don't have to manually re-add routine tasks like weekly grocery shopping or monthly bill payments.

**Why this priority**: This is the core functionality that differentiates the advanced todo app from basic ones, providing significant value by reducing repetitive work.

**Independent Test**: Can be fully tested by creating a recurring task with a specified pattern and verifying that the task is properly stored with its recurrence information.

**Acceptance Scenarios**:

1. **Given** I am on the add task screen, **When** I create a task and specify a recurrence pattern (e.g., "weekly"), **Then** the task is saved with the recurrence information and appears in my task list.
2. **Given** I have a recurring task in my list, **When** I view the task details, **Then** I can see the recurrence pattern associated with the task.

---

### User Story 2 - Set Due Dates with Time (Priority: P1)

As a user, I want to set specific due dates and times for my tasks so that I can manage my schedule more precisely and receive timely reminders.

**Why this priority**: Time-based due dates are essential for task management and enable the overdue awareness feature that users need.

**Independent Test**: Can be fully tested by creating a task with a due date and time and verifying that the due date is properly stored and displayed.

**Acceptance Scenarios**:

1. **Given** I am on the add task screen, **When** I specify a due date and time (e.g., "tomorrow 3pm"), **Then** the task is saved with the due datetime and appears in my task list with the due information.
2. **Given** I have a task with a due date and time, **When** I view the task list, **Then** I can see the due date and time displayed in a user-friendly format.

---

### User Story 3 - Auto-create Next Occurrence (Priority: P2)

As a user, I want completed recurring tasks to automatically generate the next occurrence with an updated due date so that I don't miss future instances of routine tasks.

**Why this priority**: This feature ensures continuity of recurring tasks without user intervention, maintaining the value of the recurring task functionality.

**Independent Test**: Can be fully tested by completing a recurring task and verifying that a new instance with an updated due date is created.

**Acceptance Scenarios**:

1. **Given** I have a recurring task in my list, **When** I mark it as complete, **Then** a new instance of the task is automatically created with the next occurrence's due date.
2. **Given** I have completed a recurring task, **When** I view my task list, **Then** I see the new occurrence of the task with the updated due date.

---

### User Story 4 - View Overdue and Upcoming Tasks (Priority: P2)

As a user, I want to easily identify overdue and upcoming tasks when viewing my list so that I can prioritize my work effectively.

**Why this priority**: Visual indicators for overdue and upcoming tasks help users manage their time and responsibilities more effectively.

**Independent Test**: Can be fully tested by creating tasks with past and future due dates and verifying that they are visually distinguished in the task list.

**Acceptance Scenarios**:

1. **Given** I have overdue tasks in my list, **When** I view the task list, **Then** overdue tasks are highlighted (e.g., in red or bold).
2. **Given** I have upcoming tasks due soon, **When** I view the task list, **Then** these tasks are highlighted to indicate their proximity.

---

### User Story 5 - Flexible Date Input (Priority: P3)

As a user, I want to enter due dates in flexible formats (e.g., "tomorrow 3pm", "next monday 9:00", "in 2 hours") so that I can quickly specify times without using complex date formats.

**Why this priority**: This improves user experience by allowing natural language input for dates and times, making the app more intuitive to use.

**Independent Test**: Can be fully tested by entering various flexible date formats and verifying they are correctly parsed and stored.

**Acceptance Scenarios**:

1. **Given** I am adding a task, **When** I enter a flexible date format like "tomorrow 3pm", **Then** the system correctly interprets and stores the appropriate datetime.
2. **Given** I have entered a flexible date format, **When** I view the task, **Then** the due date is displayed in a standard format.

---

### User Story 6 - Update Task Due Dates and Recurrence (Priority: P3)

As a user, I want to modify the due date and recurrence pattern of existing tasks so that I can adjust my schedule when circumstances change.

**Why this priority**: This provides flexibility to adapt recurring tasks to changing needs without having to delete and recreate them.

**Independent Test**: Can be fully tested by updating an existing task's due date and recurrence pattern and verifying the changes are saved.

**Acceptance Scenarios**:

1. **Given** I have a task with a due date and recurrence pattern, **When** I update these values, **Then** the changes are saved and reflected in the task list.
2. **Given** I have updated a recurring task, **When** I mark it as complete, **Then** the next occurrence follows the updated recurrence pattern.

---

### Edge Cases

- What happens when a recurring task is marked complete close to the end of a month (e.g., January 31st with a monthly recurrence)?
- How does the system handle tasks with due dates in the past when first implemented?
- What happens if the user tries to set a recurrence pattern that would create conflicts with other tasks?
- How does the system handle invalid or ambiguous date/time inputs?
- What happens when the app is opened after being closed for an extended period with multiple overdue tasks?

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: System MUST support creating tasks with recurrence patterns (daily, weekly, monthly, yearly, and custom intervals like "every 3 days")
- **FR-002**: System MUST store due date and time information for each task
- **FR-003**: Users MUST be able to specify due dates using flexible input formats (e.g., "tomorrow 3pm", "next monday 9:00", "in 2 hours")
- **FR-004**: System MUST automatically create the next occurrence of a recurring task when the current one is marked as complete
- **FR-005**: System MUST visually distinguish overdue tasks in the task list (e.g., with red text or bold formatting)
- **FR-006**: System MUST highlight upcoming tasks (due within 24 hours) in the task list
- **FR-007**: Users MUST be able to update the due date and recurrence pattern of existing tasks
- **FR-008**: System MUST display due dates in both relative format ("in 2 hours", "tomorrow") and absolute format (date/time)
- **FR-009**: System MUST parse natural language date/time inputs
- **FR-010**: System MUST maintain all existing basic and intermediate todo app functionality

*Example of marking unclear requirements:*

- **FR-011**: System MUST handle recurrence calculations for month-end dates by using the last day of the month when the target month has fewer days than the original date (e.g., a task set for Jan 31 that repeats monthly would occur on Feb 28 or Feb 29 in leap years)
- **FR-012**: System MUST provide visual indicators for overdue and upcoming tasks, with optional audio beep for console notifications

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single task with properties including title, description, status (completed/incomplete), due date and time, recurrence pattern, and next occurrence date
- **RecurrencePattern**: Defines how a task repeats, including type (daily, weekly, monthly, yearly, custom interval) and any additional parameters for custom intervals

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: Users can create a recurring task (e.g., weekly grocery shopping) and mark it complete, resulting in the automatic creation of the next occurrence with an updated due date
- **SC-002**: Due dates with time are displayed correctly in both relative format ("in 2 hours") and absolute format (date/time) in the task list
- **SC-003**: Overdue tasks are clearly visible with visual indicators every time users open the task list
- **SC-004**: Flexible date input works correctly for at least 80% of common natural language date formats (e.g., "tomorrow 3pm", "next monday", "in 2 hours")
- **SC-005**: The application remains responsive and performs well with up to 50 tasks without noticeable lag
- **SC-006**: Users can successfully update due dates and recurrence patterns for existing tasks without losing other task information