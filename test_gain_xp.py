from unittest import TestCase
from game import gain_xp
from game import confusion


class TestGainXp(TestCase):
    def test_gain_xp(self):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 1, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        foe = {'HP': 100, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        gain_xp(character, foe)
        self.assertEqual({'name': 'Joker', 'level': 3, 'Current HP': 1, 'Current XP': 80, 'X-coordinate': 0,
                          'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                          'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80),
                          'accuracy': 0.5,
                          'special_attack': confusion, 'special_attack_name': 'Confusion'}, character)
