import json
import argparse
from datetime import datetime
import os

DATA_FILE = "data.json"
LOG_FILE = "deleted.log"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def log_deletion(task):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Deleted Task ID={task['id']} | \"{task['description']}\"\n"
    with open(LOG_FILE, "a") as log:
        log.write(entry)


def delete_task(task_id, force=False):
    tasks = load_tasks()
    task_to_delete = None

    for t in tasks:
        if t["id"] == task_id:
            task_to_delete = t
            break

    if task_to_delete is None:
        print("Task not found.")
        return

 
    if task_to_delete.get("completed", False) and not force:
        response = input(
            "This task is already completed. Are you sure you want to delete it? (y/n): " ).strip().lower()
        if response != "y":
            print("Deletion cancelled.")
            return

    tasks.remove(task_to_delete)
    save_tasks(tasks)
    log_deletion(task_to_delete)

    print(f"Task {task_id} deleted successfully.")


def main():
    parser = argparse.ArgumentParser(description="Delete a task by ID.")
    parser.add_argument("id", type=int, help="ID of the task to delete")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Delete completed tasks without confirmation"
    )

    args = parser.parse_args()
    delete_task(args.id, args.force)


if __name__ == "__main__":
    main()
