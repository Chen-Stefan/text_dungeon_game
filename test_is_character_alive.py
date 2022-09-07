from unittest import TestCase
from game import is_character_alive
from game import confusion


class TestIsCharacterAlive(TestCase):
    def test_character_is_alive(self):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 1, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = is_character_alive(character)
        self.assertTrue(actual)

    def test_character_is_dead(self):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 0, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = is_character_alive(character)
        self.assertFalse(actual)
