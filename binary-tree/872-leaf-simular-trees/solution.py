import unittest

from ..helpers import TreeNode, list_to_tree


def are_leaf_simular(root1: TreeNode, root2: TreeNode) -> bool:
    def _get_all_leafs(root: TreeNode, leaf_list):
        if root.left is None and root.right is None:
            leaf_list.append(root.val)
            return  # go 1 lvl up the call stack, but there's nothing to return - the leaf's already in the list
        elif root.left:
            _get_all_leafs(root.left, leaf_list)
        if root.right:
            _get_all_leafs(root.right, leaf_list)
    leaf1, leaf2 = [], []
    _get_all_leafs(root1, leaf1)
    _get_all_leafs(root2, leaf2)
    return leaf1 == leaf2


class TestAreLeafSimular(unittest.TestCase):
    def test_true(self):
        vals_list1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
        vals_list2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
        head1 = list_to_tree(vals_list1)
        head2 = list_to_tree(vals_list2)
        self.assertEqual(are_leaf_simular(root1=head1, root2=head2), True)

    def test_false(self):
        vals_list1 = [1, 2, 3]
        vals_list2 = [1, 3, 2]
        head1 = list_to_tree(vals_list1)
        head2 = list_to_tree(vals_list2)
        self.assertEqual(are_leaf_simular(root1=head1, root2=head2), False)


if __name__ == "__main__":
    unittest.main()
