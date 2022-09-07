from unittest import TestCase
from unittest.mock import patch
from game import determine_foe_type


class TestDetermineFoeType(TestCase):
    @patch('random.randint', side_effect=[0])
    def test_determine_low_level_foe_type(self, mock_randint):
        foe_of_same_level = ['Spider', 'Ghoul', 'Skeleton']
        actual = determine_foe_type(foe_of_same_level)
        self.assertEqual('Spider', actual)

    @patch('random.randint', side_effect=[1])
    def test_determine_medium_level_foe_type(self, mock_randint):
        foe_of_same_level = ['Deceiver', 'Succubus', 'Berserker']
        actual = determine_foe_type(foe_of_same_level)
        self.assertEqual('Succubus', actual)

    @patch('random.randint', side_effect=[2])
    def test_determine_high_level_foe_type(self, mock_randint):
        foe_of_same_level = ['Death maiden', 'Corrupted angel', 'Soul reaper']
        actual = determine_foe_type(foe_of_same_level)
        self.assertEqual('Soul reaper', actual)
