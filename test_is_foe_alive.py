from unittest import TestCase
from game import is_foe_alive


class TestIsFoeAlive(TestCase):
    def test_foe_is_alive(self):
        foe = {'HP': 1, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        actual = is_foe_alive(foe)
        self.assertTrue(actual)

    def test_foe_is_dead(self):
        foe = {'HP': 0, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}
        actual = is_foe_alive(foe)
        self.assertFalse(actual)
