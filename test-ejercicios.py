import unittest
from unittest import TestCase
from main import pluralize, same_length


class TestPluralize(TestCase):
    def test_pluralize_cows_pig(self):
        self.assertEqual(pluralize(["cow", "pig", "cow", "cow"]), {"cows", "pig"})
    def test_pluralize_tables(self):
        self.assertEqual(pluralize(["table", "table", "table"]), {"tables"})
    def test_pluralize_chair_pencil_arm(self):
        self.assertEqual(pluralize(["chair", "pencil", "arm"]), {"chair", "pencil", "arm"})


class TestSameLength(TestCase):
    def test_same_length(self):
        self.assertTrue(same_length("110011100010"))
    def test_same_length_1(self):
        self.assertFalse(same_length("101010110"))
    def test_same_length_2(self):
        self.assertTrue(same_length("111100001100"))
    def test_same_length_3(self):
        self.assertFalse(same_length("111"))

if __name__ == "__main__":
    unittest.main()