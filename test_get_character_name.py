from unittest import TestCase
from unittest.mock import patch
from game import get_character_name


class TestGetCharacterName(TestCase):
    @patch('builtins.input', side_effect=['Big Daddy'])
    def test_get_character_name(self, mock_input):
        actual = get_character_name()
        expected = "Big Daddy"
        self.assertEqual(expected, actual)
