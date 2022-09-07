from unittest import TestCase
from game import determine_foe_in_same_area
from game import confusion


class TestDetermineFoeInSameArea(TestCase):
    def test_determine_foe_in_low_level_area(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 180, 'X-coordinate': 8,
                     'Y-coordinate': 2, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = determine_foe_in_same_area(character)
        expected = ['Spider', 'Ghoul', 'Skeleton']
        self.assertEqual(expected, actual)

    def test_determine_foe_in_medium_level_area(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 180, 'X-coordinate': 7,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = determine_foe_in_same_area(character)
        expected = ['Deceiver', 'Succubus', 'Berserker']
        self.assertEqual(expected, actual)

    def test_determine_foe_in_high_level_area(self):
        character = {'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 180, 'X-coordinate': 7,
                     'Y-coordinate': 8, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = determine_foe_in_same_area(character)
        expected = ['Death maiden', 'Corrupted angel', 'Soul reaper']
        self.assertEqual(expected, actual)
