# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(list_nodes: list[int]) -> Optional[TreeNode]:  # TODO: change with "| None"
    if not list_nodes:
        return None

    root = TreeNode(list_nodes[0])
    queue = [root]
    i = 1  # points to next value in list_nodes

    while queue and i < len(list_nodes):
        current = queue.pop(0)

        # Left child
        if i < len(list_nodes) and list_nodes[i] is not None:
            current.left = TreeNode(list_nodes[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(list_nodes) and list_nodes[i] is not None:
            current.right = TreeNode(list_nodes[i])
            queue.append(current.right)
        i += 1

    return root
