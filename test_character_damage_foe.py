from unittest import TestCase
from unittest.mock import patch
from game import character_damage_foe
from game import confusion


class TestCharacterDamageFoe(TestCase):
    @patch('random.randrange', side_effect=[75])
    def test_character_damage_foe_lower_bound(self, mock_randrange):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = character_damage_foe(character)
        self.assertEqual(75, actual)

    @patch('random.randrange', side_effect=[80])
    def test_character_damage_foe_upper_bound(self, mock_randrange):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = character_damage_foe(character)
        self.assertEqual(80, actual)
