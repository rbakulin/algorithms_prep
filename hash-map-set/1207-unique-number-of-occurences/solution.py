import unittest


def is_each_char_occurs_unique_times(arr: list[int]) -> bool:
    """
    THINGS TO REMEMBER in our case:
    1. to check if all values are unique, comparing lengths with a set is enough!
    E.g. we don't need to convert both of arrays to the list before comparing them - it would be incorrect, because
    in a list order MATTERS, however dict_values -> set -> list -> order is BROKEN
    2. len() works with dict.keys() correctly -> we DON'T need to convert it to anything either
    """
    popularity = {}
    for n in arr:
        popularity[n] = popularity.get(n, 0) + 1
    return len(popularity.values()) == len(set(popularity.values()))


class TestIsEachCharOccursUniqueTimes(unittest.TestCase):
    def test_true_only_positives(self):
        self.assertEqual(is_each_char_occurs_unique_times([1, 2, 2, 1, 1, 3]), True)

    def test_true_with_negatives(self):
        self.assertEqual(is_each_char_occurs_unique_times([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]), True)

    def test_false(self):
        self.assertEqual(is_each_char_occurs_unique_times([1, 2]), False)


if __name__ == "__main__":
    unittest.main()
