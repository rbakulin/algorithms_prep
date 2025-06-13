import unittest


# The simplest yet the most resource-demanding solution (n vertical -> n horizontal -> n elements to compare -> 0(n^3))
def get_number_of_equal_pairs(grid: list[list[int]]) -> int:
    """
    grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1
    vertical=[[3, 1, 2], [2, 7, 7], [1, 6, 7]]
    """
    equal = 0
    n = len(grid)
    column_grid = []
    for i in range(n):  # index to use in all 3 lines
        column = []  # one column = one array
        for line in grid:  # going through all the lines and take 1 element from each WITH OUR GENERAL INDEX
            column.append(line[i])
        column_grid.append(column)
    for horizontal in grid:
        for vertical in column_grid:
            if vertical == horizontal:  # inefficient - need to check all n element in each line
                equal += 1
    return equal


# pretty much the same algorithm, but we keep lines in dict instead of list -> counting is O(n^2) now
def get_number_of_equal_pairs_optimized(grid: list[list[int]]) -> int:
    """
    grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1
    horizontal={(3, 2, 1): 1, (1, 7, 6): 1, (2, 7, 7): 1}
    """
    equal = 0
    n = len(grid)
    horizontal = {}  # again keep HORIZ and VERT lines SEPARATE - we're counting only intersections between THEM
    for line in grid:
        # converting to tuple only to be able to make it a key in the dict
        horizontal[tuple(line)] = horizontal.get(tuple(line), 0) + 1
    for i in range(n):
        column = []
        for line in grid:
            column.append(line[i])
        # we don't store vertical lines in a separate dict - it makes the counting of intersections more difficult
        # instead we can check each line in horizontal dict right after it was formed
        if horizontal.get(tuple(column)):
            equal += horizontal[tuple(column)]  # DON'T FORGET: there could be MORE than 1 horiz line! (DON'T DO +1)
    return equal


class TestGetNumberOfEqualPairs(unittest.TestCase):
    def test_3_x_3_matrix(self):
        self.assertEqual(get_number_of_equal_pairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]), 1)

    def test_4_x_4_matrix(self):
        self.assertEqual(get_number_of_equal_pairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]), 3)

    def test_3_x_3_matrix_optimized(self):
        self.assertEqual(get_number_of_equal_pairs_optimized(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]), 1)

    def test_4_x_4_matrix_optimized(self):
        self.assertEqual(get_number_of_equal_pairs_optimized(
            grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]), 3)


if __name__ == "__main__":
    unittest.main()
