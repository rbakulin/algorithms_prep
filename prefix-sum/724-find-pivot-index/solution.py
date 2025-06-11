import unittest


def get_pivot_index(nums: list[int]) -> int:
    """
    [1, 7, 3, 6, 5, 6]: [0, 1, 8, 11, 17, 23], [27, 20, 17, 11, 6, 0], 3
    [2, 1, -1]: [0, 2, 3], [0, -1, 0]
    """
    prefix_sums = [None] * len(nums)  # DON'T FORGET TO FILL WITH NONE TO AVOID LIST INDEX ERROR BELLOW
    current_sum_p = 0
    for i in range(len(nums)):
        prefix_sums[i] = current_sum_p
        current_sum_p += nums[i]

    suffix_sums = [None] * len(nums)
    current_sum_s = 0
    for j in range(len(nums) - 1, -1, -1):  # DON'T FORGET RO GO BACKWARDS HERE
        suffix_sums[j] = current_sum_s
        current_sum_s += nums[j]

    pivot_index = -1
    for x in range(len(nums)):
        if prefix_sums[x] == suffix_sums[x]:
            pivot_index = x
            break  # DON'T FORGET RETURN OR BREAK! OTHERWISE, WE'LL REWRITE THE INDEX FOR BIGGER ONE
    return pivot_index


class TestGetPivotIndex(unittest.TestCase):
    def test_pivot_index_centered(self):
        self.assertEqual(get_pivot_index([1, 7, 3, 6, 5, 6]), 3)

    def test_no_pivot_index(self):
        self.assertEqual(get_pivot_index([1, 2, 3]), -1)

    def test_pivot_index_is_first(self):
        self.assertEqual(get_pivot_index([2, 1, -1]), 0)

    def test_left_index_first(self):
        self.assertEqual(get_pivot_index([-1, -1, 0, 0, -1, -1]), 2)


if __name__ == "__main__":
    unittest.main()
