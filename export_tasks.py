import json
import os
import sys
from datetime import datetime

DATA_FILE = "data.json"

PRIORITY_ORDER = {
    "high": 1,
    "medium": 2,
    "low": 3
}


def load_data():
    """Load tasks from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": []}


def export_to_csv(tasks, filename="tasks_export.csv"):
    """Write tasks to a CSV file."""
    with open(filename, "w") as f:
        f.write("id,description,priority,completed,due_date,completion_date\n")
        for t in tasks:
            f.write(f"{t['id']},"
                    f"\"{t['description']}\","
                    f"{t['priority']},"
                    f"{t['completed']},"
                    f"{t.get('due_date','')},"
                    f"{t.get('completion_date','')}\n")
    print(f"Export complete! File saved as {filename}")


def export_to_txt(tasks, filename="tasks_export.txt"):
    """Write tasks to a TXT file."""
    with open(filename, "w") as f:
        for t in tasks:
            f.write(f"ID: {t['id']}\n")
            f.write(f"Description: {t['description']}\n")
            f.write(f"Priority: {t['priority']}\n")
            f.write(f"Completed: {t['completed']}\n")
            f.write(f"Due Date: {t.get('due_date','None')}\n")
            f.write(f"Completion Date: {t.get('completion_date','None')}\n")
            f.write("-" * 40 + "\n")
    print(f"Export complete! File saved as {filename}")


def export_tasks():
    args = sys.argv[1:]

    data = load_data()
    tasks = data.get("tasks", [])

    # Filter flags
    completed_only = "--completed-only" in args
    pending_only = "--pending-only" in args
    export_txt = "--txt" in args

    if completed_only and pending_only:
        print("Error: Cannot use --completed-only and --pending-only together.")
        return

    if completed_only:
        tasks = [t for t in tasks if t.get("completed")]
    elif pending_only:
        tasks = [t for t in tasks if not t.get("completed")]

    # Sort tasks by priority for consistent output
    tasks.sort(key=lambda t: PRIORITY_ORDER.get(t["priority"], 99))

    if not tasks:
        print("No tasks match the selected filters.")
        return

    # Choose file format
    if export_txt:
        export_to_txt(tasks)
    else:
        export_to_csv(tasks)


if __name__ == "__main__":
    export_tasks()

