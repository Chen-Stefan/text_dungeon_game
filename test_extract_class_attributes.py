from unittest import TestCase
from game import extract_class_attributes
from game import create_classes
from game import confusion
from game import terror


class TestExtractClassAttributes(TestCase):

    def test_extract_sorcerer_attributes(self):
        classes_info = create_classes()
        actual = extract_class_attributes(classes_info, '2')
        expected = {'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'), 'max_HP': (100, 120, 150),
                    'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5,
                    'special_attack': confusion, 'special_attack_name': 'Confusion'}
        self.assertEqual(expected, actual)

    def test_extract_thief_attributes(self):
        classes_info = create_classes()
        actual = extract_class_attributes(classes_info, '4')
        expected = {'class name': 'Thief', 'class levels': ('Bandit', 'Assassin', 'Night Lord'),
                    'max_HP': (100, 130, 160), 'levelup_XP': (100, 150), 'max_damage': (20, 30, 40), 'accuracy': 0.9,
                    'special_attack': terror, 'special_attack_name': 'Terror'}
        self.assertEqual(expected, actual)
