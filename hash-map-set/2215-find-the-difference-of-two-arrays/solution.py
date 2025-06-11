import unittest


def get_list_diff(nums1: list[int], nums2: list[int]) -> list[list[int], list[int]]:
    distinct_nums1 = set(nums1)
    distinct_nums2 = set(nums2)
    result1 = [n1 for n1 in distinct_nums1 if n1 not in distinct_nums2]
    result2 = [n2 for n2 in distinct_nums2 if n2 not in distinct_nums1]
    return [result1, result2]


class TestGetListDiff(unittest.TestCase):
    def test_both_have_unique(self):
        self.assertEqual(get_list_diff(nums1=[1, 2, 3], nums2=[2, 4, 6]), [[1, 3], [4, 6]])

    def test_one_has_unique(self):
        self.assertEqual(get_list_diff(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]), [[3], []])


if __name__ == "__main__":
    unittest.main()
