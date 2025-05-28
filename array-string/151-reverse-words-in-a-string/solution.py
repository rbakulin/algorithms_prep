import unittest


def reverse_words(s: str) -> str:
    result = []
    i = 0  # we need second index only for getting rid of leading spaces
    j = len(s) - 1
    while i <= j:  # DON'T FORGET "=": we're adding chars to the new array -> we need to add every char, including s[i]
        if j == len(s) - 1:  # getting rid of trailing spaces
            while i <= j and s[j] == ' ':
                j -= 1
        if i == 0:  # getting rid of leading spaces
            while i <= j and s[i] == ' ':
                i += 1
        if s[j] == ' ':  # adding one space, getting rid of extra spaces
            result.append(s[j])
            j -= 1
            while i <= j and s[j] == " ":
                j -= 1
        else:
            word = ''  # we need to add the words in reversed order, but the word itself should be in straight order
            while i <= j and s[j] != ' ':
                word += s[j]
                j -= 1
            result.append(word[::-1])
    return ''.join(result)


class TestReverseWords(unittest.TestCase):
    def test_usual_reverse(self):
        self.assertEqual(reverse_words("the sky is blue"), "blue is sky the")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(reverse_words("  hello world  "), "world hello")

    def test_double_space(self):
        self.assertEqual(reverse_words("a good   example"), "example good a")


if __name__ == "__main__":
    unittest.main()

