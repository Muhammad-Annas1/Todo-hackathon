---

description: "Task list for Todo CLI App Enhancement implementation"
---

# Tasks: Todo CLI App Enhancement

**Input**: Design documents from `/specs/001-todo-app-enhancement/`
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

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Verify Python 3.13+ installation and environment
- [X] T003 [P] Check if rich library is available for enhanced formatting

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Update existing Task model in src/todo.py to include new fields (priority, tags, due_date)
- [X] T005 [P] Implement date parsing function for natural language dates in src/todo.py
- [X] T006 [P] Create validation functions for priority, tags, and due dates in src/todo.py
- [X] T007 Update existing TodoManager class to handle new fields in src/todo.py
- [X] T008 Update existing view_tasks function to display new information in src/todo.py
- [X] T009 Update existing add_task function to accept new parameters in src/todo.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Priority to Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to assign priority levels (high, medium, low) to tasks and display them with visual indicators

**Independent Test**: Can be fully tested by creating tasks with different priority levels and verifying they are displayed with appropriate indicators, delivering immediate value in task prioritization.

### Implementation for User Story 1

- [X] T010 [P] [US1] Update Task model to include priority field with default 'medium' in src/todo.py
- [X] T011 [US1] Update add_task function to accept priority parameter in src/todo.py
- [X] T012 [US1] Update update_task function to modify priority in src/todo.py
- [X] T013 [US1] Update view_tasks function to display priority with visual indicators (!!!/!!/!) in src/todo.py
- [X] T014 [US1] Add priority validation to ensure only 'high', 'medium', 'low' values in src/todo.py
- [X] T015 [US1] Update main menu to reflect enhanced task display in src/todo.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Add Tags to Tasks (Priority: P1)

**Goal**: Enable users to assign multiple tags to tasks for categorization and organization

**Independent Test**: Can be fully tested by creating tasks with multiple tags and verifying they are saved and displayed correctly, delivering value in task categorization.

### Implementation for User Story 2

- [X] T016 [P] [US2] Update Task model to include tags field as list[str] in src/todo.py
- [X] T017 [US2] Update add_task function to accept tags parameter in src/todo.py
- [X] T018 [US2] Update update_task function to modify tags in src/todo.py
- [X] T019 [US2] Update view_tasks function to display tags in src/todo.py
- [X] T020 [US2] Add tag validation to ensure proper format (alphanumeric, hyphens, underscores) in src/todo.py
- [X] T021 [US2] Implement tag parsing from user input (space/comma separated) in src/todo.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Set Due Dates for Tasks (Priority: P1)

**Goal**: Enable users to set due dates for tasks using flexible input methods (YYYY-MM-DD or natural language)

**Independent Test**: Can be fully tested by creating tasks with due dates and verifying they are saved and displayed correctly, delivering value in deadline tracking.

### Implementation for User Story 3

- [X] T022 [P] [US3] Update Task model to include due_date field in src/todo.py
- [X] T023 [US3] Update add_task function to accept due_date parameter in src/todo.py
- [X] T024 [US3] Update update_task function to modify due_date in src/todo.py
- [X] T025 [US3] Update view_tasks function to display due dates in src/todo.py
- [X] T026 [US3] Enhance date parsing function to handle natural language inputs in src/todo.py
- [X] T027 [US3] Add due date validation to ensure proper format in src/todo.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Search Tasks (Priority: P2)

**Goal**: Enable users to search through tasks by keywords in title, description, and tags

**Independent Test**: Can be fully tested by creating tasks with various content and searching for keywords, delivering value in task discovery.

### Implementation for User Story 4

- [X] T028 [US4] Implement search_tasks function in src/todo.py
- [X] T029 [US4] Add search functionality to search across title, description, and tags in src/todo.py
- [X] T030 [US4] Implement case-insensitive search in src/todo.py
- [X] T031 [US4] Add search option to main menu in src/todo.py
- [X] T032 [US4] Create search UI with input prompt in src/todo.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Filter Tasks (Priority: P2)

**Goal**: Enable users to filter tasks by status, priority, or tag

**Independent Test**: Can be fully tested by applying different filters and verifying the correct tasks are displayed, delivering value in task organization.

### Implementation for User Story 5

- [X] T033 [US5] Implement filter_tasks function in src/todo.py
- [X] T034 [US5] Add filtering by status (all, pending, completed) in src/todo.py
- [X] T035 [US5] Add filtering by priority (all, high, medium, low) in src/todo.py
- [X] T036 [US5] Add filtering by specific tag in src/todo.py
- [X] T037 [US5] Add filter option to main menu in src/todo.py
- [X] T038 [US5] Create filter UI with input prompts in src/todo.py

**Checkpoint**: At this point, User Stories 1-5 should all work independently

---

## Phase 8: User Story 6 - Sort Tasks (Priority: P3)

**Goal**: Enable users to sort tasks by priority, due date, or title

**Independent Test**: Can be fully tested by applying different sorting options and verifying tasks are displayed in the correct order, delivering value in task organization.

### Implementation for User Story 6

- [X] T039 [US6] Implement sort_tasks function in src/todo.py
- [X] T040 [US6] Add sorting by priority (high to low) in src/todo.py
- [X] T041 [US6] Add sorting by due date (earliest first) in src/todo.py
- [X] T042 [US6] Add sorting by title (alphabetically A-Z) in src/todo.py
- [X] T043 [US6] Add sort option to main menu in src/todo.py
- [X] T044 [US6] Create sort UI with input prompts in src/todo.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T045 [P] Update README with new features and usage examples
- [X] T046 [P] Add error handling for edge cases (invalid dates, etc.) in src/todo.py
- [X] T047 [P] Add type hints to all new functions in src/todo.py
- [X] T048 [P] Code cleanup and refactoring of new functionality in src/todo.py
- [X] T049 [P] Performance optimization for search/filter/sort with large task lists
- [X] T050 Run quickstart.md validation to ensure all features work as expected

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
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/2/3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/2/3 but should be independently testable
- **User Story 6 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/2/3/4/5 but should be independently testable

### Within Each User Story

- Core implementation before UI integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Update Task model to include priority field with default 'medium' in src/todo.py"
Task: "Update add_task function to accept priority parameter in src/todo.py"
Task: "Update update_task function to modify priority in src/todo.py"
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
7. Add User Story 6 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
   - Developer F: User Story 6
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence