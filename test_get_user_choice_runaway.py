from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice_runaway


class TestGetUserChoiceRunaway(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_runaway(self, mock_input):
        actual = get_user_choice_runaway()
        expected = "1"
        self.assertEqual(expected, actual)
