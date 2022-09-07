from unittest import TestCase
from game import determine_class_type


class TestDetermineClassType(TestCase):

    def test_one_warrior(self):
        actual = determine_class_type('1')
        expected = 'Warrior'
        self.assertEqual(expected, actual)

    def test_three_amazon(self):
        actual = determine_class_type('3')
        expected = 'Amazon'
        self.assertEqual(expected, actual)
