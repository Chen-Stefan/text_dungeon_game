from unittest import TestCase
from game import terror


class TestTerror(TestCase):

    def test_terror_reduce_foe_max_damage(self):
        character = {'name': 'Illidan', 'level': 3, 'Current HP': 160, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Thief', 'class levels': ('Bandit', 'Assassin', 'Night Lord'),
                     'max_HP': (100, 130, 160), 'levelup_XP': (100, 150), 'max_damage': (20, 30, 40), 'accuracy': 0.9,
                     'special_attack': terror, 'special_attack_name': 'Terror'}
        foe = {'HP': 80, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60}
        foe_type = 'Death maiden'
        terror(character, foe, foe_type)
        self.assertEqual({'HP': 80, 'max_damage': 10, 'accuracy': 0.7, 'XP': 60}, foe)
