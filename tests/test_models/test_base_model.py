#!usr/bin/python3
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModelDocs(unittest.TestCase):
    """ test for docstrings """
    def test_documentation(self):
        """ class docstring test """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_pub_priv_methods(self):
        """ methods docstring test """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

class TestBaseModelPep8(unittest.TestCase):
    """ test for pep8 formatting """
    def pep8_test(self):
        """ test base and test_base for pep8 formatting """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        res = style.check_files([file1, file2])
        self.assertEqual(res.total_errors,
                         0, "Pep style errors and warnings my dog.")