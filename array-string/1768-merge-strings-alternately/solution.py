import unittest


def merge_alternately(word1: str, word2: str) -> str:
    result = ''
    max_len = max(len(word1), len(word2))
    for i in range(max_len):
        if i > len(word1) - 1:
            result += word2[i]
        elif i > len(word2) - 1:
            result += word1[i]
        else:  # DO NOT FORGET TO USE MAX INDEX ONLY IN "ELSE"!
            result += word1[i] + word2[i]
    return result


class TestMergeAlternately(unittest.TestCase):
    def test_equal_length(self):
        self.assertEqual(merge_alternately("abc", "pqr"), "apbqcr")

    def test_first_longer(self):
        self.assertEqual(merge_alternately("ab", "pqrs"), "apbqrs")

    def test_second_longer(self):
        self.assertEqual(merge_alternately("abcd", "pq"), "apbqcd")


if __name__ == "__main__":
    unittest.main()

