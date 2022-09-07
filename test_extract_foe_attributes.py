from unittest import TestCase
from game import extract_foe_attributes
from game import create_foe


class TestExtractFoeAttributes(TestCase):
    def test_extract_low_level_foe_attributes(self):
        foe_data = create_foe()
        actual = extract_foe_attributes(foe_data, 'Spider')
        expected = {'HP': 30, 'max_damage': 6, 'accuracy': 0.5, 'XP': 10}
        self.assertEqual(expected, actual)

    def test_extract_medium_level_foe_attributes(self):
        foe_data = create_foe()
        actual = extract_foe_attributes(foe_data, 'Deceiver')
        expected = {'HP': 45, 'max_damage': 12, 'accuracy': 0.6, 'XP': 30}
        self.assertEqual(expected, actual)

    def test_extract_high_level_foe_attributes(self):
        foe_data = create_foe()
        actual = extract_foe_attributes(foe_data, 'Soul reaper')
        expected = {'HP': 100, 'max_damage': 25, 'accuracy': 0.7, 'XP': 80}
        self.assertEqual(expected, actual)
