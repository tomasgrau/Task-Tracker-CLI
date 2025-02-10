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
        "status": "To do",
        "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": ""
    }
    # Check if the tasks file exists
    if os.path.exists("tasks.json"):
        # Add task
        with open("tasks.json", "r") as tasks_file:
            tasks_list = json.load(tasks_file)
            # Get last task id 
            if tasks_list != []:
                id = tasks_list[-1]["id"]
                new_task["id"] = id + 1
            # Save new task
            tasks_list.append(new_task)
            print("Task created successfully")
        
        with open("tasks.json", "w") as tasks_file:
            json.dump(tasks_list, tasks_file, indent=2)

    else:
        # Create tasks file and add new task
        create_file(new_task)

def update_task(id: int, new_task: str):
    with open("tasks.json", "r") as tasks_file:
        tasks_list = json.load(tasks_file)
        for task in tasks_list:
            if task["id"] == id:
                task["description"] = new_task
                task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            else:
                print("This task doesn't exist")
    with open("tasks.json", "w") as tasks_file:
            json.dump(tasks_list, tasks_file, indent=2)

def delete_task(id: int):
    with open("tasks.json", "r") as tasks_file:
        tasks_list :list = json.load(tasks_file)
        for i, task in enumerate(tasks_list):
            if task["id"] == id:
                print("Task found")
                tasks_list.pop(i)
                try:
                    with open("tasks.json", "w") as tasks_file:
                        json.dump(tasks_list, tasks_file, indent=2)
                    return "Task deleted"
                except IOError as e:
                    print(f"Error writing to tasks file: {e}")
                    return
        print("Task not found")

def list_tasks():
    with open("tasks.json", "r") as tasks_file:
        tasks_list: list = json.load(tasks_file)
        if tasks_list == []:
            print("There are not tasks yet")
            return
        for task in tasks_list:
            print(f"- {task["description"]}  State: {task["status"]}")

def list_in_progress():
    with open("tasks.json", "r") as tasks_file:
        tasks_list: list = json.load(tasks_file)
        if tasks_list == []:
            print("There are not tasks yet")
            return
        
        in_progress_found = False
        for task in tasks_list:
            if task["status"] == "in-progress":
                print(f"- {task["description"]}  State: {task["status"]}")
                in_progress_found = True
        if not in_progress_found:
            print("There are no tasks in-progress yet")
        

def list_done():
    with open("tasks.json", "r") as tasks_file:
        tasks_list: list = json.load(tasks_file)
        if tasks_list == []:
            print("There are not tasks yet")
            return

        done_tasks_found = False
        for task in tasks_list:
            if task["status"] == "done":
                print(f"- {task["description"]}  State: {task["status"]}")           
                done_tasks_found = True
        
        if not done_tasks_found:
            print("There are no tasks done yet")

def main():
    parser = argparse.ArgumentParser(prog="Task Tracker CLI", description="Simple Task Tracker")
    parser.add_argument("-a", "--add", nargs="+", type=str, help="Add a new task")
    parser.add_argument("-u", "--update", nargs="+", help="Update a task already created")
    parser.add_argument("-d", "--delete", nargs=1, type=int, help="Delete a task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-li", "--in-progress", help="List tasks that are in-progress")
    parser.add_argument("-ld", "--done", help="List tasks that are done")
    parser.add_argument("-mi", "--mark-in-progress", help="Change status of a task to in progress")
    parser.add_argument("-md", "--mark-done", help="Change status of a task to done")
    
    args = parser.parse_args()
    if args.add:
        add_task(" ".join(args.add))
    if args.update:
        id = int(args.update[0])
        task_args = args.update[1:]
        new_task = " ".join(task_args)
        print(new_task)
        update_task(id, new_task)
    if args.delete:
        print(args.delete[0])
        delete_task(args.delete[0])
    if args.list:
        list_tasks()
    if args.in_progress:
        list_in_progress()
    if args.done:
        list_done()


        
        

if __name__ == '__main__':
    main()