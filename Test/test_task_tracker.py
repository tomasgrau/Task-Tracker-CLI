import unittest
import json
import os

import filecmp
import sys
from datetime import datetime

sys.path.append("..")

import task_tracker

class TestCreateTaskFile(unittest.TestCase):
    def setUp(self):
        os.mkdir("test_dir")
        os.chdir("test_dir")

    def tearDown(self):
        os.chdir("..")
        for file in os.listdir("test_dir"):
            os.remove(os.path.join("test_dir", file))
        os.rmdir("test_dir")
        
    
    def test_create_file(self):
        task = {
        "id": 0,
        "description": "",
        "status": "to-do",
        "createdAt": "",
        "updatedAt": ""
        }
        task_tracker.create_file(task)
        self.assertTrue(os.path.exists("tasks.json"))

class TestGetTasks(unittest.TestCase):
    def setUp(self):
        os.mkdir("test_dir")
        os.chdir("test_dir")
        with open("tasks.json", "w") as tasks:
            json.dump(
                [
                    {
                        "id": 0,
                        "description": "Cocinar",
                        "status": "to-do",
                        "createdAt": "28/02/2025 17:35:07",
                        "updatedAt": ""
                    },
                    {
                        "id": 1,
                        "description": "Cocinar 2",
                        "status": "to-do",
                        "createdAt": "01/03/2025 00:13:46",
                        "updatedAt": ""
                    }
                ]
            , tasks, indent=2)

    def tearDown(self):
        os.chdir("..")
        for file in os.listdir("test_dir"):
            os.remove(os.path.join("test_dir", file))
        os.rmdir("test_dir")

    def test_get_tasks(self):
        self.assertEqual(task_tracker.get_tasks(),
                         [
                    {
                        "id": 0,
                        "description": "Cocinar",
                        "status": "to-do",
                        "createdAt": "28/02/2025 17:35:07",
                        "updatedAt": ""
                    },
                    {
                        "id": 1,
                        "description": "Cocinar 2",
                        "status": "to-do",
                        "createdAt": "01/03/2025 00:13:46",
                        "updatedAt": ""
                    }
                ]
                )

class TestWriteTask(unittest.TestCase):

    def setUp(self):
        os.mkdir("test_dir")
        os.chdir("test_dir")
        with open("test.json", "w") as tasks:
            json.dump(
                [
                    {
                        "id": 0,
                        "description": "Cocinar",
                        "status": "to-do",
                        "createdAt": "28/02/2025 17:35:07",
                        "updatedAt": ""
                    },
                    {
                        "id": 1,
                        "description": "Cocinar 2",
                        "status": "to-do",
                        "createdAt": "01/03/2025 00:13:46",
                        "updatedAt": ""
                    }
                ]
            , tasks, indent=2)
            
    def tearDown(self):
        os.chdir("..")
        for file in os.listdir("test_dir"):
            os.remove(os.path.join("test_dir", file))
        os.rmdir("test_dir")

    def test_write_task(self):
        task_tracker.write_tasks([
                    {
                        "id": 0,
                        "description": "Cocinar",
                        "status": "to-do",
                        "createdAt": "28/02/2025 17:35:07",
                        "updatedAt": ""
                    },
                    {
                        "id": 1,
                        "description": "Cocinar 2",
                        "status": "to-do",
                        "createdAt": "01/03/2025 00:13:46",
                        "updatedAt": ""
                    }
                ])
        self.assertTrue(filecmp.cmp("tasks.json", "test.json"))
        

class TestTaskTracker(unittest.TestCase):
    def setUp(self):
        os.mkdir("test_dir")
        os.chdir("test_dir")
        with open("tasks.json", "w") as task_file:
            json.dump([],task_file)
    
    def tearDown(self):
        os.chdir("..")
        for file in os.listdir("test_dir"):
            os.remove(os.path.join("test_dir", file))
        os.rmdir("test_dir")


    def test_add(self):
        new_task = {
        "id": 0,
        "description": "Cook",
        "status": "to-do",
        "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": ""
    }
        task_tracker.add_task("Cook")
        with open("tasks.json", "r") as tasks_file:
            tasks = json.load(tasks_file)
        self.assertEqual(new_task,tasks[0])

    def test_update(self):
        updated_task = {
        "id": 0,
        "description": "Cook 2",
        "status": "to-do",
        "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
        task_tracker.add_task("Cook")
        task_tracker.update_task(0, "Cook 2")
        with open("tasks.json", "r") as tasks_file:
            tasks = json.load(tasks_file)
        self.assertEqual(updated_task, tasks[0])

    def test_update_non_existing_task(self):
        task_tracker.add_task("Cook")
        self.assertEqual(task_tracker.update_task(12, "Cook"), False)

    def test_delete(self):
        pass

    def test_list(self):
        pass

    def test_list_in_progress(self):
        pass

    def test_list_done(self):    
        pass

    def test_mark_in_progress(self):
        pass

    def test_mark_done(self):
        pass



if __name__ == "__main__":
    unittest.main()