from unittest import TestCase
from unittest.mock import patch
from game import make_board


@patch('random.choice', side_effect=['You found a tavern'])
class TestMakeBoard(TestCase):
    def test_make_board_with_one_description(self, mock_choice):
        actual = make_board(10, 10)
        expected = {(0, 0): 'You found a tavern', (0, 1): 'You found a tavern', (0, 2): 'You found a tavern', (0, 3):
                    'You found a tavern', (0, 4): 'You found a tavern', (0, 5): 'You found a tavern',
                    (0, 6): 'You found a tavern', (0, 7): 'You found a tavern', (0, 8): 'You found a tavern',
                    (0, 9): 'You found a tavern', (1, 0): 'You found a tavern', (1, 1): 'You found a tavern',
                    (1, 2): 'You found a tavern', (1, 3): 'You found a tavern', (1, 4): 'You found a tavern',
                    (1, 5): 'You found a tavern', (1, 6): 'You found a tavern', (1, 7): 'You found a tavern',
                    (1, 8): 'You found a tavern', (1, 9): 'You found a tavern', (2, 0): 'You found a tavern',
                    (2, 1): 'You found a tavern', (2, 2): 'You found a tavern', (2, 3): 'You found a tavern',
                    (2, 4): 'You found a tavern', (2, 5): 'You found a tavern', (2, 6): 'You found a tavern',
                    (2, 7): 'You found a tavern', (2, 8): 'You found a tavern', (2, 9): 'You found a tavern',
                    (3, 0): 'You found a tavern', (3, 1): 'You found a tavern', (3, 2): 'You found a tavern',
                    (3, 3): 'You found a tavern', (3, 4): 'You found a tavern', (3, 5): 'You found a tavern',
                    (3, 6): 'You found a tavern', (3, 7): 'You found a tavern', (3, 8): 'You found a tavern',
                    (3, 9): 'You found a tavern', (4, 0): 'You found a tavern', (4, 1): 'You found a tavern',
                    (4, 2): 'You found a tavern', (4, 3): 'You found a tavern', (4, 4): 'You found a tavern',
                    (4, 5): 'You found a tavern', (4, 6): 'You found a tavern', (4, 7): 'You found a tavern',
                    (4, 8): 'You found a tavern', (4, 9): 'You found a tavern', (5, 0): 'You found a tavern',
                    (5, 1): 'You found a tavern', (5, 2): 'You found a tavern', (5, 3): 'You found a tavern',
                    (5, 4): 'You found a tavern', (5, 5): 'You found a tavern', (5, 6): 'You found a tavern',
                    (5, 7): 'You found a tavern', (5, 8): 'You found a tavern', (5, 9): 'You found a tavern',
                    (6, 0): 'You found a tavern', (6, 1): 'You found a tavern', (6, 2): 'You found a tavern',
                    (6, 3): 'You found a tavern', (6, 4): 'You found a tavern', (6, 5): 'You found a tavern',
                    (6, 6): 'You found a tavern', (6, 7): 'You found a tavern', (6, 8): 'You found a tavern',
                    (6, 9): 'You found a tavern', (7, 0): 'You found a tavern', (7, 1): 'You found a tavern',
                    (7, 2): 'You found a tavern', (7, 3): 'You found a tavern', (7, 4): 'You found a tavern',
                    (7, 5): 'You found a tavern', (7, 6): 'You found a tavern', (7, 7): 'You found a tavern',
                    (7, 8): 'You found a tavern', (7, 9): 'You found a tavern', (8, 0): 'You found a tavern',
                    (8, 1): 'You found a tavern', (8, 2): 'You found a tavern', (8, 3): 'You found a tavern',
                    (8, 4): 'You found a tavern', (8, 5): 'You found a tavern', (8, 6): 'You found a tavern',
                    (8, 7): 'You found a tavern', (8, 8): 'You found a tavern', (8, 9): 'You found a tavern',
                    (9, 0): 'You found a tavern', (9, 1): 'You found a tavern', (9, 2): 'You found a tavern',
                    (9, 3): 'You found a tavern', (9, 4): 'You found a tavern', (9, 5): 'You found a tavern',
                    (9, 6): 'You found a tavern', (9, 7): 'You found a tavern', (9, 8): 'You found a tavern',
                    (9, 9): 'You found a tavern'}
        self.assertEqual(actual, expected)
