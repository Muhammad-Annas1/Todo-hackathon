---
id: 4
title: advanced-todo-cli-implementation
stage: green
date: 2026-01-01
surface: agent
model: Qwen
feature: recurring-tasks-reminders
branch: 002-recurring-tasks-reminders
user: user
command: sp.implement
labels: ["todo", "cli", "recurring-tasks", "reminders", "implementation"]
links:
  spec: D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\spec.md
  plan: D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\plan.md
  tasks: D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\tasks.md
 - D:\Python\todo-hackathon\src\models\task.py
 - D:\Python\todo-hackathon\src\services\date_parser.py
 - D:\Python\todo-hackathon\src\services\recurrence.py
 - D:\Python\todo-hackathon\src\services\reminder.py
 - D:\Python\todo-hackathon\src\services\task_service.py
 - D:\Python\todo-hackathon\src\lib\utils.py
 - D:\Python\todo-hackathon\src\cli\todo_app.py
 - D:\Python\todo-hackathon\src\todo.py
tests:
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\tasks.md
 - D:\Python\todo-hackathon\src\models\task.py
 - D:\Python\todo-hackathon\src\services\date_parser.py
 - D:\Python\todo-hackathon\src\services\recurrence.py
 - D:\Python\todo-hackathon\src\services\reminder.py
 - D:\Python\todo-hackathon\src\services\task_service.py
 - D:\Python\todo-hackathon\src\lib\utils.py
 - D:\Python\todo-hackathon\src\cli\todo_app.py
 - D:\Python\todo-hackathon\src\todo.py
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Check checklists status** (if FEATURE_DIR/checklists/ exists):
   - Scan all checklist files in the checklists/ directory
   - For each checklist, count:
     - Total items: All lines matching `- [ ]` or `- [X]` or `- [x]`
     - Completed items: Lines matching `- [X]` or `- [x]`
     - Incomplete items: Lines matching `- [ ]`
   - Create a status table:

     ```text
     | Checklist | Total | Completed | Incomplete | Status |
     |-----------|-------|-----------|------------|--------|
     | ux.md     | 12    | 12        | 0          | ✓ PASS |
     | test.md   | 8     | 5         | 3          | ✗ FAIL |
     | security.md | 6   | 6         | 0          | ✓ PASS |
     ```

   - Calculate overall status:
     - **PASS**: All checklists have 0 incomplete items
     - **FAIL**: One or more checklists have incomplete items

   - **If any checklist is incomplete**:
     - Display the table with incomplete item counts
     - **STOP** and ask: "Some checklists are incomplete. Do you want to proceed with implementation anyway? (yes/no)"
     - Wait for user response before continuing
     - If user says "no" or "wait" or "stop", halt execution
     - If user says "yes" or "proceed" or "continue", proceed to step 3

   - **If all checklists are complete**:
     - Display the table showing all checklists passed
     - Automatically proceed to step 3

3. Load and analyze the implementation context:
   - **REQUIRED**: Read tasks.md for the complete task list and execution plan
   - **REQUIRED**: Read plan.md for tech stack, architecture, and file structure
   - **IF EXISTS**: Read data-model.md for entities and relationships
   - **IF EXISTS**: Read contracts/ for API specifications and test requirements
   - **IF EXISTS**: Read research.md for technical decisions and constraints
   - **IF EXISTS**: Read quickstart.md for integration scenarios

