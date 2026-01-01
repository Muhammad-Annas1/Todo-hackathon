---
id: 3
title: advanced-todo-cli-tasks
stage: tasks
date: 2026-01-01
surface: agent
model: Qwen
feature: recurring-tasks-reminders
branch: 002-recurring-tasks-reminders
user: user
command: sp.tasks
labels: ["todo", "cli", "recurring-tasks", "reminders", "tasks"]
links:
  spec: D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\spec.md
  plan: D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\plan.md
  ticket: null
  adr: null
  pr: null
files:
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\tasks.md
tests:
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\tasks.md
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: 

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

**Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **[Story] label**: REQUIRED for user story phase tasks only
   - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
   - Setup phase: NO story label
   - Foundational phase: NO story label  
   - User Story phases: MUST have story label
   - Polish phase: NO story label
5. **Description**: Clear action with exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create model` (missing Task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

### Task Organization

1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
   - Each user story (P1, P2, P3...) gets its own phase
   - Map all related components to their story:
     - Models needed for that story
     - Services needed for that story
     - Endpoints/UI needed for that story
     - If tests requested: Tests specific to that story
   - Mark story dependencies (most stories should be independent)

2. **From Contracts**:
   - Map each contract/endpoint → to the user story it serves
   - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

3. **From Data Model**:
   - Map each entity to the user story(ies) that need it
   - If entity serves multiple stories: Put in earliest story or Setup phase
   - Relationships → service layer tasks in appropriate story phase

4. **From Setup/Infrastructure**:
   - Shared infrastructure → Setup phase (Phase 1)
   - Foundational/blocking tasks → Foundational phase (Phase 2)
   - Story-specific setup → within that story's phase

### Phase Structure

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
- **Phase 3+**: User Stories in priority order (P1, P2, P3...)
  - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
  - Each phase should be a complete, independently testable increment
- **Final Phase**: Polish & Cross-Cutting Concerns

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.tasks Advanced Level Implementation Plan - Todo CLI App

Project: Todo
Level: Advanced (Intelligent Features)
Builds on: Basic + Intermediate (same codebase)
Estimated effort: 8–16 hours (due to date/time logic complexity)

Goal: Add recurring tasks + full datetime support with in-app reminders/awareness

Recommended Implementation Order:

1. Update Data Model (1–2h)
   - Add to Task:
     - due_datetime: datetime.datetime | None
     - recurrence: str | None          # e.g. "daily", "weekly", "every 2 weeks", "monthly"
   - Optional helper field: original_due (for recurrence calculation)

2. Natural Date/Time Input Parser (2–4h) – most time-consuming part
   - Accept flexible inputs: "tomorrow 3pm", "next monday 9", "in 2 hours", "2026-01-15 14:30"
   - Use dateutil.parser.parse() if allowed (recommended)
   - Fallback: simple manual parsing for common patterns
   - Add during Add/Update task flow

3. Recurring Task Logic (2–3h)
   - When toggle complete on recurring task:
     - Calculate next due date based on recurrence pattern
     - Create new task copy with updated due_datetime
     - Mark current as complete (keep original for history)
   - Add helper functions:
     - calculate_next_date(current_date, recurrence_str)

4. Enhance View List (1–2h)
   - New columns: Due (relative time, e.g. "in 3h", "overdue 2d", "—")
   - Recurrence indicator (e.g. "↻ weekly")
   - Highlight:
     - Overdue → bold/red
     - Soon (next 24h) → yellow/italic

5. In-App Awareness / Reminders (1.5–2h)
   - On every view/list: auto-show:
     - Overdue section
     - Upcoming (next 24h/7d) section
   - Optional stretch: simple beep or console flash for overdue (thread/timer)

6. Menu & Flow Updates (1h)
   - Add task: ask due date/time + recurrence (optional)
   - Update task: allow changing due + recurrence
   - Optional new menu items:
     - 9. Show Overdue
     - 10. Show Upcoming

7. Testing & Polish (1–2h)
   - Test cases:
     - Create daily task → complete → next day appears
     - Set "next monday 9am" → correct datetime
     - Overdue tasks highlighted
   - Error handling for invalid date inputs
   - Update README: new advanced features + examples

Constraints & Notes:
- Still purely in-memory
- Dependencies: dateutil strongly recommended (if not, implement simple parser)
- rich library almost mandatory now for colors/highlights
- Keep main loop non-blocking

Success Checklist:
☐ Recurring tasks auto-reschedule correctly
☐ Flexible date/time input works for common cases
☐ Overdue & upcoming tasks visually highlighted
☐ All previous features still work
☐ No major slowdown with 50+ tasks

## Response snapshot

I'll help you generate an actionable, dependency-ordered tasks.md for the advanced todo CLI app with recurring tasks and time-based reminders. Let me start by running the prerequisites check script.

I've successfully generated the tasks.md file for the advanced todo CLI app with recurring tasks and time-based reminders. The tasks are organized by user story in priority order, following the required checklist format with proper IDs, labels, and file paths. The implementation strategy follows an incremental approach starting with core functionality.

The generated tasks.md file includes:

1. Setup phase (T001-T010): Project structure and dependencies
2. Foundational phase (T011-T016): Core data model and services
3. User Story phases in priority order:
   - US1: Create Recurring Tasks (T017-T021)
   - US2: Set Due Dates with Time (T022-T027)
   - US5: Flexible Date Input (T028-T032)
   - US3: Auto-create Next Occurrence (T033-T037)
   - US4: View Overdue and Upcoming Tasks (T038-T044)
   - US6: Update Task Due Dates and Recurrence (T045-T048)
4. Final phase: Polish & Cross-Cutting Concerns (T049-T056)

The file includes dependency information, parallel execution examples, and independent test criteria for each user story. All tasks follow the required format with checkboxes, sequential IDs, and appropriate labels.

## Outcome

- ✅ Impact: Created comprehensive task breakdown for advanced todo CLI app with recurring tasks and time-based reminders
- 🧪 Tests: Generated 56 specific tasks organized by user story priority
- 📁 Files: Created tasks.md in the feature directory with proper structure
- 🔁 Next prompts: Ready for implementation phase
- 🧠 Reflection: Successfully organized tasks by user story with proper dependencies and parallel execution opportunities

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tasks follow required format
- Prompt variant (if applicable): Standard task breakdown prompt
- Next experiment (smallest change to try): Begin implementation with Phase 1 tasks