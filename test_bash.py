from unittest import TestCase
from game import bash


class TestBash(TestCase):

    def test_bash_damage(self):
        character = {'name': 'Chris', 'level': 2, 'Current HP': 100, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'),
                     'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6,
                     'special_attack': bash, 'special_attack_name': 'Bash'}
        foe = {'HP': 80, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60}
        foe_type = 'Death maiden'
        bash(character, foe, foe_type)
        self.assertEqual({'HP': 80 - 45 * 1.3, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60}, foe)
