import unittest


def compress(chars: list[str]) -> int:
    """
    ["a", "a", "b", "b", "c", "c", "c"]
    """
    s = ''
    i = 0
    while i < len(chars):
        char = chars[i]
        count = 0  # it's easier to start from the char itself in the inside loop ↓
        while i < len(chars) and chars[i] == char:
            count += 1
            i += 1  # don't forget to also move the main index
        s += char  # we DON'T need to add counter if the char is not multiply
        if count > 1:
            s += str(count)
    chars.clear()  # NOT char = []
    chars += list(s)
    return len(s)


def compress_space_optimized(chars: list[str]) -> int:
    write = 0  # increases only after writing a char
    i = 0
    while i < len(chars):
        char = chars[i]
        count = 0
        while i < len(chars) and chars[i] == char:
            count += 1
            i += 1
        chars[write] = char
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write


class TestCompress(unittest.TestCase):
    def test_three_chars(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        self.assertEqual(compress(chars), 6)
        self.assertEqual(chars, ["a", "2", "b", "2", "c", "3"])

    def test_one_char(self):
        chars = ["a"]
        self.assertEqual(compress(chars), 1)
        self.assertEqual(chars, ["a"])

    def test_two_chars(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.assertEqual(compress(chars), 4)
        self.assertEqual(chars, ["a", "b", "1", "2"])

    # TEST OPTIMIZED FUNCTION
    def test_three_chars_optimized(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        result_length = compress_space_optimized(chars)
        self.assertEqual(result_length, 6)
        self.assertEqual(chars[:result_length], ["a", "2", "b", "2", "c", "3"])

    def test_one_char_optimized(self):
        chars = ["a"]
        result_length = compress_space_optimized(chars)
        self.assertEqual(result_length, 1)
        self.assertEqual(chars[:result_length], ["a"])

    def test_two_chars_optimized(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        result_length = compress_space_optimized(chars)
        self.assertEqual(result_length, 4)
        self.assertEqual(chars[:result_length], ["a", "b", "1", "2"])


if __name__ == "__main__":
    unittest.main()
