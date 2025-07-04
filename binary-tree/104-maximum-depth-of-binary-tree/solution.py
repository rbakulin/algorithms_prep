import unittest

from ..helpers import TreeNode, list_to_tree


def get_max_depth(root: TreeNode | None) -> int:
    """
    [3, 9, 20, None, None, 15, 7]

       3
      / \
     9  20
       /  \
      15   7

    get_max_depth(3)
    │
    ├── left = get_max_depth(9) → returns 1
    │   ├── left = get_max_depth(None) → returns 0
    │   └── right = get_max_depth(None) → returns 0
    │   max(0, 0) + 1 = 1
    │
    └── right = get_max_depth(20) → returns 2
        ├── left = get_max_depth(15) → returns 1
        │   ├── left = get_max_depth(None) → returns 0
        │   └── right = get_max_depth(None) → returns 0
        │   max(0, 0) + 1 = 1
        │
        └── right = get_max_depth(7) → returns 1
            ├── left = get_max_depth(None) → returns 0
            └── right = get_max_depth(None) → returns 0
            max(0, 0) + 1 = 1
        max(1, 1) + 1 = 2
    max(1, 2) + 1 = 3
    """
    if root is None:
        return 0  # reached the end of a path (no node here), return 0 because None doesn't contribute to depth
    else:
        left = get_max_depth(root.left)
        right = get_max_depth(root.right)
        return max(left, right) + 1  # take the larger depth between left and right, then add 1 for the current node


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
