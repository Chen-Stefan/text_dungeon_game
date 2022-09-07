from unittest import TestCase
from unittest.mock import patch
from game import get_character_class


class TestGetCharacterClass(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_get_character_class(self, mock_input):
        actual = get_character_class()
        expected = "2"
        self.assertEqual(expected, actual)
