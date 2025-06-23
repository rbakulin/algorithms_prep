import unittest
from typing import Optional

from ..helpers import LinkedList, list_to_linkedlist, linkedlist_to_list


def remove_middle_node(head: LinkedList) -> Optional[LinkedList]:
    """
    O(2n) time complexity
    [1, 2, 3, 4] -> [1, 2, 4]
    [2, 1] -> [2]
    """
    n = 0
    current = head
    while current:  # extra loop just to count all the vals - can be avoided
        n += 1
        current = current.next
    if n == 1:
        return None  # DON'T FORGET: since the returned value is optional, it's fine to just return None
    middle_index = n // 2
    i = 0
    current = head
    while i != middle_index - 1:
        current = current.next
        i += 1
    current.next = current.next.next
    return head


def remove_middle_node_fast_slow(head: LinkedList) -> Optional[LinkedList]:
    """
    the func travers through the linked list 1 time -> O(n)
    """
    if not head.next:
        return None
    slow = head  # moves 1 step a time (head -> head.next) - will be on middle index, when the fast well get to the end
    fast = head  # moves 2 steps a time (head -> head.next.next)
    prev = None  # needed only for tracking prev element before slow - it will be used, when we'll skip the middle node
    while fast and fast.next:  # fast and next to it exist -> fast.next.next also exists
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next  # skipping the middle index
    return head


class TestRemoveMiddleNode(unittest.TestCase):
    def test_odd_node_count(self):
        vals_list = [1, 3, 4, 7, 1, 2, 6]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [1, 3, 4, 1, 2, 6])

    def test_even_node_count(self):
        vals_list = [1, 2, 3, 4]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [1, 2, 4])

    def test_two_node_count(self):
        vals_list = [2, 1]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [2])

    def test_one_node_count(self):
        vals_list = [1]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [])

    def test_odd_node_count_fast_slow(self):
        vals_list = [1, 3, 4, 7, 1, 2, 6]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node_fast_slow(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [1, 3, 4, 1, 2, 6])

    def test_even_node_count_fast_slow(self):
        vals_list = [1, 2, 3, 4]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node_fast_slow(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [1, 2, 4])

    def test_two_node_count_fast_slow(self):
        vals_list = [2, 1]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node_fast_slow(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [2])

    def test_one_node_count_fast_slow(self):
        vals_list = [1]
        head = list_to_linkedlist(vals_list)
        no_middle_node = remove_middle_node_fast_slow(head)
        self.assertEqual(linkedlist_to_list(no_middle_node), [])


if __name__ == "__main__":
    unittest.main()
