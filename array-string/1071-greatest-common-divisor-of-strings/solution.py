import unittest


def get_str_gcd(s: str, t: str) -> str:
    def _get_gcd(i: int, j: int) -> int:
        i, j = j, i % j  # Euclidean algorithm
        if j == 0:
            return i
        else:
            return _get_gcd(i, j)
    if s + t != t + s:
        return ''
    return t[:_get_gcd(len(s), len(t))]  # it's ok that slice does -1 of GCD val - we want as many chars as GCD val


class TestGetStrGcd(unittest.TestCase):
    def test_substring_twice(self):
        self.assertEqual(get_str_gcd("ABCABC", "ABC"), "ABC")

    def test_less_than_substring(self):
        self.assertEqual(get_str_gcd("ABABAB", "ABAB"), "AB")

    def test_not_substring(self):
        self.assertEqual(get_str_gcd("LEET", "CODE"), "")


if __name__ == "__main__":
    unittest.main()

