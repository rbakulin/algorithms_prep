import unittest


def get_max_ones_after_deletion(nums: list[int]) -> int:
    """
    [1, 1, 0, 1], 3
    """
    i, j = 0, 0
    zeros_met = 0
    max_line = 0
    while j < len(nums):
        if nums[j] == 0:
            zeros_met += 1
        while zeros_met > 1:
            if nums[i] == 0:
                zeros_met -= 1
            i += 1
        current_line = j - i + 1
        max_line = max(max_line, current_line)
        j += 1
    max_line -= 1  # we always have to "delete" one char: whether it's 0 or 1
    return max_line


class TestGetMaxOnesAfterDeletion(unittest.TestCase):
    def test_small_array(self):
        self.assertEqual(get_max_ones_after_deletion([1, 1, 0, 1]), 3)

    def test_big_array(self):
        self.assertEqual(get_max_ones_after_deletion([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)

    def test_delete_one(self):
        self.assertEqual(get_max_ones_after_deletion([1, 1, 1]), 2)


if __name__ == "__main__":
    unittest.main()
