import json
DATA_FILE="data.json"
def load_tasks():
	if not os.path.exists(DATA_FILE):
		print("Error: data.json file not found.")
		return {"tasks":[]}
	with open(DATA_FILE,"r") as f:
		data=json.load(f)
	return data
def save_tasks(data):
	with open(DATA_FILE,"w") as f:
		json.dump(data,f,indent=4)

def complete_task(task_id):
	data=load_tasks()
	tasks=data["tasks"]
	found=False
	for task in tasks:
		if task["id"]==task_id:
			found=True
			if task["completed"]:
				print("Task",task_id,"is already completed.")
			else:
				task["completed"]=True
				save_tasks(data)
				print("Task",task_id,"marked as completed.")
			break
	if not found:
		print("Task with ID",task_id,"not found.")
if __name__=="__main__":
	import os
	print("Enter the task to complete:")
	task_id_input=input().strip()
	if task_id_input.isdigit():
		task_id=int(task_id_input)
		complete_task(task_id)
	else:
		print("Please enter a valid task ID number.")
