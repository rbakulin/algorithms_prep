import unittest


def collide_asteroids(asteroids: list[int]) -> list[int]:
    """
    [5, 10, -5] -> [5, 10]
    [-9, 7]) -> [-9, 7]
    [5, 6, -10] -> [-10]
    [-2, -1, 1, 2] -> [-2, -1, 1, 2]
    """
    result = []
    for asteroid in asteroids:
        # this is the condition for starting simulating a collision
        # REMEMBER! we collide ONLY if:
        # 1. current asteroid is negative (moving left)
        # 2. there's something to collide with (the stack is not empty)
        # 3. asteroid, that collides (last in the stack) with the current asteroid is positive (moving right)
        while result and result[-1] > 0 and asteroid < 0:  # DON'T FORGET about result[-1] > 0 condition!!!
            if asteroid * -1 > result[-1]:
                result.pop()
            elif asteroid * -1 == result[-1]:
                result.pop()
                break  # if current asteroid is equal to the last one of the stack, WE DON'T ADD IT TO THE STACK
            else:
                break  # the same if current asteroid is smaller
        # this condition works only if while above ends naturally (NOT WITH BREAK)
        # it means that the current asteroid survived OR it DOESN'T fall under collision condition at all
        else:
            result.append(asteroid)
    return result


class TestCollideAsteroids(unittest.TestCase):
    def test_positive_left(self):
        self.assertEqual(collide_asteroids(asteroids=[5, 10, -5]), [5, 10])

    def test_negative_left(self):
        self.assertEqual(collide_asteroids(asteroids=[5, 6, -10]), [-10])

    def test_no_asteroids_left(self):
        self.assertEqual(collide_asteroids(asteroids=[8, -8]), [])

    def test_no_collision(self):
        self.assertEqual(collide_asteroids(asteroids=[-9, 7]), [-9, 7])

    def test_no_collision_many(self):
        self.assertEqual(collide_asteroids(asteroids=[-2, -1, 1, 2]), [-2, -1, 1, 2])


if __name__ == "__main__":
    unittest.main()
