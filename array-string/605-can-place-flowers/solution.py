import unittest


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    """
    [1, 0, 1] 3/2
    [1, 0, 1, 0] 4/2
    [1, 0, 1, 0, 1] 5/3
    [1, 0, 1, 0, 1, 0] 6/3
    [1, 0, 1, 0, 1, 0, 1] 7/4
    """
    if n == 0:
        return True
    length = len(flowerbed)
    if length % 2 == 0:  # if list length's even we can add as many 1's maximum as 0's
        if n > length / 2:
            return False
    elif length % 2 == 1:  # if list length's odd we can add as many 1's as in even list but + 1
        if n > int(length / 2 + 0.5):
            return False
    if length in (1, 2):
        return True if 1 not in flowerbed else False
    for i in range(length):
        if n == 0:
            return True
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif i == length - 1:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
        else:
            # DOUBLE CHECK EVERY CONDITION, YOU MADE STUPID MISTAKE WHEN FORGOT TO COMPARE WITH ZERO IN THE LAST ONE
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
    if n == 0:
        return True
    return False


class TestCanPlaceFlowers(unittest.TestCase):
    def test_can_place(self):
        self.assertEqual(can_place_flowers([1, 0, 0, 0, 1], 1), True)

    def test_can_not_place(self):
        self.assertEqual(can_place_flowers([1, 0, 0, 0, 1], 2), False)


if __name__ == "__main__":
    unittest.main()
