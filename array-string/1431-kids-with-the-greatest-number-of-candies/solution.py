import unittest


def is_greatest_after_extra(candies: list[int], extra_candies: int) -> list[bool]:
    max_candies = max(candies)
    result = []
    for candy in candies:
        if candy + extra_candies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result


class TestIsGreatestAfterExtra(unittest.TestCase):
    def test_one_false(self):
        self.assertEqual(is_greatest_after_extra([2, 3, 5, 1, 3], 3), [True, True, True, False, True])

    def test_one_true(self):
        self.assertEqual(is_greatest_after_extra([4, 2, 1, 1, 2], 1), [True, False, False, False, False])

    def test_one_false_short(self):
        self.assertEqual(is_greatest_after_extra([12, 1, 12], 10), [True, False, True])


if __name__ == "__main__":
    unittest.main()

