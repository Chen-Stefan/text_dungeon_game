from unittest import TestCase
from unittest.mock import patch
from game import attack_hit_character


class TestAttackHitCharacter(TestCase):
    @patch('random.random', side_effect=[0.5])
    def test_attack_hit_character(self, mock_random):
        foe = {'HP': 100, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        actual = attack_hit_character(foe)
        self.assertTrue(actual)

    @patch('random.random', side_effect=[0.7])
    def test_attack_not_hit_character_on_the_boundary(self, mock_random):
        foe = {'HP': 100, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        actual = attack_hit_character(foe)
        self.assertFalse(actual)

    @patch('random.random', side_effect=[0.9])
    def test_attack_not_hit_character_outside_of_boundary(self, mock_random):
        foe = {'HP': 100, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        actual = attack_hit_character(foe)
        self.assertFalse(actual)