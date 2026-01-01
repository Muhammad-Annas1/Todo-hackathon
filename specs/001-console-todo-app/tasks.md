---

description: "Task list for Console Todo App implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 [P] Create src directory
- [x] T003 [P] Create pyproject.toml with project metadata
- [x] T004 [P] Create README.md with setup instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create todo.py main application file with basic structure
- [x] T006 Implement Task data model with ID, title, description, and completion status
- [x] T007 Implement global tasks storage (list of dictionaries)
- [x] T008 Implement generate_next_id() helper function
- [x] T009 Implement find_task_by_id() helper function

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks to their todo list with a title and description

**Independent Test**: Can be fully tested by adding a new task with title and description and verifying it appears in the task list.

### Implementation for User Story 1

- [x] T010 [P] [US1] Implement add_task() function with validation in src/todo.py
- [x] T011 [US1] Implement main menu loop with option 1 (Add task) in src/todo.py
- [x] T012 [US1] Add error handling for empty title in add_task() function
- [x] T013 [US1] Add auto-generation of unique IDs for new tasks

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Allow users to view all their tasks with their ID, title, description, and completion status

**Independent Test**: Can be fully tested by viewing the task list after adding tasks and verifying they display correctly with all required information.

### Implementation for User Story 2

- [x] T014 [P] [US2] Implement view_tasks() function with clean table-like format in src/todo.py
- [x] T015 [US2] Implement main menu option 2 (View tasks) in src/todo.py
- [x] T016 [US2] Add status indicators ([ ] for incomplete, [X] for complete) to view_tasks()
- [x] T017 [US2] Handle case of empty task list with appropriate message

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Allow users to update existing task details (title or description)

**Independent Test**: Can be fully tested by updating a task's title or description and verifying the changes are reflected when viewing the task.

### Implementation for User Story 3

- [x] T018 [P] [US3] Implement update_task() function in src/todo.py
- [x] T019 [US3] Implement main menu option 3 (Update task) in src/todo.py
- [x] T020 [US3] Add error handling for invalid task IDs in update_task()
- [x] T021 [US3] Add validation for updated task details

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Allow users to delete tasks by ID

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the task list.

### Implementation for User Story 4

- [x] T022 [P] [US4] Implement delete_task() function in src/todo.py
- [x] T023 [US4] Implement main menu option 4 (Delete task) in src/todo.py
- [x] T024 [US4] Add error handling for invalid task IDs in delete_task()
- [x] T025 [US4] Add confirmation prompt for task deletion (optional)

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Allow users to mark tasks as complete or incomplete so that they can track their progress

**Independent Test**: Can be fully tested by toggling a task's completion status and verifying the change is reflected when viewing the task.

### Implementation for User Story 5

- [x] T026 [P] [US5] Implement toggle_complete() function in src/todo.py
- [x] T027 [US5] Implement main menu option 5 (Toggle complete) in src/todo.py
- [x] T028 [US5] Add error handling for invalid task IDs in toggle_complete()
- [x] T029 [US5] Verify status change reflects in view_tasks()

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T030 [P] Add comprehensive error handling for all user inputs
- [x] T031 [P] Add type hints to all functions according to PEP 8
- [x] T032 [P] Ensure functions are short and focused (single responsibility)
- [x] T033 [P] Add comments to explain complex logic (minimal as per constitution)
- [x] T034 [P] Format code according to PEP 8 style guide
- [x] T035 [P] Verify code length remains under 300 lines
- [x] T036 [P] Update README.md with usage instructions
- [x] T037 [P] Test all 5 core features together for integration issues
- [x] T038 [P] Run quickstart validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with other stories but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all implementation tasks for User Story 1 together:
Task: "Implement add_task() function with validation in src/todo.py"
Task: "Implement main menu loop with option 1 (Add task) in src/todo.py"
Task: "Add error handling for empty title in add_task() function"
Task: "Add auto-generation of unique IDs for new tasks"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence