from unittest import TestCase
from unittest.mock import patch
from game import attack_hit_foe
from game import confusion


class TestAttackHitFoe(TestCase):
    @patch('random.random', side_effect=[0.4])
    def test_attack_hit_foe(self, mock_random):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = attack_hit_foe(character)
        self.assertTrue(actual)

    @patch('random.random', side_effect=[0.5])
    def test_attack_not_hit_foe_on_the_boundary(self, mock_random):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = attack_hit_foe(character)
        self.assertFalse(actual)

    @patch('random.random', side_effect=[0.8])
    def test_attack_not_hit_foe_outside_of_boundary(self, mock_random):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        actual = attack_hit_foe(character)
        self.assertFalse(actual)
