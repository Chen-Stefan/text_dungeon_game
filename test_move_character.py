from unittest import TestCase
from game import move_character
from game import bash


class TestMoveCharacter(TestCase):

    def test_move_character_north(self):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = move_character(character, '1')
        expected = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 0,
                    'Y-coordinate': 5, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                    'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                    'special_attack': bash, 'special_attack_name': 'Bash'}
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 6,
                     'Y-coordinate': 7, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = move_character(character, '2')
        expected = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 7,
                    'Y-coordinate': 7, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                    'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                    'special_attack': bash, 'special_attack_name': 'Bash'}
        self.assertEqual(expected, actual)
