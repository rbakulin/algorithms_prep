import unittest


def is_there_triplet(nums: list[int]) -> bool:
    """
    [20, 100, 10, 112, 5, 13]
    1. first = 20, second = -inf
    2. first = 20, second = 100
    3. first = 10, second = 100
    4. first = 10, second = 100
    5. first = 10 (used to be 20, but updated value is obviously smaller, so it doesn't affect correctness),
    second = 100, third = 112 -> TRUE
    """
    first, second = float('inf'), float('inf')
    for n in nums:
        if n <= first:  # CAUTION! IN CASE ALL ELEMENTS ARE EQUAL WE MUSTN'T RETURN TRUE ON THE THIRD EQUAL ELEMENT!
            first = n   # So, that's why we compare LESS OR EQUAL
        elif n <= second:
            second = n
        else:
            return True
    return False


class TestIsThereTriplet(unittest.TestCase):
    def test_true_simple(self):
        self.assertEqual(is_there_triplet([1, 2, 3, 4, 5]), True)

    def test_true_separate(self):
        self.assertEqual(is_there_triplet([2, 1, 5, 0, 4, 6]), True)

    def test_true_separate_and_triplet_smaller_than_first_numbers(self):
        self.assertEqual(is_there_triplet([20, 100, 10, 12, 5, 13]), True)

    def test_false(self):
        self.assertEqual(is_there_triplet([5, 4, 3, 2, 1]), False)

    def test_false_all_equal(self):
        self.assertEqual(is_there_triplet([1, 1, 1, 1]), False)


if __name__ == "__main__":
    unittest.main()

