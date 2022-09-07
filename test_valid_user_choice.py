from unittest import TestCase
from game import valid_user_choice


class TestValidUserChoice(TestCase):

    def test_two_for_length_two(self):
        actual = valid_user_choice('2', 2)
        self.assertTrue(actual)

    def test_three_for_length_two(self):
        actual = valid_user_choice('3', 2)
        self.assertFalse(actual)

    def test_four_for_length_four(self):
        actual = valid_user_choice('4', 4)
        self.assertTrue(actual)

    def test_five_for_length_four(self):
        actual = valid_user_choice('5', 4)
        self.assertFalse(actual)
