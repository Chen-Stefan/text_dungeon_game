from unittest import TestCase
from game import confusion


class TestConfusion(TestCase):

    def test_confusion_reduce_foe_accuracy(self):
        character = {'name': 'Joker', 'level': 3, 'Current HP': 150, 'Current XP': 0, 'X-coordinate': 0,
                     'Y-coordinate': 6, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'),
                     'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                     'special_attack': confusion, 'special_attack_name': 'Confusion'}
        foe = {'HP': 80, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60}
        foe_type = 'Death maiden'
        confusion(character, foe, foe_type)
        self.assertEqual({'HP': 80, 'max_damage': 20, 'accuracy': 0.7 / 2, 'XP': 60}, foe)
