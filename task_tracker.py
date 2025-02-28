# Task Tracker CLI

import argparse
import json
import os
from datetime import datetime

def create_file(task):
    with open("tasks.json", "w") as tasks_file:
        json.dump([task], tasks_file, indent=2)
    print(f"Task created!\n-------------------\nId: {task['id']}\nDescription: {task['description']}\nStatus: {task['status']}")

def get_tasks():
    try:
        with open("tasks.json", "r") as tasks_file:
            tasks_list: list = json.load(tasks_file)
            return tasks_list
    except FileNotFoundError:
        return []
    
def write_tasks(tasks_list):
    with open("tasks.json", "w") as tasks_file:
            json.dump(tasks_list, tasks_file, indent=2)

def add_task(task: str):
    # Function to add a new task
    id = 0
    new_task = {
        "id": id,
        "description": task,
        "status": "to-do",
        "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": ""
    }
    # Check if the tasks file exists
    if os.path.exists("tasks.json"):
        # Add task
        tasks_list = get_tasks() 
        # Get last task id 
        if tasks_list != []:
            id = tasks_list[-1]["id"]
            new_task["id"] = id + 1
        # Save new task
        tasks_list.append(new_task)
        write_tasks(tasks_list)
        print(f"Task created!\n-------------------\nId: {new_task['id']}\nDescription: {new_task['description']}\nStatus: {new_task['status']}")


    else:
        # Create tasks file and add new task
        create_file(new_task)

def update_task(id: int, new_task: str):
    tasks_list = get_tasks()
    if tasks_list == []:
        print("There are not tasks yet")
        return 
    
    task_found = False
    for task in tasks_list:
        if task["id"] == id:
            task["description"] = new_task
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            task_found = True
            break

    if task_found:
        write_tasks(tasks_list)
        print(f"Task updated!\n-------------------\nId: {task['id']}\nDescription: {task['description']}\nStatus: {task['status']}\nUpdated at: {task['updatedAt']}")
    else:
        print(f"Task with id: {id} doesn't exist")

def delete_task(id: int):
    tasks_list = get_tasks()
    if tasks_list == []:
        print("There are not tasks yet")
        return  
    for i, task in enumerate(tasks_list):
        if task["id"] == id:
            tasks_list.pop(i)
            try:
                write_tasks(tasks_list)
                print("Task deleted")
                return 
            except IOError as e:
                print(f"Error writing to tasks file: {e}")
                return
    print("Task not found")

def list_tasks():
        tasks_list = get_tasks()
        if tasks_list == []:
            print("There are not tasks yet")
            return
        for task in tasks_list:
            print(f"{task["id"]} - {task["description"]}, Status: {task["status"]}")

def list_in_progress():
    tasks_list = get_tasks()
    if tasks_list == []:
        print("There are not tasks yet")
        return
    
    in_progress_found = False
    for task in tasks_list:
        if task["status"] == "in-progress":
            print(f"{task["id"]} - {task["description"]}, Status: {task["status"]}")
            in_progress_found = True
    if not in_progress_found:
        print("There are no tasks in-progress yet")
    

def list_done():
    tasks_list = get_tasks()
    if tasks_list == []:
        print("There are not tasks yet")
        return

    done_tasks_found = False
    for task in tasks_list:
        if task["status"] == "done":
            print(f"{task["id"]} - {task["description"]}, Status: {task["status"]}")           
            done_tasks_found = True
    
    if not done_tasks_found:
        print("There are no tasks done yet")

def mark_in_progress(id):
    tasks_list = get_tasks()
    if tasks_list == []:
        print("There are not tasks yet")
        return 
    task_found = False
    for task in tasks_list:
        if task["id"] == id:
            task_found = True
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            write_tasks(tasks_list)
            print(f"Task with id: {id} is now in-progress")

    if not task_found:
        print(f"No task with id: {id} was found")

def mark_done(id):
    tasks_list = get_tasks()
    
    task_found = False
    for task in tasks_list:
        if task["id"] == id:
            task_found = True
            task["status"] = "done"
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            write_tasks(tasks_list)
            print(f"Task with id: {id} is now done")
    
    if not task_found:
        print(f"No task with id: {id} was found")
    


def main():
    parser = argparse.ArgumentParser(prog="Task Tracker CLI", description="Simple Task Tracker")
    parser.add_argument("-a", "--add", nargs="+", type=str, help="Add a new task")
    parser.add_argument("-u", "--update", nargs="+", help="Update a task already created")
    parser.add_argument("-d", "--delete", nargs=1, type=int, help="Delete a task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-li", "--in-progress", action="store_true", help="List tasks that are in-progress")
    parser.add_argument("-ld", "--done", action="store_true", help="List tasks that are done")
    parser.add_argument("-mi", "--mark-in-progress", nargs=1, type=int, help="Change status of a task to in progress")
    parser.add_argument("-md", "--mark-done", nargs=1, type=int, help="Change status of a task to done")
    
    args = parser.parse_args()
    if args.add:
        add_task(" ".join(args.add))
    if args.update:
        id = int(args.update[0])
        task_args = args.update[1:]
        new_task = " ".join(task_args)
        update_task(id, new_task)
    if args.delete:
        delete_task(args.delete[0])
    if args.list:
        list_tasks()
    if args.in_progress:
        list_in_progress()
    if args.done:
        list_done()
    if args.mark_in_progress:
        mark_in_progress(args.mark_in_progress[0])
    if args.mark_done:
        mark_done(args.mark_done[0])

        
if __name__ == '__main__':
    main()