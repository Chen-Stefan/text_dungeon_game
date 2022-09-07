from unittest import TestCase
from unittest.mock import patch
from game import foe_runaway


class TestFoeRunaway(TestCase):
    @patch('random.random', side_effect=[0.1])
    def test_foe_runaway(self, mock_random):
        actual = foe_runaway()
        self.assertTrue(actual)

    @patch('random.random', side_effect=[0.2])
    def test_foe_stays_on_the_boundary(self, mock_random):
        actual = foe_runaway()
        self.assertFalse(actual)

    @patch('random.random', side_effect=[0.8])
    def test_foe_stays_outside_of_boundary(self, mock_random):
        actual = foe_runaway()
        self.assertFalse(actual)