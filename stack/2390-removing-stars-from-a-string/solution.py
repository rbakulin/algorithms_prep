import unittest


def remove_stars(s: str) -> str:
    """
    "leet**cod*e" -> "lecoe"
    """
    result = []  # be careful - using a list to operate with chars, not a string
    for char in s:
        if char == "*":
            result.pop()
        else:
            result.append(char)
    return "".join(result)


class TestRemoveStars(unittest.TestCase):
    def test_chars_left(self):
        self.assertEqual(remove_stars(s="leet**cod*e"), "lecoe")

    def test_erase_str(self):
        self.assertEqual(remove_stars(s="erase*****"), "")


if __name__ == "__main__":
    unittest.main()
