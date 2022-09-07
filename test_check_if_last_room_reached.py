from unittest import TestCase
from game import check_if_last_room_reached
from game import confusion


class TestCheckIfLastRoomReached(TestCase):
    def test_last_room_not_reached(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 180, 'X-coordinate': 8,
                     'Y-coordinate': 9, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = check_if_last_room_reached(character)
        self.assertFalse(actual)

    def test_last_room_is_reached(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 180, 'X-coordinate': 9,
                     'Y-coordinate': 9, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = check_if_last_room_reached(character)
        self.assertTrue(actual)
