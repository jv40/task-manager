"""
#During Sprint 2, the add_task file was expanded to include an optional validated due_date, and every new task is created with a completion_date. 
#This fixed the fact that Sprint 1 had an inconsistent JSON structure for add_tasks. view_tasks.py was improved to sort tasks by priority, show or hide completed tasks with a --show-completed flag, and display the new due-date and completion-date fields. complete_task.py was updated so finishing a task now records a timestamp and supports
# undoing completion. export_tasks.py was added, providing CSV/TXT export and filters for completed or pending tasks. 
