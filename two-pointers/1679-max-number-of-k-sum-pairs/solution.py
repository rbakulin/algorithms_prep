import unittest


def get_max_pairs_count_hashmap(nums: list[int], k: int) -> int:
    seen = {}
    count = 0
    for n in nums:
        diff = k - n
        if seen.get(diff, 0):  # ACCORDING TO PROBLEM'S CONDITION, THERE CAN NOT BE ANY ZEROS OR NEGATIVE NUMBERS
            count += 1
            seen[diff] -= 1
        else:
            seen[n] = seen.get(n, 0) + 1
    return count


def get_max_pairs_count_two_pointers(nums: list[int], k: int) -> int:
    pairs = 0
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] > k:
            j -= 1
        elif nums[i] + nums[j] < k:
            i += 1
        else:
            pairs += 1
            i += 1
            j -= 1
    return pairs


class TestGetMaxPairsCount(unittest.TestCase):
    def test_two_pairs_hashmap(self):
        self.assertEqual(get_max_pairs_count_hashmap([1, 2, 3, 4], 5), 2)

    def test_one_pair_hashmap(self):
        self.assertEqual(get_max_pairs_count_hashmap([3, 1, 3, 4, 3], 6), 1)

    def test_two_pairs_pointers(self):
        self.assertEqual(get_max_pairs_count_two_pointers([1, 2, 3, 4], 5), 2)

    def test_one_pair_pointers(self):
        self.assertEqual(get_max_pairs_count_two_pointers([3, 1, 3, 4, 3], 6), 1)


if __name__ == "__main__":
    unittest.main()
