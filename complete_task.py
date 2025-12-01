import json
from datetime import datetime

DATA_FILE="data.json"

def complete_task():
	task_id=input("Enter task ID to complete: ").strip()
	if not task_id.isdigit():
		print("Invalid ID format.")
		return
	task_id=int(task_id)
	with open(DATA_FILE,"r") as f:
		data=json.load(f)
	found=None
	for t in data["tasks"]:
		if t["id"] == task_id:
			found=t
			break
	if not found:
		print("Task not found.")
		return
	if found["completed"]:
		undo=input("Task is already completed. Undo completion? (yes/no): ")
		if undo=="yes":
			found["completed"]=False
			found["completion_date"]=None
			print("Completion undone.")
		else:
			print("No changes made.")
	else:
		found["completed"]=True
		found["completion_date"]=datetime.now().strftime("%Y-%m-%d")
		print("Task marked completed!")
	with open(DATA_FILE,"w") as f:
		json.dump(data,f,indent=4)
if __name__=="__main__":
	complete_task()
