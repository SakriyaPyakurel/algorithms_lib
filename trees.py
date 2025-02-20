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
    def preorder(self):
        elements = [] 
        elements.append(self.data) 
        if self.left:
            elements+=self.left.preorder()
        if self.right:
            elements+=self.right.preorder() 
        return elements
    def postorder(self):
        elements = []
        if self.left:
            elements+=self.left.postorder() 
        if self.right:
            elements+=self.right.postorder()
        elements.append(self.data) 
        return elements
    def sum(self):
        res = 0 
        if self.left:
            res+=self.left.sum()
        res+=self.data 
        if self.right:
            res+=self.right.sum() 
        return res
    def min(self):
      current = self
      while current.left is not None:
        current = current.left
      return current.data
    def max(self):
        current = self 
        while current.right is not None:
            current=current.right 
        return current.data
    def find(self,val):
        if val == self.data:
            return True 
        if val < self.data:
            if self.left:
                return self.left.find(val)
        if val > self.data:
            if self.right:
                return self.right.find(val) 
        return False
    def remove(self, val):
      if val < self.data:
        if self.left:
            self.left = self.left.remove(val)
      elif val > self.data:
        if self.right:
            self.right = self.right.remove(val)
      else:
        if self.left is None and self.right is None:
            return None
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left
        max_val = self.left.max()
        self.data = max_val
        self.left = self.left.remove(max_val)
      return self
class Graph:
    def __init__(self,weight=False):
        self.graph = {} 
        self.weight = weight
    def add_node(self,node,edge,weight:int|float=None):
        if self.weight:
          if node in self.graph:
              if weight is not None:
                  self.graph[node][edge] = weight
              else:
                  raise Exception('Invalid weight supplied') 
          else:
              if weight is not None:
                self.graph[node] = {edge:weight} 
              else:
                raise Exception('Invalid weight supplied')
        else:
            if node in self.graph:
                if weight is None:
                    self.graph[node].append(edge)
                else:
                    raise Exception('Cannot supply weight in non-weighted graph') 
            else:
                if weight is None:
                    self.graph[node] = [edge] 
                else:
                    raise Exception('Cannot supply weight in non-weighted graph') 
    def get_paths(self, start, end, path=None):
      if path is None:
        path = []  
      path = path + [start]


      if start == end:
        return path

      if start not in self.graph:
        return []

      paths = []


      if self.weight:
         neighbors = self.graph[start].keys()
      else:
        neighbors = self.graph[start]

      for node in neighbors:
        if node not in path:
            new_paths = self.get_paths(node, end, path)
            paths.extend(new_paths)
      return paths
    def get_shortest_path(self, start, end):
      if start == end:
        return [start]
      if start not in self.graph:
        return None

      if not self.weight:
        queue = [[start]]
        visited = set()

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self.graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)
        return None

   
      else:
        queue = [(0, start, [start])]
        visited = set()

        while queue:
            queue.sort(key=lambda x: x[0])
            cost, node, path = queue.pop(0)

            if node == end:
                return path

            if node in visited:
                continue

            visited.add(node)

            for neighbor, w in self.graph.get(node, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((cost + w, neighbor, new_path))
        return None

  
