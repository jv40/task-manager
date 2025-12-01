import json
import sys
DATA_FILE="data.json"

PRIORITY_ORDER={
	"high":1,
	"medium":2,
	"low":3
}

def view_tasks():
	show_completed="--show-completed" in sys.argv
	with open(DATA_FILE,"r") as f:
		data=json.load(f)
	tasks=data["tasks"]
	if not show_completed:
		tasks=[t for t in tasks if not t["completed"]]
	tasks.sort(key=lambda t: PRIORITY_ORDER.get(t["priority"],99))
	if not tasks:
		print("No tasks to display.")
		return
	for t in tasks:
		status="Completed" if t["completed"] else "Pending"
		due=t["due_date"] if t["due_date"] else "None"
		print(f"[{t['id']}] {t['description']} ({t['priority']})")
		print(f"       Due: {due}")
		print(f"       Status: {status}")
		if t["completion_date"]:
			print(f"          Completed on: {t['completion_date']}")
		print()
if __name__=="__main__":
	view_tasks()
