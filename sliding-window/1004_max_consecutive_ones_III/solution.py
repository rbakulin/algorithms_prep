import unittest


def get_max_count_ones_with_flip(nums: list[int], k: int) -> int:
    """
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2 = 6
    [0, 0, 1], 1 = 2
    """
    max_line_len = 0
    i, j = 0, 0
    zeros_met = 0
    while j < len(nums):  # just move j forward till the end
        if nums[j] == 0:  # count 0 that we met
            zeros_met += 1
        while zeros_met > k:  # if too many 0, we have to move i till we get rid of one 0
            if nums[i] == 0:
                zeros_met -= 1  # got rid of one 0 in the window -> zeros_met == k -> valid window
            i += 1
        current_line_len = j - i + 1  # i, j - indexes (start with 0), but we need length (starts with 1)
        max_line_len = max(max_line_len, current_line_len)
        j += 1  # IF USE WHILE, DO NOT FORGET TO INCREASE MANUALLY!
    return max_line_len


class TestGetMaxCountOnesWithFlip(unittest.TestCase):
    def test_two_flips(self):
        self.assertEqual(get_max_count_ones_with_flip([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)

    def test_three_flips(self):
        self.assertEqual(get_max_count_ones_with_flip([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),
                         10)


if __name__ == "__main__":
    unittest.main()
