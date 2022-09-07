from unittest import TestCase
from game import recover_character_hp
from game import confusion


class TestRecoverCharacterHp(TestCase):
    def test_recover_character_hp(self):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 80, 'Current XP': 20, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        recover_character_hp(character)
        self.assertEqual({'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 20, 'X-coordinate': 0,
                          'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                          'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80),
                          'accuracy': 0.5, 'special_attack': confusion, 'special_attack_name': 'Confusion'}, character)
