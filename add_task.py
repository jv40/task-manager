import json
import re
DATA_FILE="data.json"

def is_valid_date(d):
	"""Validate YYYY--MM--DD format"""
	return re.match(r"^\d{4}-\d{2}-\d{2}$",d) is not None

def add_task():
	description=input("Enter task description: ").strip()
	priority=input("Enter priority (high/medium/low): ").strip().lower()
	due_date=input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
	if due_date=="":
		due_date=None
	elif not is_valid_date(due_date):
		print("Invalid date format. Must be YYYY-MM-DD.")
		return
	with open(DATA_FILE,"r") as f:
		data=json.load(f)
	task_id=len(data["tasks"])+1
	new_task={
		"id":task_id,
		"description":description,
		"priority": priority,
		"completed": False,
		"due_date":due_date,
		"completion_date":None
	}
	data["tasks"].append(new_task)
	with open(DATA_FILE,"w") as f:
		json.dump(data,f,indent=4)
	print(f"Task #{task_id} added successfully!")
if __name__=="__main__":
	add_task()

