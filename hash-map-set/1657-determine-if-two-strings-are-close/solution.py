import unittest


def are_strings_close(word1: str, word2: str) -> bool:
    """
    word1 = "cabbba", word2 = "abbccc", true
    ("c": 1, "a": 2, "b": 3), ("a": 1, "b": 2, "c": 3)
    """
    popularity1 = {}
    for c1 in word1:
        popularity1[c1] = popularity1.get(c1, 0) + 1
    popularity2 = {}
    for c2 in word2:
        popularity2[c2] = popularity2.get(c2, 0) + 1
    if set(popularity1.keys()) != set(popularity2.keys()):  # DON'T FORGET to check, that the same set of chars is used
        return False
    # REMEMBER: sort() changes the array and returns None, that's why we're using sorted() instead
    return sorted(list(popularity1.values())) == sorted(list(popularity2.values()))


class TestAreStringsClose(unittest.TestCase):
    def test_true_via_swapping(self):
        self.assertEqual(are_strings_close(word1="abc", word2="bca"), True)

    def test_false(self):
        self.assertEqual(are_strings_close(word1="a", word2="aa"), False)

    def test_true_via_swapping_and_inverting(self):
        self.assertEqual(are_strings_close(word1="cabbba", word2="abbccc"), True)

    def test_false_different_chars(self):
        self.assertEqual(are_strings_close(word1="uau", word2="ssx"), False)


if __name__ == "__main__":
    unittest.main()
