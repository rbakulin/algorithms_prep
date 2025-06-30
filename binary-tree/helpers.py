# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(nodes: list[int] | None) -> TreeNode | None:
    """
    nodes = [3,9,20,11,14,15,7] == [root=3, roots_children=(9,20), 9s_children=(11,14), 20s_children(15,7)]
    """
    if not nodes:
        return None
    tree_objects = [TreeNode(node) if node is not None else None for node in nodes]
    root = tree_objects[0]
    parent_index = 0
    child_index = 1
    while child_index < len(tree_objects):
        parent = tree_objects[parent_index]
        parent_index += 1
        if parent is None:
            continue
        parent.left = tree_objects[child_index]
        child_index += 1
        parent.right = tree_objects[child_index]
        child_index += 1
    return root
