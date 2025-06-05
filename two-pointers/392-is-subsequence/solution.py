import unittest


def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True
    i = 0
    chars_to_match = len(s)
    for j in range(len(t)):
        if t[j] == s[i]:
            chars_to_match -= 1
            i += 1
        if chars_to_match == 0:
            return True
    return False


class TestIsSubsequence(unittest.TestCase):
    def test_true(self):
        self.assertEqual(is_subsequence("abc", "ahbgdc"), True)

    def test_false(self):
        self.assertEqual(is_subsequence("axc", "ahbgdc"), False)

    def test_true_s_empty(self):
        self.assertEqual(is_subsequence("", "ahbgdc"), True)

    def test_false_t_empty(self):
        self.assertEqual(is_subsequence("abc", ""), False)


if __name__ == "__main__":
    unittest.main()
