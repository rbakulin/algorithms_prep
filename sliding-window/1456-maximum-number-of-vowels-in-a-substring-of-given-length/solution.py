import unittest


def get_max_vowels_in_substring(s: str, k: int) -> int:
    """
    s="abciiidef", k=3
    current_vowels = 1, max_vowels = 1, current_vowels = 0, i = 1, j = 3
    current_vowels = 1, max_vowels = 1, current_vowels = 1, i = 2, j = 4
    current_vowels = 2, max_vowels = 2, current_vowels = 2, i = 3, j = 5
    current_vowels = 3, max_vowels = 3, current_vowels = 2, i = 4, j = 6
    current_vowels = 2, max_vowels = 3, current_vowels = 1, i = 4, j = 6
    """
    vowels = set('aeiou')
    max_vowels = 0
    current_vowels = 0
    for t in range(k - 1):  # want to repeat same thing for every i, j in while ↓ - count till k -1 (range also does -1)
        if s[t] in vowels:
            current_vowels += 1
    i = 0
    j = k - 1
    while j < len(s):
        if s[j] in vowels:
            current_vowels += 1
        max_vowels = max(current_vowels, max_vowels)
        if s[i] in vowels:
            current_vowels -= 1
        i += 1
        j += 1
    return max_vowels


class TestGetMaxVowelsInSubstring(unittest.TestCase):
    def test_k_equals_vowels(self):
        self.assertEqual(get_max_vowels_in_substring(s="abciiidef", k=3), 3)

    def test_k_fewer_than_vowels(self):
        self.assertEqual(get_max_vowels_in_substring(s="aeiou", k=2), 2)

    def test_k_more_than_vowels(self):
        self.assertEqual(get_max_vowels_in_substring(s="leetcode", k=3), 2)


if __name__ == "__main__":
    unittest.main()
