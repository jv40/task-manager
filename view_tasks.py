import json
import os

DATA_FILE = "data.json"

def load_data():
    """Load tasks from JSON file or return empty list wrapper."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": []}

def view_tasks():
    """Display all tasks neatly with ID, status, priority, description."""
    data = load_data()
    tasks = data.get("tasks", [])

    if not tasks:
        print("No tasks available.")
        return

    print("\n Task List")
    print("-" * 50)
    for task in tasks:
        status = " Completed" if task.get("completed") else " Not Completed"
        print("ID:", task.get("id"))
        print("Description:", task.get("description"))
        print("Priority:", task.get("priority"))
        print("Status:", status)
        print("-" * 50)

if __name__ == "__main__":
    view_tasks()

