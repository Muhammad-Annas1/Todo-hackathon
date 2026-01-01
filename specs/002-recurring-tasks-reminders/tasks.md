# Tasks: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders

**Feature**: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders  
**Branch**: 002-recurring-tasks-reminders  
**Generated**: 2026-01-01  
**Based on**: specs/002-recurring-tasks-reminders/spec.md, plan.md, data-model.md, contracts/

## Implementation Strategy

This implementation follows an incremental delivery approach, starting with the core functionality and building up features. The MVP will include basic recurring tasks and due dates (US1 and US2), with additional features added in subsequent phases.

## Dependencies

- User Story 1 (Create Recurring Tasks) and User Story 2 (Set Due Dates with Time) can be developed in parallel
- User Story 3 (Auto-create Next Occurrence) depends on US1 and US2
- User Story 4 (View Overdue and Upcoming Tasks) depends on US2
- User Story 5 (Flexible Date Input) can be developed in parallel with US2
- User Story 6 (Update Task Due Dates and Recurrence) depends on US1 and US2

## Parallel Execution Examples

- T001-T004 can be executed in parallel with T005-T007
- T015 [P] [US1] and T016 [P] [US2] can be developed simultaneously
- T025 [P] [US4] and T026 [P] [US5] can be developed simultaneously

## Phase 1: Setup

### Goal
Initialize the project structure and set up dependencies required for the advanced features.

### Tasks
- [X] T001 Create models directory: src/models/
- [X] T002 Create services directory: src/services/
- [X] T003 Create lib directory: src/lib/
- [X] T004 Install rich library for visual indicators: pip install rich
- [X] T005 Install python-dateutil for flexible date parsing: pip install python-dateutil
- [X] T006 Create task.py file in src/models/
- [X] T007 Create date_parser.py file in src/services/
- [X] T008 Create recurrence.py file in src/services/
- [X] T009 Create reminder.py file in src/services/
- [X] T010 Create utils.py file in src/lib/

## Phase 2: Foundational

### Goal
Implement the core data model and foundational services that will be used across all user stories.

### Tasks
- [X] T011 [P] Implement Task class with due_datetime, recurrence, and next_occurrence fields in src/models/task.py
- [X] T012 [P] Implement validation rules for Task entity in src/models/task.py
- [X] T013 [P] Implement parse_flexible_date function in src/services/date_parser.py
- [X] T014 [P] Implement calculate_next_occurrence function in src/services/recurrence.py
- [X] T015 [P] [US1] Update existing task management functions to handle new fields in src/services/task_service.py
- [X] T016 [P] [US2] Create helper functions for relative date display in src/lib/utils.py

## Phase 3: User Story 1 - Create Recurring Tasks (Priority: P1)

### Goal
Enable users to create tasks that repeat on a schedule (daily, weekly, monthly, yearly).

### Independent Test Criteria
Can be fully tested by creating a recurring task with a specified pattern and verifying that the task is properly stored with its recurrence information.

### Tasks
- [X] T017 [US1] Add recurrence parameter to add_task function in src/services/task_service.py
- [X] T018 [US1] Implement recurrence pattern validation in src/services/recurrence.py
- [X] T019 [US1] Update CLI to prompt for recurrence pattern when adding tasks in src/cli/todo_app.py
- [X] T020 [US1] Add recurrence display to task view in src/cli/todo_app.py
- [X] T021 [US1] Test creating recurring tasks with different patterns

## Phase 4: User Story 2 - Set Due Dates with Time (Priority: P1)

### Goal
Allow users to set specific due dates and times for their tasks to manage their schedule more precisely.

### Independent Test Criteria
Can be fully tested by creating a task with a due date and time and verifying that the due date is properly stored and displayed.

### Tasks
- [X] T022 [US2] Update Task class to handle due_datetime field in src/models/task.py
- [X] T023 [US2] Update add_task function to accept due_datetime parameter in src/services/task_service.py
- [X] T024 [US2] Update CLI to prompt for due date/time when adding tasks in src/cli/todo_app.py
- [X] T025 [US2] Implement due date display formatting in src/lib/utils.py
- [X] T026 [US2] Update task display to show due dates in src/cli/todo_app.py
- [X] T027 [US2] Test creating tasks with various due dates and times

