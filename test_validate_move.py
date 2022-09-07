from unittest import TestCase
from game import validate_move
from game import bash


class TestValidateMove(TestCase):

    def test_north_from_x_five_y_zero(self):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 5,
                     'Y-coordinate': 0, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = validate_move(character, '1')
        self.assertFalse(actual)

    def test_east_from_x_nine_y_zero(self):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 9,
                     'Y-coordinate': 0, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = validate_move(character, '2')
        self.assertFalse(actual)

    def test_south_from_x_five_y_nine(self):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 5,
                     'Y-coordinate': 9, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = validate_move(character, '3')
        self.assertFalse(actual)

    def test_west_from_x_zero_y_nine(self):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 9, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        actual = validate_move(character, '4')
        self.assertFalse(actual)

    def test_anywhere_from_x_five_y_five(self):
        character = {'name': 'Chris', 'level': 1, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 5,
                     'Y-coordinate': 5, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        for direction in ['1', '2', '3', '4']:
            actual = validate_move(character, direction)
            self.assertTrue(actual)
