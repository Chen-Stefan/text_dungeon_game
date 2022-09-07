from unittest import TestCase
from unittest.mock import patch
from game import foe_damage_character


class TestFoeDamageCharacter(TestCase):
    @patch('random.randrange', side_effect=[23])
    def test_foe_damage_character_lower_bound(self, mock_randrange):
        foe = {'HP': 100, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        actual = foe_damage_character(foe)
        self.assertEqual(23, actual)

    @patch('random.randrange', side_effect=[26])
    def test_foe_damage_character_upper_bound(self, mock_randrange):
        foe = {'HP': 100, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        actual = foe_damage_character(foe)
        self.assertEqual(26, actual)
