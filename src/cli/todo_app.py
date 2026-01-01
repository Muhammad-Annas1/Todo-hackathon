"""
Main CLI application with enhanced menu
"""
from datetime import datetime
import sys
from rich.console import Console
from rich.table import Table
from rich.text import Text

from services.task_service import TaskManager
from services.date_parser import parse_flexible_date
from services.reminder import get_overdue_tasks, get_upcoming_tasks
from lib.utils import format_datetime_for_display, format_relative_time


class TodoApp:
    """
    Main CLI application for the advanced todo app with recurring tasks
    and time-based reminders.
    """
    
    def __init__(self):
        self.task_manager = TaskManager()
        self.console = Console()
    
    def run(self):
        """
        Main application loop - runs until user chooses to quit.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.toggle_task_completion()
            elif choice == "6":
                self.view_overdue_tasks()
            elif choice == "7":
                self.view_upcoming_tasks()
            elif choice == "0":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
    
    def display_menu(self):
        """
        Display the main menu options.
        """
        self.console.print("\n[bold blue]Advanced Todo CLI App[/bold blue]")
        self.console.print("1. Add new task - With prompts for due date/time and recurrence")
        self.console.print("2. View all tasks - Enhanced with due dates and recurrence indicators")
        self.console.print("3. Update existing task - With options to change due date/time and recurrence")
        self.console.print("4. Delete task")
        self.console.print("5. Mark task as complete/incomplete")
        self.console.print("6. Show overdue tasks - Dedicated view for overdue items")
        self.console.print("7. Show upcoming tasks - Dedicated view for upcoming items")
        self.console.print("0. Quit")
    
    def add_task(self):
        """
        Add a new task with prompts for due date/time and recurrence.
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            return
        
        description = input("Enter task description (optional): ").strip()
        
        # Prompt for due date/time
        due_date_input = input("Enter due date/time (optional, e.g., 'tomorrow 3pm', '2026-01-15 14:30'): ").strip()
        due_datetime = None
        if due_date_input:
            due_datetime = parse_flexible_date(due_date_input)
            if due_datetime is None:
                print(f"Could not parse the date/time: {due_date_input}")
                return
        
        # Prompt for recurrence
        recurrence = input("Enter recurrence pattern (optional, e.g., 'daily', 'weekly', 'monthly', 'every 3 days'): ").strip()
        if recurrence:
            from src.services.recurrence import validate_recurrence_pattern
            if not validate_recurrence_pattern(recurrence):
                print(f"Invalid recurrence pattern: {recurrence}")
                return
        
        # Add the task
        task = self.task_manager.add_task(title, description, due_datetime, recurrence)
        print(f"Task '{task.title}' added successfully with ID {task.id}")
    
    def view_all_tasks(self):
        """
        View all tasks with enhanced display showing due dates and recurrence indicators.
        """
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("\nNo tasks found.")
            return
        
        table = Table(title="All Tasks")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Title", min_width=15)
        table.add_column("Description", min_width=20)
        table.add_column("Status", width=10)
        table.add_column("Due", min_width=15)
        table.add_column("Recurrence", min_width=12)
        
        for task in tasks:
            status = "[green]✓ Completed[/green]" if task.completed else "[red]○ Pending[/red]"
            
            # Format due date with visual indicators
            if task.due_datetime:
                relative_time = format_relative_time(task.due_datetime)
                if task.is_overdue():
                    due_text = f"[red]{relative_time}[/red]"
                elif task.is_upcoming():
                    due_text = f"[yellow]{relative_time}[/yellow]"
                else:
                    due_text = relative_time
            else:
                due_text = "—"
            
            # Format recurrence with indicator
            recurrence_text = task.recurrence if task.recurrence else "—"
            if task.recurrence:
                recurrence_text = f"↻ {recurrence_text}"
            
            table.add_row(
                str(task.id),
                task.title,
                task.description,
                status,
                due_text,
                recurrence_text
            )
        
        self.console.print(table)
    
    def update_task(self):
        """
        Update an existing task with options to change due date/time and recurrence.
        """
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        
        print(f"\nUpdating task: {task.title}")
        
        # Get new values (or keep existing if empty input)
        new_title = input(f"Enter new title (current: '{task.title}'): ").strip()
        if not new_title:
            new_title = task.title
        
        new_description = input(f"Enter new description (current: '{task.description}'): ").strip()
        if not new_description:
            new_description = task.description
        
        # Handle due date update
        current_due = format_datetime_for_display(task.due_datetime) if task.due_datetime else "None"
        due_input = input(f"Enter new due date/time (current: '{current_due}', blank to keep): ").strip()
        new_due_datetime = task.due_datetime  # Default to current
        if due_input:
            if due_input.lower() in ['none', 'null', 'clear']:
                new_due_datetime = None
            else:
                parsed_date = parse_flexible_date(due_input)
                if parsed_date is None:
                    print(f"Could not parse the date/time: {due_input}")
                    return
                new_due_datetime = parsed_date
        
        # Handle recurrence update
        current_recurrence = task.recurrence if task.recurrence else "None"
        recurrence_input = input(f"Enter new recurrence pattern (current: '{current_recurrence}', blank to keep): ").strip()
        new_recurrence = task.recurrence  # Default to current
        if recurrence_input:
            if recurrence_input.lower() in ['none', 'null', 'clear']:
                new_recurrence = None
            else:
                from src.services.recurrence import validate_recurrence_pattern
                if not validate_recurrence_pattern(recurrence_input):
                    print(f"Invalid recurrence pattern: {recurrence_input}")
                    return
                new_recurrence = recurrence_input
        
        # Update the task
        success = self.task_manager.update_task(
            task_id, new_title, new_description, 
            new_due_datetime, new_recurrence
        )
        
        if success:
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Failed to update task {task_id}.")
    
    def delete_task(self):
        """
        Delete a task by ID.
        """
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        success = self.task_manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Failed to delete task {task_id}. Task may not exist.")
    
    def toggle_task_completion(self):
        """
        Toggle task completion status.
        """
        try:
            task_id = int(input("Enter task ID to toggle: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        success = self.task_manager.toggle_task_completion(task_id)
        if success:
            task = self.task_manager.get_task(task_id)
            status = "completed" if task.completed else "pending"
            print(f"Task {task_id} marked as {status}.")
            
            # If it was a recurring task that was just completed, inform the user
            if task.completed and task.is_recurring():
                print("Note: A new occurrence of this recurring task has been created.")
        else:
            print(f"Failed to toggle task {task_id}. Task may not exist.")
    
    def view_overdue_tasks(self):
        """
        Display all overdue tasks with special highlighting.
        """
        all_tasks = self.task_manager.get_all_tasks()
        overdue_tasks = get_overdue_tasks(all_tasks)
        
        if not overdue_tasks:
            print("\nNo overdue tasks.")
            return
        
        table = Table(title="Overdue Tasks")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Title", min_width=15)
        table.add_column("Due", min_width=15)
        table.add_column("Recurrence", min_width=12)
        
        for task in overdue_tasks:
            relative_time = format_relative_time(task.due_datetime)
            recurrence_text = f"↻ {task.recurrence}" if task.recurrence else "—"
            
            table.add_row(
                str(task.id),
                task.title,
                f"[red]{relative_time}[/red]",
                recurrence_text
            )
        
        self.console.print(table)
    
    def view_upcoming_tasks(self):
        """
        Display all tasks due within 24 hours with special highlighting.
        """
        try:
            hours = int(input("Enter number of hours to look ahead (default 24): ") or "24")
        except ValueError:
            hours = 24
        
        all_tasks = self.task_manager.get_all_tasks()
        upcoming_tasks = get_upcoming_tasks(all_tasks, hours)
        
        if not upcoming_tasks:
            print(f"\nNo tasks due within the next {hours} hours.")
            return
        
        table = Table(title=f"Upcoming Tasks (Next {hours} Hours)")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Title", min_width=15)
        table.add_column("Due", min_width=15)
        table.add_column("Recurrence", min_width=12)
        
        for task in upcoming_tasks:
            relative_time = format_relative_time(task.due_datetime)
            recurrence_text = f"↻ {task.recurrence}" if task.recurrence else "—"
            
            table.add_row(
                str(task.id),
                task.title,
                f"[yellow]{relative_time}[/yellow]",
                recurrence_text
            )
        
        self.console.print(table)


def main():
    """
    Main entry point for the application.
    """
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()