#!/usr/bin/python3


"""
    This is the Unittest module for the Basemodel Class.
"""


from models.base_model import BaseModel
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """
        These are the test cases for the BaseModel class.
    """

    def setUp(self):
        """This method sets up the test methods."""
        pass

    def tearDown(self):
        """This method tears down the test methods."""
        pass
    
    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_for_instantiation(self):
        """This tests an instance of the BaseModel class."""
        testinst = BaseModel()
        self.assertEqual(str(type(testinstance)), "<class 'models.base_model.BaseModel'>")
        self.assertInstance(testinstance, BaseModel)
        self.assertTrue(issubclass(type(testinstance), BaseModel))

    def test_for_instantiation_with_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_for_instantiation_with_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [i for i in range(1000)]
        testinst = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        testinst = BaseModel(*args)

    def test_3_attributes(self):
        """Tests attributes value for instance of a BaseModel class."""

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_for_datetime_created(self):
        """This tests if created_at and updated_at are current at instantiation"""
        curr_date = datetime.now()
        testinst = BaseModel()
        timediff = testinst.updated_at - testinst.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        timediff = testinst.created_at - curr_date
        self.assertTrue(abs(timediff.total_seconds()) < 0.1)

    def test_for_id(self):
        """This tests for the unique user ids."""

        x = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(x)), len(x))

    def test_for_str(self):
        """This tests for the __str__ method."""
        testinst = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(testinst))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), testinst.id)
        i = res.group(3)
        i = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", i)
        x = json.loads(i.replace("'",'"'))
        icopy = testinst.__dict__.copy()
        icopy["created_at"] = repr(icopy["created_at"])
        icopy["updated_at"] = repr(icopy["updated_at"])
        self.assertEqual(x, icopy)

    def test_for_save(self):
        """ This tests the public instance method save()."""

        testinst = BaseModel()
        time.sleep(0.5)
        curr_date = datetime.now()
        testinst.save()
        timediff = testinst.updated_at - curr_date
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_for_to_dict(self):
        """This tests the public instance method to_dict()."""

        testinst = BaseModel()
        testinst.name = "The Sample Car"
        testinst.age = 109
        x = testinst.to_dict()
        self.assertEqual(x["id"], testinst.id)
        self.assertEqual(x["__class__"], type(testinst).__name__)
        self.assertEqual(x["created_at"], testinst.created_at.isoformat())
        self.assertEqual(x["updated_at"], testinst.updated_at.isoformat())
        self.assertEqual(x["name"], testinst.name)
        self.assertEqual(x["age"], testinst.age)

    def test_for_to_dict_no_args(self):
        """Tests to_dict() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_for_to_dict_excess_args(self):
        """Tests to_dict() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_for_instantiation_kwargs(self):
        """Tests instantiation with **kwargs."""

        testinst = BaseModel()
        testinst.name = "Holberton"
        testinst.my_number = 89
        testinst_json = testinst.to_dict()
        new_inst = BaseModel(**testinst_json)
        self.assertEqual(new_inst.to_dict(), testinst.to_dict())

    def test_for_instantiation_kwargs_from_dict(self):
        """This tests the instantiation with **kwargs from custom dict."""
        x = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        y = BaseModel(**x)
        self.assertEqual(o.to_dict(), x)

    def test_for_save_2(self):
        """Tests that storage.save() is called from save()."""
        self.resetStorage()
        testinst = BaseModel()
        testinst.save()
        key = "{}.{}".format(type(testinst).__name__, testinst.id)
        x = {key: testinst.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(x)))
            f.seek(0)
            self.assertEqual(json.load(f), x)

    def test_for_save_with_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_for_save_with_too_many_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

if __name__ == '__main__':
    unittest.main()
