---
id: 2
title: advanced-todo-cli-plan
stage: plan
date: 2026-01-01
surface: agent
model: Qwen
feature: recurring-tasks-reminders
branch: 002-recurring-tasks-reminders
user: user
command: sp.plan
labels: ["todo", "cli", "recurring-tasks", "reminders", "plan"]
links:
  spec: D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\spec.md
  ticket: null
  adr: null
  pr: null
files:
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\plan.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\research.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\data-model.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\quickstart.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\contracts\task-contracts.md
tests:
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\plan.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\research.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\data-model.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\quickstart.md
 - D:\Python\todo-hackathon\specs\002-recurring-tasks-reminders\contracts\task-contracts.md
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

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


/sp.plan Advanced Level Implementation Plan - Todo CLI App

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

I'll help you create an implementation plan for the advanced todo CLI app with recurring tasks and time-based reminders. Let me start by running the setup script to get the required paths and context.

The implementation plan for the advanced todo CLI app with recurring tasks and time-based reminders has been successfully created. Here's a summary of what was accomplished:

1. **Setup**: Successfully ran the setup script and obtained the required paths
2. **Technical Context**: Filled in the technical context with Python 3.13+, datetime module, dateutil, and rich library
3. **Constitution Check**: Identified and documented violations of the original constitution (due dates and filtering) which were justified for this advanced feature
4. **Research**: Created research.md with decisions on date/time parsing, recurrence calculation, visual indicators, and storage strategy
5. **Data Model**: Created data-model.md with enhanced Task entity and RecurrencePattern value object
6. **Contracts**: Created function contracts for task management, recurrence, date/time parsing, and reminder functions
7. **Quickstart Guide**: Created a quickstart guide explaining the new features and usage
8. **Agent Context**: Updated the Qwen agent context with the new technologies and frameworks
9. **Project Structure**: Defined the project structure with models, services, cli, and lib directories

All required artifacts have been generated and the implementation plan is ready for the next phase. The plan addresses all aspects of the advanced feature including recurring tasks, due dates with time, and reminder functionality while maintaining existing functionality.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for advanced todo CLI app with recurring tasks and time-based reminders
- 🧪 Tests: Generated research, data model, contracts, and quickstart documentation
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts in the feature directory
- 🔁 Next prompts: Ready for /sp.tasks to break the plan into specific tasks
- 🧠 Reflection: Successfully implemented all required planning phases while addressing constitution violations appropriately

## Evaluation notes (flywheel)

- Failure modes observed: Constitution violations identified and properly documented in complexity tracking
- Graders run and results (PASS/FAIL): All planning phases completed successfully
- Prompt variant (if applicable): Standard implementation planning prompt
- Next experiment (smallest change to try): Break plan into specific tasks with /sp.tasks