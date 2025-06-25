import unittest
from typing import Optional

from ..helpers import LinkedList, list_to_linkedlist, linkedlist_to_list


def reverse_linkedlist(head: Optional[LinkedList]) -> Optional[LinkedList]:
    """
    [1, 2, 3] -> [3, 2, 1]
    0. 1 -> None; 2 -> 1
    1. 3 -> 2;
    """
    if not head:
        return None
    if not head.next:
        return head
    current, next_node = head, head.next
    while next_node:
        if current == head:
            current.next = None
        original_next = next_node.next  # save next before reversing, so we can continue traversing the linkedlist
        next_node.next = current
        current = next_node
        next_node = original_next
    return current   # ATTENTION!!! HEAD node is the LAST now! "current" is the new head after the reversing!


class TestReverseLinkedlist(unittest.TestCase):
    def test_five_nodes(self):
        vals_list = [1, 2, 3, 4, 5]
        head = list_to_linkedlist(vals_list)
        grouped = reverse_linkedlist(head)
        self.assertEqual(linkedlist_to_list(grouped), [5, 4, 3, 2, 1])

    def test_two_nodes(self):
        vals_list = [1, 2]
        head = list_to_linkedlist(vals_list)
        grouped = reverse_linkedlist(head)
        self.assertEqual(linkedlist_to_list(grouped), [2, 1])

    def test_zero_nodes(self):
        vals_list = []
        head = list_to_linkedlist(vals_list)
        grouped = reverse_linkedlist(head)
        self.assertEqual(linkedlist_to_list(grouped), [])


if __name__ == "__main__":
    unittest.main()
