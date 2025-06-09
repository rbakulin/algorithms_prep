import unittest


def get_max_avg_subarray(nums: list[int], k: int) -> float:
    """
    [1, 12, -5, -6, 50, 3], 4, sum_k = 8
    sum_k = 2, avg = 0.5, max_avg = 0.5, sum_k = 1
    sum_k = 51, avg = 12.75, max_avg = 12.75, sum_k = 39
    sum_k = 42, avg = 10.5, max_avg = 12.75, sum_k = 48
    """
    i = 0
    j = k - 1
    max_avg = - float('inf')  # DON'T FORGET TO SET IT TO -INF (NOT TO 0!) TO UPDATE MAXIMUM NEGATIVE SUM CORRECTLY

    window_sum = sum(nums[i: j])
    while j < len(nums):
        window_sum += nums[j]
        avg = window_sum / k
        max_avg = max(avg, max_avg)
        window_sum -= nums[i]
        i += 1
        j += 1
    return max_avg


class TestGetMaxAvgSubarray(unittest.TestCase):
    def test_many_nums(self):
        self.assertEqual(get_max_avg_subarray([1, 12, -5, -6, 50, 3], 4), 12.75)

    def test_one_num(self):
        self.assertEqual(get_max_avg_subarray([5], 1), 5.00000)

    def test_one_num_negative(self):
        self.assertEqual(get_max_avg_subarray([-1], 1), -1.00000)


if __name__ == "__main__":
    unittest.main()
