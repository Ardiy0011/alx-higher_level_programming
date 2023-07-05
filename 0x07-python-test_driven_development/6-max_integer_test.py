#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """regular expectation"""
        expected_ = [1, 5, 3, 9, 2]
        self.assertEqual(max_integer(expected_), 9)

    def max_at_begining(self):
        """regular expectation"""
        expected_ = [9, 5, 3, 2, 1]
        self.assertEqual(max_integer(expected_), 9)

    def empty(self):
        """Test where list is empty"""
        Empty_list = []
        self.assertEqual(max_integer(Empty_list), None)

    def negative(self):
        """Test for negative integers"""
        non_integer = [-10, -5, -3, -20]
        self.assertEqual(max_integer(non_integer), -3)

    def single(self):
        """where only a single integer or element is passed."""
        one_elemet = [42]
        self.assertEqual(max_integer(one_elemet), 42)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Tests a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")
