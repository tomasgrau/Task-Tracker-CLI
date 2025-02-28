import unittest
import json
import os
import task_tracker

class TestTaskFile(unittest.TestCase):
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

        

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_sum(self):
        self.assertEqual(2+2,4)



if __name__ == "__main__":
    unittest.main()