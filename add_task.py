import json
import os

DATA_FILE = "data.json"

def load_data():
    """Load task data from data.json or create default structure."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {
        "tasks": [],
        "settings": {
            "app_name": "Task Manager",
            "version": "1.0.0",
            "max_tasks": 100
        }
    }

def save_data(data):
    """Save task data back to data.json."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_next_id(tasks):
    """Return the next task ID."""
    if not tasks:
        return 1
    highest = 0
    for t in tasks:
        if int(t.get("id", 0)) > highest:
            highest = int(t["id"])
    return highest + 1

def add_task(description, priority):
    """Add a new task with description and priority."""
    data = load_data()
    tasks = data["tasks"]

    max_tasks = data.get("settings", {}).get("max_tasks", 100)
    if len(tasks) >= max_tasks:
        print("You have reached the maximum number of tasks.")
        return

    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "priority": priority,
        "completed": False
    }

    tasks.append(new_task)
    save_data(data)
    print(" Task added:", description, "(Priority:", priority + ")")

if __name__ == "__main__":
    print("Enter task description:")
    desc = input().strip()
    print("Enter priority (high, medium, low):")
    prio = input().strip().lower()
    if prio not in ["high", "medium", "low"]:
        print("Priority must be: high, medium, or low.")
    else:
        add_task(desc, prio)

