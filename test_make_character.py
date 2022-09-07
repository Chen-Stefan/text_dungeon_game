from unittest import TestCase
from game import make_character
from game import bash
from game import focus


class TestMakeCharacter(TestCase):

    def test_merge_with_warrior(self):
        character_name = 'Chris'
        class_attributes = {'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                            'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60),
                            'accuracy': 0.6, 'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = make_character(character_name, class_attributes)
        expected = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 0,
                    'Y-coordinate': 0, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                    'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                    'special_attack': bash, 'special_attack_name': 'Bash'}
        self.assertEqual(expected, actual)

    def test_merge_with_amazon(self):
        character_name = 'Hoda'
        class_attributes = {'class name': 'Amazon', 'class levels': ('Archer', 'Ranger', 'Demon Hunter'),
                            'max_HP': (100, 140, 180), 'levelup_XP': (100, 160), 'max_damage': (30, 40, 50),
                            'accuracy': 0.8, 'special_attack': focus, 'special_attack_name': 'Focus'}
        actual = make_character(character_name, class_attributes)
        expected = {'name': 'Hoda', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 0,
                    'Y-coordinate': 0, 'class name': 'Amazon', 'class levels': ('Archer', 'Ranger', 'Demon Hunter'),
                            'max_HP': (100, 140, 180), 'levelup_XP': (100, 160), 'max_damage': (30, 40, 50),
                            'accuracy': 0.8, 'special_attack': focus, 'special_attack_name': 'Focus'}
        self.assertEqual(expected, actual)
