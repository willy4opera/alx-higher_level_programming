#!/usr/bin/python3
"""Here, we defined unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 108
    TestBase_save_to_file - line 154
    TestBase_from_json_string - line 232
    TestBase_create - line 286
    TestBase_load_from_file - line 338
    TestBase_save_to_file_csv - line 404
    TestBase_load_from_file_csv - line 482
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Dev_testinstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def dev_test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def dev_test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def dev_test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def dev_test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def dev_test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def dev_test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def dev_test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def dev_test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def dev_test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def dev_test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def dev_test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def dev_test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def dev_test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def dev_test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def dev_test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def dev_test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def dev_test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def dev_test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def dev_test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def dev_test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def dev_test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def dev_test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def dev_test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
