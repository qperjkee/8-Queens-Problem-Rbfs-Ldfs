import unittest, time
from unittest.mock import patch
from main import find_wrong_spots, count_conflicts, generate_random_queens_positions, get_size, get_depth, get_decision, is_solution, find_child_states, find_successors, ldfs, rbfs_nqueens

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.conflicts = count_conflicts(state)

class TestQueensFunctions(unittest.TestCase):

    def test_find_wrong_spots(self):
        self.assertEqual(find_wrong_spots([5, 2, 2, 4, 7, 0, 1, 1]), [5, 0, 2, 4, 1])
        self.assertEqual(find_wrong_spots([3, 1, 7, 5, 0, 2, 4, 6]), [])
        self.assertEqual(find_wrong_spots([6, 2, 7, 7, 0, 2, 4, 5]), [2, 7, 4, 5])

    def test_count_conflicts(self):
        self.assertEqual(count_conflicts([5, 2, 2, 4, 7, 0, 1, 1]), 6)
        self.assertEqual(count_conflicts([3, 1, 7, 5, 0, 2, 4, 6]), 0)
        self.assertEqual(count_conflicts([6, 2, 7, 7, 0, 2, 4, 5]), 4)
    
    def test_generate_random_queens_positions(self):
        size = 8
        positions = generate_random_queens_positions(size)
        self.assertEqual(len(positions), size)
        for position in positions:
            self.assertTrue(0 <= position < size)
    
    def test_is_solution_true(self):
        node = Node([3, 1, 7, 5, 0, 2, 4, 6])
        self.assertTrue(is_solution(node))

    def test_is_solution_false(self):
        node = Node([6, 2, 7, 7, 0, 2, 4, 5])
        self.assertFalse(is_solution(node))
    
    def test_find_child_states(self):
        queens_positions = [0, 1, 2]
        child_states = find_child_states(queens_positions)
        expected_child_states = [
            [1, 1, 2],
            [2, 1, 2],
            [0, 0, 2],
            [0, 2, 2],
            [0, 1, 0],
            [0, 1, 1]
        ]
        self.assertEqual(child_states, expected_child_states)
    
    def test_ldfs_solution(self):
        node = Node([0, 1, 2, 1])
        start_time = time.time()
        result = ldfs(node, 0, 4, node, start_time)
        self.assertIsNotNone(result)
        self.assertTrue(is_solution(Node(result)))
    
    def test_find_successors(self):
        node = Node([0, 1, 2])
        successors = find_successors(node)
        self.assertEqual(len(set(successors)), len(successors))
    
    def test_rbfs_nqueens_solution(self):
        queens_positions = [0, 2, 4, 1, 3, 4, 5, 7]
        result = rbfs_nqueens(queens_positions)
        self.assertTrue(result)
        self.assertTrue(is_solution(Node(queens_positions)))
    
    @patch("builtins.input", side_effect=["3", "9", "10", "8"])
    def test_get_size_valid_input(self, mock_input):
        size = get_size()
        self.assertEqual(size, 8)

    @patch("builtins.input", side_effect=["-2", "22", "dd", "2"])
    def test_get_depth_valid_input(self, mock_input):
        depth = get_depth(8)
        self.assertEqual(depth, 2)
    
    @patch("builtins.input", side_effect=["2"])
    def test_get_decision_valid_input(self, mock_input):
        depth = get_decision()
        self.assertEqual(depth, 2)
    
    @patch("builtins.input", side_effect=["dsa"])
    def test_get_decision_invalid_input(self, mock_input):
        depth = get_decision()
        self.assertEqual(depth, 0)

if __name__ == '__main__':
    unittest.main()