## Phase 5: User Story 5 - Flexible Date Input (Priority: P3)

### Goal
Allow users to enter due dates in flexible formats (e.g., "tomorrow 3pm", "next monday 9:00", "in 2 hours").

### Independent Test Criteria
Can be fully tested by entering various flexible date formats and verifying they are correctly parsed and stored.

### Tasks
- [X] T028 [US5] Implement flexible date parsing using dateutil in src/services/date_parser.py
- [X] T029 [US5] Add error handling for invalid date formats in src/services/date_parser.py
- [X] T030 [US5] Integrate flexible date parsing with CLI input in src/cli/todo_app.py
- [X] T031 [US5] Test various flexible date formats: "tomorrow 3pm", "next monday 9:00", "in 2 hours"
- [X] T032 [US5] Test error handling for invalid date formats

## Phase 6: User Story 3 - Auto-create Next Occurrence (Priority: P2)

### Goal
Automatically generate the next occurrence of completed recurring tasks with an updated due date.

### Independent Test Criteria
Can be fully tested by completing a recurring task and verifying that a new instance with an updated due date is created.

### Tasks
- [X] T033 [US3] Implement create_next_occurrence function in src/services/recurrence.py
- [X] T034 [US3] Update toggle_task_completion to handle recurring tasks in src/services/task_service.py
- [X] T035 [US3] Add logic to calculate next occurrence when marking recurring tasks complete in src/services/recurrence.py
- [X] T036 [US3] Test completing recurring tasks and verifying next occurrence creation
- [X] T037 [US3] Handle edge cases for month-end dates in recurrence calculations

## Phase 7: User Story 4 - View Overdue and Upcoming Tasks (Priority: P2)

### Goal
Easily identify overdue and upcoming tasks when viewing the task list to prioritize work effectively.

### Independent Test Criteria
Can be fully tested by creating tasks with past and future due dates and verifying that they are visually distinguished in the task list.

### Tasks
- [X] T038 [US4] Implement get_overdue_tasks function in src/services/reminder.py
- [X] T039 [US4] Implement get_upcoming_tasks function in src/services/reminder.py
- [X] T040 [US4] Add overdue task highlighting using rich in src/cli/todo_app.py
- [X] T041 [US4] Add upcoming task highlighting using rich in src/cli/todo_app.py
- [X] T042 [US4] Add dedicated menu options for showing overdue and upcoming tasks in src/cli/todo_app.py
- [X] T043 [US4] Test visual indicators for overdue and upcoming tasks
- [X] T044 [US4] Test dedicated views for overdue and upcoming tasks

## Phase 8: User Story 6 - Update Task Due Dates and Recurrence (Priority: P3)

### Goal
Modify the due date and recurrence pattern of existing tasks to adjust the schedule when circumstances change.

### Independent Test Criteria
Can be fully tested by updating an existing task's due date and recurrence pattern and verifying the changes are saved.

### Tasks
- [X] T045 [US6] Update update_task function to handle due_datetime and recurrence fields in src/services/task_service.py
- [X] T046 [US6] Update CLI to prompt for due date/time and recurrence when updating tasks in src/cli/todo_app.py
- [X] T047 [US6] Test updating due dates and recurrence patterns of existing tasks
- [X] T048 [US6] Verify that updates don't affect other task properties

## Phase 9: Polish & Cross-Cutting Concerns

### Goal
Final integration, testing, and polish to ensure all features work together seamlessly.

### Tasks
- [X] T049 Integrate all new features with existing functionality
- [X] T050 Test end-to-end workflows combining multiple features
- [X] T051 Add comprehensive error handling throughout the application
- [X] T052 Perform performance testing with up to 50 tasks
- [X] T053 Update README with new feature documentation
- [X] T054 Run final integration tests
- [X] T055 Verify all acceptance scenarios from user stories pass
- [X] T056 Code review and refactoring if needed