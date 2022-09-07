from unittest import TestCase
from game import focus


class TestFocus(TestCase):
    def test_focus_increase_character_accuracy(self):
        character = {'name': 'Wonder woman', 'level': 3, 'Current HP': 180, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Amazon', 'class levels': ('Archer', 'Ranger', 'Demon Hunter'),
                     'max_HP': (100, 140, 180), 'levelup_XP': (100, 160), 'max_damage': (30, 40, 50), 'accuracy': 0.8,
                     'special_attack': focus, 'special_attack_name': 'Focus'}
        foe = {'HP': 80, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60}
        foe_type = 'Death maiden'
        focus(character, foe, foe_type)
        self.assertEqual({'name': 'Wonder woman', 'level': 3, 'Current HP': 180, 'Current XP': 0, 'X-coordinate': 0,
                          'Y-coordinate': 6, 'class name': 'Amazon', 'class levels':
                          ('Archer', 'Ranger', 'Demon Hunter'), 'max_HP': (100, 140, 180), 'levelup_XP': (100, 160),
                          'max_damage': (30, 40, 50), 'accuracy': 1, 'special_attack': focus,
                          'special_attack_name': 'Focus'}, character)