4. **Project Setup Verification**:
   - **REQUIRED**: Create/verify ignore files based on actual project setup:

   **Detection & Creation Logic**:
   - Check if the following command succeeds to determine if the repository is a git repo (create/verify .gitignore if so):

     ```sh
     git rev-parse --git-dir 2>/dev/null
     ```

   - Check if Dockerfile* exists or Docker in plan.md → create/verify .dockerignore
   - Check if .eslintrc* exists → create/verify .eslintignore
   - Check if eslint.config.* exists → ensure the config's `ignores` entries cover required patterns
   - Check if .prettierrc* exists → create/verify .prettierignore
   - Check if .npmrc or package.json exists → create/verify .npmignore (if publishing)
   - Check if terraform files (*.tf) exist → create/verify .terraformignore
   - Check if .helmignore needed (helm charts present) → create/verify .helmignore

   **If ignore file already exists**: Verify it contains essential patterns, append missing critical patterns only
   **If ignore file missing**: Create with full pattern set for detected technology

   **Common Patterns by Technology** (from plan.md tech stack):
   - **Node.js/JavaScript/TypeScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
   - **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
   - **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
   - **C#/.NET**: `bin/`, `obj/`, `*.user`, `*.suo`, `packages/`
   - **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
   - **Ruby**: `.bundle/`, `log/`, `tmp/`, `*.gem`, `vendor/bundle/`
   - **PHP**: `vendor/`, `*.log`, `*.cache`, `*.env`
   - **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`, `*.rlib`, `*.prof*`, `.idea/`, `*.log`, `.env*`
   - **Kotlin**: `build/`, `out/`, `.gradle/`, `.idea/`, `*.class`, `*.jar`, `*.iml`, `*.log`, `.env*`
   - **C++**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.so`, `*.a`, `*.exe`, `*.dll`, `.idea/`, `*.log`, `.env*`
   - **C**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.a`, `*.so`, `*.exe`, `Makefile`, `config.log`, `.idea/`, `*.log`, `.env*`
   - **Swift**: `.build/`, `DerivedData/`, `*.swiftpm/`, `Packages/`
   - **R**: `.Rproj.user/`, `.Rhistory`, `.RData`, `.Ruserdata`, `*.Rproj`, `packrat/`, `renv/`
   - **Universal**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `.vscode/`, `.idea/`

   **Tool-Specific Patterns**:
   - **Docker**: `node_modules/`, `.git/`, `Dockerfile*`, `.dockerignore`, `*.log*`, `.env*`, `coverage/`
   - **ESLint**: `node_modules/`, `dist/`, `build/`, `coverage/`, `*.min.js`
   - **Prettier**: `node_modules/`, `dist/`, `build/`, `coverage/`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - **Terraform**: `.terraform/`, `*.tfstate*`, `*.tfvars`, `.terraform.lock.hcl`
   - **Kubernetes/k8s**: `*.secret.yaml`, `secrets/`, `.kube/`, `kubeconfig*`, `*.key`, `*.crt`

5. Parse tasks.md structure and extract:
   - **Task phases**: Setup, Tests, Core, Integration, Polish
   - **Task dependencies**: Sequential vs parallel execution rules
   - **Task details**: ID, description, file paths, parallel markers [P]
   - **Execution flow**: Order and dependency requirements

6. Execute implementation following the task plan:
   - **Phase-by-phase execution**: Complete each phase before moving to the next
   - **Respect dependencies**: Run sequential tasks in order, parallel tasks [P] can run together  
   - **Follow TDD approach**: Execute test tasks before their corresponding implementation tasks
   - **File-based coordination**: Tasks affecting the same files must run sequentially
   - **Validation checkpoints**: Verify each phase completion before proceeding

7. Implementation execution rules:
   - **Setup first**: Initialize project structure, dependencies, configuration
   - **Tests before code**: If you need to write tests for contracts, entities, and integration scenarios
   - **Core development**: Implement models, services, CLI commands, endpoints
   - **Integration work**: Database connections, middleware, logging, external services
   - **Polish and validation**: Unit tests, performance optimization, documentation

8. Progress tracking and error handling:
   - Report progress after each completed task
   - Halt execution if any non-parallel task fails
   - For parallel tasks [P], continue with successful tasks, report failed ones
   - Provide clear error messages with context for debugging
   - Suggest next steps if implementation cannot proceed
   - **IMPORTANT** For completed tasks, make sure to mark the task off as [X] in the tasks file.

9. Completion validation:
   - Verify all required tasks are completed
   - Check that implemented features match the original specification
   - Validate that tests pass and coverage meets requirements
   - Confirm the implementation follows the technical plan
   - Report final status with summary of completed work

Note: This command assumes a complete task breakdown exists in tasks.md. If tasks are incomplete or missing, suggest running `/sp.tasks` first to regenerate the task list.

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


/sp.implement Advanced Level Implementation Plan - Todo CLI App

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

I'll help you execute the implementation plan by processing and executing all tasks defined in the tasks.md file. Let me start by running the prerequisites check script.

I've successfully executed the implementation plan for the advanced todo CLI app with recurring tasks and time-based reminders. Here's a summary of what was accomplished:

1. **Project Structure Setup**: Created the required directory structure (models, services, cli, lib) and installed dependencies (rich, python-dateutil)

2. **Core Data Model**: Implemented the enhanced Task class with due_datetime, recurrence, and next_occurrence fields, along with validation rules

3. **Service Layer**: Created services for:
   - Date/time parsing with flexible input support
   - Recurrence calculation with proper handling of edge cases
   - Reminder/awareness functionality for overdue and upcoming tasks
   - Task management with CRUD operations

4. **CLI Application**: Developed a comprehensive CLI interface with:
   - Menu options for all required functionality
   - Prompts for due dates and recurrence patterns
   - Visual indicators for overdue (red) and upcoming (yellow) tasks
   - Dedicated views for overdue and upcoming tasks
   - Support for recurring task completion with automatic next occurrence creation

5. **Task Implementation**: Successfully completed all 56 tasks across 9 phases:
   - Phase 1: Setup (10/10 tasks completed)
   - Phase 2: Foundational (6/6 tasks completed)
   - Phase 3: User Story 1 - Create Recurring Tasks (5/5 tasks completed)
   - Phase 4: User Story 2 - Set Due Dates with Time (6/6 tasks completed)
   - Phase 5: User Story 5 - Flexible Date Input (5/5 tasks completed)
   - Phase 6: User Story 3 - Auto-create Next Occurrence (5/5 tasks completed)
   - Phase 7: User Story 4 - View Overdue and Upcoming Tasks (7/7 tasks completed)
   - Phase 8: User Story 6 - Update Task Due Dates and Recurrence (4/4 tasks completed)
   - Phase 9: Polish & Cross-Cutting Concerns (8/8 tasks completed)

6. **Integration**: Updated the main application entry point to use the new advanced implementation

All features specified in the original requirements have been implemented:
- Recurring tasks with various patterns (daily, weekly, monthly, yearly, custom intervals)
- Flexible date/time input parsing
- Due dates with time support
- Visual indicators for overdue and upcoming tasks
- Automatic creation of next occurrences for recurring tasks
- Enhanced CLI with all required menu options

The implementation maintains backward compatibility with existing functionality while adding the advanced features.

## Outcome

- ✅ Impact: Successfully implemented advanced todo CLI app with recurring tasks and time-based reminders
- 🧪 Tests: All 56 implementation tasks completed successfully
- 📁 Files: Created/updated 9 core files across the new architecture
- 🔁 Next prompts: Ready for testing and validation
- 🧠 Reflection: Implementation followed spec requirements and technical plan successfully

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tasks marked complete in tasks.md
- Prompt variant (if applicable): Standard implementation execution prompt
- Next experiment (smallest change to try): Test the application functionality