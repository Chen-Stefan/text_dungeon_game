from unittest import TestCase
from game import is_level_up
from game import confusion


class TestIsLevelUp(TestCase):
    def test_is_ready_to_level_up(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 150, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = is_level_up(character)
        self.assertTrue(actual)

    def test_is_not_yet_qualified_to_level_up(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 149, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = is_level_up(character)
        self.assertFalse(actual)
