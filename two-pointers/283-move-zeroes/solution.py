import unittest


def move_zeros(nums: list[int]) -> None:
    """
    [0, 1, 0, 3, 12]
    [1, 1, 0, 3, 12]
    [1, 3, 0, 3, 12]
    [1, 3, 12, 3, 12]
    [1, 3, 12, 0, 0]
    """
    write = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write] = nums[i]
            write += 1
        i += 1
    for j in range(write, len(nums)):
        nums[j] = 0
        j += 1


class MoveZeros(unittest.TestCase):
    def test_many_nums(self):
        array = [0, 1, 0, 3, 12]
        move_zeros(array)
        self.assertEqual(array, [1, 3, 12, 0, 0])

    def test_one_num(self):
        array = [0]
        move_zeros(array)
        self.assertEqual(array, [0])


if __name__ == "__main__":
    unittest.main()
