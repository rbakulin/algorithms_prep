import unittest

from ..helpers import TreeNode, list_to_tree


def count_good_nodes(root: TreeNode) -> int:
    def _get_all_good_nodes(node: TreeNode, path_max: int, goods: list[int]):
        if node.val >= path_max:  # the value has to be BIGGER then every other val on its path
            goods.append(node.val)
        # good or not every node affects what the future children consider as the max value on the path
        path_max = max(node.val, path_max)
        if node.left:
            _get_all_good_nodes(node.left, path_max, goods)
        if node.right:
            _get_all_good_nodes(node.right, path_max, goods)
    good_nodes = []  # have to be MUTABLE, so it can be change OUTSIDE the CURRENT CALL
    # we don't need all path to each val, only the max val on this path
    _get_all_good_nodes(node=root, path_max=root.val, goods=good_nodes)
    return len(good_nodes)


class TestCountGoodNodes(unittest.TestCase):
    def test_two_branches_tree(self):
        vals_list = [3, 1, 4, 3, None, 1, 5]
        head = list_to_tree(vals_list)
        self.assertEqual(count_good_nodes(root=head), 4)

    def test_one_branch_tree(self):
        vals_list = [3, 3, None, 4, 2]
        head = list_to_tree(vals_list)
        self.assertEqual(count_good_nodes(root=head), 3)

    def test_only_root_tree(self):
        vals_list = [1]
        head = list_to_tree(vals_list)
        self.assertEqual(count_good_nodes(root=head), 1)


if __name__ == "__main__":
    unittest.main()
