from trees import TreeNode,BST 
root = TreeNode('Electronics') # Initializing a general tree root node 
phone = TreeNode('Phone') 
tv = TreeNode('tv') 
root.add_child(phone) 
root.add_child(tv) 
print(root.tree()) 
#Sample Output: 
# Electronics
#    |--Phone
#    |--tv
# Adding further nodes
samsung = TreeNode('samsung') 
motorola = TreeNode('motorola') 
phone.add_child(samsung) 
phone.add_child(motorola)
print(root.tree())
# Sample output:
# Electronics
#    |--Phone
#       |--samsung
#       |--motorola
#    |--tv
# Only display to a specific level(depth)
print(root.tree(1)) 
#Sample Output:
# Electronics
#    |--Phone
#    |--tv
# Displaying tree as a python dictionary 
# with leave node:
print(root.tree_dict()) #{'Electronics': ['Phone', 'tv'], 'Phone': ['samsung', 'motorola'], 'samsung': None, 'motorola': None, 'tv': None}
# without leave node:
print(root.tree_dict(leave=False)) #{'Electronics': ['Phone', 'tv'], 'Phone': ['samsung', 'motorola']}
# Get the level(depth of a node) in the tree 
print(root.get_level()) #0
print(phone.get_level()) #1
print(motorola.get_level()) #2 
# Binary Search Tree:
search = BST(15) 
# Adding elements 
search.add(12) 
search.add(27)
search.add(14) 
search.add(7) 
search.add(20) 
search.add(28) 
search.add(23)
#Inorder traversal
print(search.inorder()) # [7, 12, 14, 15, 20, 23, 27, 28]
print(search.preorder()) # [15, 12, 7, 14, 27, 20, 23, 28]
print(search.postorder()) # [7, 14, 12, 23, 20, 28, 27, 15]