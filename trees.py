class TreeNode:
    def __init__(self, data):
        self.data = data
        self.__children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.__children.append(child)
    def tree_dict(self, leave=True):
        if not self.__children:  
            return {self.data: None} if leave else {}

        tree_dict = {self.data: [child.data for child in self.__children]}
        
        for child in self.__children:
            tree_dict.update(child.tree_dict(leave)) 
        
        return tree_dict
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def get_max_depth(self):
        if not self.__children:
            return self.get_level()
        return max(child.get_max_depth() for child in self.__children)
    def tree(self, level=None):
        if self.parent is None: 
            max_depth = self.get_max_depth()
            if level is not None and level > max_depth:
                raise ValueError(f"Invalid level provided. Max depth is {max_depth}, but got {level}.")

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        result = prefix + self.data + "\n"

        if level is None or self.get_level() < level:
            for child in self.__children:
                result += child.tree(level)

        return result
class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.__children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        if len(self.__children)==2:
            raise Exception(f'The parent: {self.parent} already has two nodes')
        self.__children.append(child)
    def tree_dict(self, leave=True):
        if not self.__children:  
            return {self.data: None} if leave else {}

        tree_dict = {self.data: [child.data for child in self.__children]}
        
        for child in self.__children:
            tree_dict.update(child.tree_dict(leave)) 
        for k,v in tree_dict.items():
            if v is not None:
                if len(v) == 1:
                    raise Exception(f'The parent node {k} is incomplete')
        return tree_dict
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def get_max_depth(self):
        if not self.__children:
            return self.get_level()
        return max(child.get_max_depth() for child in self.__children)
    def tree(self, level=None):
        if self.parent is None: 
            max_depth = self.get_max_depth()
            if level is not None and level > max_depth:
                raise ValueError(f"Invalid level provided. Max depth is {max_depth}, but got {level}.")

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        result = prefix + self.data + "\n"
        if level is None or self.get_level() < level:
            if len(self.__children) == 1:
                raise Exception("Tree is incomplete cannot display")
            else:
              for child in self.__children:
                result += child.tree(level)

        return result
class BST:
    def __init__(self,data:int|str):
        self.data = data 
        self.left = None 
        self.right = None 
    def add(self,data:int|str):
        if data == self.data:
            raise Exception(f'node {data} is already present in the tree') 
        if data < self.data:
            if self.left:
                self.left.add(data) 
            else:
                self.left = BST(data) 
        else:
            if self.right:
                self.right.add(data) 
            else:
                self.right = BST(data) 
    def inorder(self):
        elements = [] 
        if self.left:
            elements+=self.left.inorder()
        elements.append(self.data) 
        if self.right:
            elements+=self.right.inorder() 
        return elements
        
        