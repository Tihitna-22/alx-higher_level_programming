#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests to check Base class"""
    def test_no_id(self):
        """Tests id as None"""
        bs = Base()
        self.assertEqual(bs.id, 1)

    def test_no_id_after_set(self):
        """Tests id as None after not None"""
        bs2 = Base()
        self.assertEqual(bs2.id, 2)

    def test_to_json_string(self):
        """Tests regular to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 6, "width": 3, "height": 4, "x": 5, "y": 6}
        d2 = {"id": 5, "width": 4, "height": 6, "x": 7, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        a = json.loads(json_s)
        self.assertEqual(a, [d1, d2])

    def test_empty_to_json_string(self):
        """Test for passing empty list/ None"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        json_s = Base.to_json_string(None)
        self.assertEqual(json_s, [])
