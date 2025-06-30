import unittest
from typing import Optional

from ..helpers import TreeNode, list_to_tree


def get_max_depth(head: Optional[TreeNode]) -> int:
    """
    [3, 9, 20, None, None, 15, 7]
       3
      / \
     9  20
       /  \
      15   7

    """
    if head is None:
        return 0
    else:
        left = get_max_depth(head.left)
        right = get_max_depth(head.right)
        return max(left, right) + 1


class TestGetMaxDepth(unittest.TestCase):
    def test_three_nodes(self):
        vals_list = [3, 9, 20, None, None, 15, 7]
        head = list_to_tree(vals_list)
        self.assertEqual(get_max_depth(head), 3)

    def test_two_nodes(self):
        vals_list = [1, None, 2]
        head = list_to_tree(vals_list)
        self.assertEqual(get_max_depth(head), 2)


if __name__ == "__main__":
    unittest.main()
