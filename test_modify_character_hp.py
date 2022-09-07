from unittest import TestCase
from game import modify_character_hp
from game import confusion


class TestModifyCharacterHp(TestCase):
    def test_modify_character_hp(self):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        damage_to_character = 20
        modify_character_hp(character, damage_to_character)
        self.assertEqual({'name': 'Joker', 'level': 3, 'Current HP': 130, 'Current XP': 0, 'X-coordinate': 0,
                          'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                          'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80),
                          'accuracy': 0.5, 'special_attack': confusion, 'special_attack_name': 'Confusion'}, character)

