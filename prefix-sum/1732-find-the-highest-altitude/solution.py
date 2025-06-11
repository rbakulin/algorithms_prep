import unittest


def get_highest_altitude(gain: list[int]) -> int:
    """
    [-5, 1, 5, 0, -7], 1
    -5, -5
    -4, -4
    1, 1
    1, 1
    -6, 1
    """
    max_alt = 0  # NOT -inf, cause the start point (0) is also counted as one of the altitudes
    current_alt = 0
    for g in gain:
        current_alt += g
        max_alt = max(current_alt, max_alt)
    return max_alt


class TestGetHighestAltitude(unittest.TestCase):
    def test_positive_altitude(self):
        self.assertEqual(get_highest_altitude([-5, 1, 5, 0, -7]), 1)

    def test_zero_altitude(self):
        self.assertEqual(get_highest_altitude([-4, -3, -2, -1, 4, 3, 2]), 0)


if __name__ == "__main__":
    unittest.main()
