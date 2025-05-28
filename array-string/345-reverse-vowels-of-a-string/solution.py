import unittest


def reverse_vowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    result = list(s)  # !!! no need to fill the list with Nones
    i = 0
    j = len(s) - 1
    while i < j:  # if result is filled with corresponding chars (but not Nones), there's no need to go to i == j step
        while i < j and result[i] not in vowels:  # DO NOT FORGET TO CHECK i < j IN THE INSIDE LOOP ALSO
            i += 1
        while i < j and result[j] not in vowels:
            j -= 1
        result[i], result[j] = result[j], result[i]
        i += 1  # !!! DO NOT FORGET TO MOVE INDEXES AFTER WE FOUND TWO VOWELS
        j -= 1
    return ''.join(result)


class TestReverseVowels(unittest.TestCase):
    def test_ice_cream(self):
        self.assertEqual(reverse_vowels("IceCreAm"), "AceCreIm")

    def test_leetcode(self):
        self.assertEqual(reverse_vowels("leetcode"), "leotcede")

    def test_space(self):
        self.assertEqual(reverse_vowels(" "), " ")

    def test_no_vowels(self):
        self.assertEqual(reverse_vowels(".,"), ".,")


if __name__ == "__main__":
    unittest.main()

