# main.py - run this file in PyCharm
from sorting import build_unsorted, insertion_sort
from traversals import build_tree, bfs, preorder, inorder, postorder

name = input("Enter your full name: ")

print("\nPART 1: SORTING")
unsorted_array = build_unsorted(name)
print("Unsorted:", unsorted_array)
sorted_array = insertion_sort(unsorted_array)
print("Sorted:  ", sorted_array)

print("\nPART 2: TREE TRAVERSALS (tree built from the sorted array)")
root = build_tree(sorted_array)
print("BFS (Level order):", " -> ".join(bfs(root)))
print("DFS Preorder:     ", " -> ".join(preorder(root)))
print("DFS Inorder:      ", " -> ".join(inorder(root)))
print("DFS Postorder:    ", " -> ".join(postorder(root)))