# Definition for singly-linked list.
class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(list_nodes: list[int]) -> LinkedList:
    """
    list_nodes = [1, 2, 3]
    (dummy) cur_node = (0, None)
    0. next_node = (1, None); (dummy) cur_node = (0, 1); cur_node = (1, None)
    1. next_node = (2, None); cur_node = (1, 2); cur_node = (2, None)
    2. next_node = (3, None); cur_node = (2, 3); cur_node = (3, None)
    return (1, 2)
    """
    dummy = LinkedList()  # we don't reassign this var
    cur_node = dummy  # start with CURRENT node (0, None)
    for value in list_nodes:
        next_node = LinkedList(value)  # create NEXT node with list val, but next is None
        cur_node.next = next_node  # link CURRENT node with the NEXT
        cur_node = next_node  # make the NEXT node the CURRENT
    return dummy.next  # return the FIRST LinkedList instance, that formed from the FIRST VALUE of the LIST (head)


def linkedlist_to_list(head: LinkedList) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
