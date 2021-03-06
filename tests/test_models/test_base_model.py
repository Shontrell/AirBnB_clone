#!/usr/bin/python3
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
import os
import json


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


class TestBaseModelClass(unittest.TestCase):
    """ test BaseModel Class methods """
    @classmethod
    def setUpClass(cls):
        """ create instance for test """
        cls.basemodel = BaseModel()

    def test_id(self):
        """ test type of id of an instance """
        self.assertEqual(str, type(self.basemodel.id))

    def test_created_at(self):
        """ test type of created_at attribute """
        self.assertEqual(datetime, type(self.basemodel.created_at))

    def test_updated_at(self):
        """ test type of updated at attribute """
        self.assertEqual(datetime, type(self.basemodel.updated_at))

    def test_to_dict(self):
        """ test to_dict method """
        dictionary = self.basemodel.to_dict() ''' create tmp dict and check type'''
        self.assertEqual(type(dictionary), dict)
        ''' check if method is in dir '''
        self.assertTrue('to_dict' in dir(self.basemodel))

    @classmethod
    def tearDownClass(cls):
        """ delete instance of test cases """
        pass
