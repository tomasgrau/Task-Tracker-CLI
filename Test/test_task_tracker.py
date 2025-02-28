import unittest
import json
import os
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
    def test_get_tasks(self):
        pass

class TestWriteTask(unittest.TestCase):
    def test_write_task(self):
        pass

class TestTaskTracker(unittest.TestCase):
    def test_add(self):
        pass 

    def test_update(self):
        pass

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