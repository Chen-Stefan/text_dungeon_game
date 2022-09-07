from unittest import TestCase
from unittest.mock import patch
from game import get_user_direction_choice


class TestGetUserDirectionChoice(TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_get_user_direction_choice(self, mock_input):
        actual = get_user_direction_choice()
        expected = "3"
        self.assertEqual(expected, actual)