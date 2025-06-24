import unittest
from typing import Optional

from ..helpers import LinkedList, list_to_linkedlist, linkedlist_to_list


def group_odd_indexes_after_even(head: LinkedList) -> Optional[LinkedList]:
    """
    [1, 2, 3, 4, 5] -> [1, 3, 5, 2, 4] || [3, 2, 1] -> [3, 1, 2]
    0. 1 -> 3; 2 -> 4
    1. 3 -> 5; 4 -> None
    """
    if not head:
        return None
    if not (head.next and head.next.next):  # len() is 1 or 2
        return head
    even, odd, next_even = head, head.next, head.next.next
    first_odd = odd  # we store the first odd to link the last even node to this odd at the end
    while even and odd and next_even:
        even.next = odd.next
        odd.next = next_even.next
        even = even.next
        odd = odd.next
        next_even = odd.next if odd else None
    even.next = first_odd
    return head



class TestGroupEvenIndexesAfterOdd(unittest.TestCase):
    def test_five_nodes(self):
        vals_list = [1, 2, 3, 4, 5]
        head = list_to_linkedlist(vals_list)
        grouped = group_odd_indexes_after_even(head)
        self.assertEqual(linkedlist_to_list(grouped), [1, 3, 5, 2, 4])

    def test_seven_nodes(self):
        vals_list = [2, 1, 3, 5, 6, 4, 7]
        head = list_to_linkedlist(vals_list)
        grouped = group_odd_indexes_after_even(head)
        self.assertEqual(linkedlist_to_list(grouped), [2, 3, 6, 7, 1, 5, 4])

    def test_three_nodes(self):
        vals_list = [3, 2, 1]
        head = list_to_linkedlist(vals_list)
        grouped = group_odd_indexes_after_even(head)
        self.assertEqual(linkedlist_to_list(grouped), [3, 1, 2])

    def test_four_nodes(self):
        vals_list = [1, 2, 3, 4]
        head = list_to_linkedlist(vals_list)
        grouped = group_odd_indexes_after_even(head)
        self.assertEqual(linkedlist_to_list(grouped), [1, 3, 2, 4])

    def test_zero_nodes(self):
        vals_list = []
        head = list_to_linkedlist(vals_list)
        grouped = group_odd_indexes_after_even(head)
        self.assertEqual(linkedlist_to_list(grouped), [])


if __name__ == "__main__":
    unittest.main()
