from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.randint', side_effect=[20])
    def test_there_is_foe_inside_boundary(self, mock_randint):
        actual = check_for_foes()
        self.assertTrue(actual)

    @patch('random.randint', side_effect=[21])
    def test_there_is_foe_outside_boundary(self, mock_randint):
        actual = check_for_foes()
        self.assertFalse(actual)

    @patch('random.randint', side_effect=[75])
    def test_there_is_no_foe(self, mock_randint):
        actual = check_for_foes()
        self.assertFalse(actual)