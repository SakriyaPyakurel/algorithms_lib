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
# Preorder traversal
print(search.preorder()) # [15, 12, 7, 14, 27, 20, 23, 28]
#Postorder traversal
print(search.postorder()) # [7, 14, 12, 23, 20, 28, 27, 15]
# Sum of all elements
print(search.sum()) # 146
# Getting min value 
print(search.min()) #7
# Getting max value
print(search.max()) # 28
# Checking whether a value is present in the tree or not 
print(search.find(14)) # True
print(search.find(13)) # False
# Testing with string 
search = BST('Sam') 
search.add('Sakriya') 
search.add('David') 
search.add('Elina') 
search.add('Ramesh') 
print(search.inorder()) #['David', 'Elina', 'Ramesh', 'Sakriya', 'Sam']
print(search.preorder()) # ['Sam', 'Sakriya', 'David', 'Elina', 'Ramesh'] 
print(search.postorder()) # ['Ramesh', 'Elina', 'David', 'Sakriya', 'Sam']
print(search.min()) # David
print(search.max()) # Sam 
print(search.find('Elina')) #True
print(search.find('Gagan')) #False
