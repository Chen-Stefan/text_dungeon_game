from unittest import TestCase
from game import modify_foe_hp


class TestModifyFoeHp(TestCase):
    def test_modify_foe_hp(self):
        foe = {'HP': 80, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60}
        damage_to_foe = 30
        modify_foe_hp(foe, damage_to_foe)
        self.assertEqual({'HP': 50, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60}, foe)
