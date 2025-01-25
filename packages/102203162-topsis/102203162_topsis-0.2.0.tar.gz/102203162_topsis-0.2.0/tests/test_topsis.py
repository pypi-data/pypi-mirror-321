import unittest
from topsis.topsis import topsis

class TestTopsis(unittest.TestCase):
    def test_topsis(self):
        data = [[250, 16, 12, 5],
                [200, 16, 8, 3],
                [300, 32, 16, 4],
                [275, 32, 8, 4],
                [225, 16, 16, 2]]
        weights = [0.25, 0.25, 0.25, 0.25]
        impacts = ['+', '+', '-', '+']
        rankings, _ = topsis(data, weights, impacts)
        self.assertEqual(rankings.tolist(), [3, 1, 4, 2, 5])

if __name__ == '__main__':
    unittest.main()
