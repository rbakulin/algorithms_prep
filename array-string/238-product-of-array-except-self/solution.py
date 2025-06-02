import unittest


def get_product_except_i(nums: list[int]) -> list[int]:
    """
    given: [1, 2, 3, 4]
    prefix: [1, 1, 2, 6]
    suffix: [24, 12 , 4, 1]
    result: [24, 12, 8, 6]

    given: [-1, 1, 0, -3, 3]
    prefix: [1, -1, -1, 0, 0]
    suffix: [0, 0, -9, 3, 1]
    result: [0, 0, 9, 0, 0]
    """
    n = len(nums)
    prefix_prods = [0] * n  # WARNING! NOT [0 * len(nums)]
    cur_prefix_prod = 1
    for i in range(n):
        prefix_prods[i] = cur_prefix_prod
        cur_prefix_prod *= nums[i]
    suffix_prods = [0] * n
    cur_suffix_prod = 1
    for j in range(n - 1, -1, -1):
        suffix_prods[j] = cur_suffix_prod
        cur_suffix_prod *= nums[j]
    result = [0] * n
    for i in range(n):
        result[i] = prefix_prods[i] * suffix_prods[i]
    return result


def get_product_except_i_space_opt(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n  # doesn't count as extra space (problem condition)
    cur_prefix_prod = 1
    for i in range(n):
        result[i] = cur_prefix_prod
        cur_prefix_prod *= nums[i]
    cur_suffix_prod = 1
    for j in range(n - 1, -1, -1):
        result[j] = result[j] * cur_suffix_prod
        cur_suffix_prod *= nums[j]
    return result


class TestGetProductExceptI(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(get_product_except_i([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_zero(self):
        self.assertEqual(get_product_except_i([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_positive_opt(self):
        self.assertEqual(get_product_except_i_space_opt([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_zero_opt(self):
        self.assertEqual(get_product_except_i_space_opt([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


if __name__ == "__main__":
    unittest.main()

