import unittest


def get_max_square(height: list[int]) -> int:
    max_square = - float('inf')
    i = 0
    j = len(height) - 1
    while i < j:
        length = j - i  # these are indexes, so we don't need to do -1
        if height[i] >= height[j]:
            square = height[j] * length  # CALCULATE THE SQUARE WITH THE LOWER VALUE (by the problem's condition)
            j -= 1  # TRY TO FIND A BIGGER VALUE INSTEAD OF THE CURRENT SMALLEST TO INCREASE TO SQUARE
        else:
            square = height[i] * length
            i += 1
        if square > max_square:
            max_square = square
    return max_square


class TestGetMaxSquare(unittest.TestCase):
    def test_many_nums(self):
        self.assertEqual(get_max_square([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_two_nums(self):
        self.assertEqual(get_max_square([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
