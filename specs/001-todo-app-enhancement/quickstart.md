# Quickstart Guide: Todo CLI App Enhancement

**Feature**: Todo CLI App Enhancement
**Date**: 2025-01-01
**Branch**: 001-todo-app-enhancement

## Overview

This guide provides instructions for setting up and using the enhanced Todo CLI application with priority, tags, due dates, search, filter, and sort functionality.

## Prerequisites

- Python 3.13 or higher
- (Optional) Rich library for enhanced formatting: `pip install rich`

## Setup

1. Clone or navigate to the project directory
2. Ensure Python 3.13+ is installed
3. (Optional) Install rich for better formatting:
   ```bash
   pip install rich
   ```

## Running the Application

```bash
cd src
python todo.py
```

## New Features Overview

### 1. Priority Levels
- Tasks can have priority: high (!!!), medium (!!)), or low (!)
- Default priority is "medium"
- Priority is displayed with visual indicators

### 2. Tags
- Tasks can have multiple tags
- Tags are separated by spaces or commas
- Tags help categorize and organize tasks

### 3. Due Dates
- Tasks can have due dates in YYYY-MM-DD format
- Natural language input supported: "tomorrow", "next friday", "in 3 days"
- Due dates are displayed in the task list

### 4. Search
- Search across task titles, descriptions, and tags
- Case-insensitive search
- Access via main menu option

### 5. Filter
- Filter tasks by status (all, pending, completed)
- Filter by priority (all, high, medium, low)
- Filter by specific tags
- Combined filtering possible

### 6. Sort
- Sort by priority (high to low)
- Sort by due date (earliest first)
- Sort by title (alphabetically)
- Default sort is by creation order

## Usage Examples

### Adding a Task with New Features
```
1. Add new task
Title: Complete project proposal
Description: Write and review the project proposal document
Priority [high/medium/low] (default: medium): high
Tags (space/comma separated): work project urgent
Due date (YYYY-MM-DD or natural language): next friday
```

### Searching Tasks
```
6. Search tasks
Enter search keyword: project
```

### Filtering Tasks
```
7. Filter tasks
Filter by status [all/pending/completed] (default: all): pending
Filter by priority [all/high/medium/low] (default: all): high
Filter by tag (optional): project
```

### Sorting Tasks
```
8. Sort tasks
Sort by [priority/due_date/title/id] (default: id): due_date
Order [asc/desc] (default: asc): asc
```

## Menu Options

The main menu now includes:
1. Add new task
2. View all tasks
3. Update existing task
4. Delete task
5. Toggle task completion
6. Search tasks
7. Filter tasks
8. Sort tasks
0. Quit

## Development

### Code Structure
- Main application: `src/todo.py`
- Task model: Within `todo.py` (in-memory implementation)
- All functionality contained in a single file for simplicity

### Key Functions
- `add_task()`: Enhanced to support new fields
- `view_tasks()`: Enhanced to display new information
- `search_tasks()`: New function for keyword search
- `filter_tasks()`: New function for filtering
- `sort_tasks()`: New function for sorting
- `parse_date()`: New function for date parsing

### Testing the Features
1. Add tasks with various priorities, tags, and due dates
2. Verify display of new information in the task list
3. Test search functionality with keywords from title, description, and tags
4. Test filtering with different criteria
5. Test sorting with different fields and orders
6. Verify backward compatibility with existing functionality