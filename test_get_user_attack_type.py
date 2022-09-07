from unittest import TestCase
from unittest.mock import patch
from game import get_user_attack_type
from game import bash


class TestGetUserAttackType(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_get_user_attack_type(self, mock_input):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = get_user_attack_type(character)
        expected = "2"
        self.assertEqual(expected, actual)
