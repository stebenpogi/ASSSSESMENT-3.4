

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


def preorder(node):    # Root -> Left -> Right
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)


def inorder(node):     # Left -> Root -> Right
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


def postorder(node):   # Left -> Right -> Root
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]


name = input("Enter your full name: ")
letters = [ch for ch in name.upper() if ch.isalpha()]
root = build_tree(letters)

print("Letters:   ", letters)
print("Preorder:  ", " -> ".join(preorder(root)))
print("Inorder:   ", " -> ".join(inorder(root)))
print("Postorder: ", " -> ".join(postorder(root)))