from unittest import TestCase
from game import level_up
from game import confusion


class TestLevelUp(TestCase):
    def test_level_up_and_update_new_xp(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 180, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = level_up(character)
        self.assertEqual({'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 30, 'X-coordinate': 0,
                          'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                          'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80),
                          'accuracy': 0.5,
                          'special_attack': confusion, 'special_attack_name': 'Confusion'}, actual)
