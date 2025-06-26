import unittest

from ..helpers import LinkedList, list_to_linkedlist


def get_max_twin_sum(head: [LinkedList]) -> int:
    """[4,2,2,3] -> 7"""
    max_sum = - float("inf")
    nodes = []
    current = head
    while current:
        nodes.append(current.val)  # DO NOT FORGET: we're adding VALUE (.val), not the node itself!
        current = current.next
    n = len(nodes)
    for i in range(n - 1, -1, -1):
        cur_sum = nodes[i] + nodes[n - 1 - i]
        max_sum = max(cur_sum, max_sum)
    return max_sum


class TestGetMaxTwinSum(unittest.TestCase):
    def test_all_sums_equal(self):
        vals_list = [5, 4, 2, 1]
        head = list_to_linkedlist(vals_list)
        self.assertEqual(get_max_twin_sum(head), 6)

    def test_one_max_sum(self):
        vals_list = [4, 2, 2, 3]
        head = list_to_linkedlist(vals_list)
        self.assertEqual(get_max_twin_sum(head), 7)

    def test_only_one_sum(self):
        vals_list = [1000, 1]
        head = list_to_linkedlist(vals_list)
        self.assertEqual(get_max_twin_sum(head), 1001)


if __name__ == "__main__":
    unittest.main()
