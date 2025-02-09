# Task Tracker CLI

import argparse
import json
import os
from datetime import datetime

def create_file(task):
    print(task)
    with open("tasks.json", "w") as tasks_file:
        json.dump([task], tasks_file, indent=2)

def add_task(task: str):
    # Function to add a new task
    id = 0
    new_task = {
        "id": id,
        "description": task,
        "status": "New task",
        "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": ""
    }
    # Check if the tasks file exists
    if os.path.exists("tasks.json"):
        # Add task
        with open("tasks.json", "r") as tasks_file:
            tasks_list = json.load(tasks_file)
            # Get last task id 
            id = tasks_list[-1]["id"]
            # Set new id to new task
            new_task["id"] = id + 1
            # Save new task
            tasks_list.append(new_task)
            print(tasks_list)
        
        with open("tasks.json", "w") as tasks_file:
            json.dump(tasks_list, tasks_file, indent=2)

    else:
        # Create tasks file and add new task
        create_file(new_task)

    def update_task(id: int, task: str):
        with open("tasks.json", "w") as tasks_file:
            tasks_list = json.load(tasks_file)
            for task in tasks_list:
                if task["id"] == id:
                    task["description"] = task
                    task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                else:
                    print("This task doesn't exist")




def main():
    parser = argparse.ArgumentParser(prog="Task Tracker CLI", description="Simple Task Tracker")
    parser.add_argument("-a", "--add", type=str, help="Add a new task")
    parser.add_argument("-u", "--update", nargs=2, help="Update a task already created")
    args = parser.parse_args()
    if args.add:
        add_task(args.add)
    if args.update:
        print(args.update)
        

if __name__ == '__main__':
    main()