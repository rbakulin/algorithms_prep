import unittest


def decode_string(s: str) -> str:
    """
    s="3[a2[c]]" -> "accaccacc"
    """
    stack = []
    for char in s:
        if char == "]":
            str_to_add = ""
            while stack and stack[-1] != "[":
                str_to_add += stack.pop()
            stack.pop()  # remove "["
            multiplier = stack.pop()  # the symbol before "[" is guaranteed multiplier (by task's description)
            while stack and stack[-1].isdigit():  # the multiplier could consist of several digits
                multiplier += stack.pop()
            str_to_add = int(multiplier[::-1]) * str_to_add[::-1]  # DON'T FORGET to reverse BOTH multiplier and string
            for add_char in str_to_add:
                stack.append(add_char)
        else:
            stack.append(char)
    return "".join(stack)


class TestDecodeString(unittest.TestCase):
    # def test_multiplier(self):
    #     self.assertEqual(decode_string(s="3[a]2[bc]"), "aaabcbc")

    def test_nested_multiplier(self):
        self.assertEqual(decode_string(s="3[a2[c]]"), "accaccacc")

    # def test_multiplier_with_suffix(self):
    #     self.assertEqual(decode_string(s="2[abc]3[cd]ef"), "abcabccdcdcdef")


if __name__ == "__main__":
    unittest.main()
