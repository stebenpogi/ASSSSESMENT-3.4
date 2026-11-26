
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(letters):
    """Fill the tree level by level, left to right."""
    nodes = [Node(ch) for ch in letters]
    for i, node in enumerate(nodes):
        if 2 * i + 1 < len(nodes):
            node.left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            node.right = nodes[2 * i + 2]
    return nodes[0]


def bfs(root):
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def preorder(n):   # Root -> Left -> Right
    return [] if n is None else [n.data] + preorder(n.left) + preorder(n.right)


def inorder(n):    # Left -> Root -> Right
    return [] if n is None else inorder(n.left) + [n.data] + inorder(n.right)


def postorder(n):  # Left -> Right -> Root
    return [] if n is None else postorder(n.left) + postorder(n.right) + [n.data]