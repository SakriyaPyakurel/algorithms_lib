class Node:
    def __init__(self,data=None,next=None):
        self.data = data 
        self.next = next 
class SinglyLinkedlist:
    def __init__(self):
        self.head = None 
    def insert_at_begining(self,data):
        node = Node(data,self.head) 
        self.head = node 
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None) 
            return
        iter = self.head 
        while iter.next:
            iter = iter.next    
        iter.next = Node(data,None) 
    def insert_values(self,data_list:list,start=False):
        if start:
          for element in reversed(data_list):
            self.insert_at_begining(element)
        else:
            for element in data_list:
                self.insert_at_end(element)
    def get_length(self):
        count = 0 
        iter = self.head 
        while iter: 
            count+=1
            iter=iter.next
        return count
    def items(self,n=None,cast=False):
        if self.head is None:
            return [] if cast else '[]'
        if n is not None and  n > self.get_length():
            length = self.get_length()
            raise ValueError(f'Linked list has length {length} but n was given {n}')
        if cast:           
          iter = self.head 
          listr = []
          count = 0
          while iter and (n is None or count<n):
            listr.append(iter.data)
            iter = iter.next 
            count+=1
        else:
            iter = self.head 
            listr = '['
            count = 0
            while iter and (n is None or count<n):
               listr+=str(iter.data) 
               iter = iter.next 
               count+=1
               if iter and (n is None or count<n):
                  listr+=' '
            listr+= ']'
        return listr
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid index provided') 
        if index == 0:
            self.head = self.head.next 
            return 
        count = 0 
        iter = self.head 
        while iter:
            if count == index-1:
                iter.next = iter.next.next
                break 
            iter = iter.next 
            count+=1
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid index provided')
        if index==0:
            self.insert_at_begining(data) 
            return 
        count = 0 
        iter = self.head 
        while iter:
            if count == index-1:
                node = Node(data,iter.next) 
                iter.next = node 
                break 
            iter = iter.next
            count+=1
    def insert_after_value(self,data_after,data):
        if self.head is None:
            print('linked list is empty') 
            return 
        if self.head.data == data_after:
            self.head.next = Node(data,self.head.next)
            return 
        iter = self.head
        while iter:
            if iter.data == data_after:
                iter.next = Node(data,iter.next)
                break 
            iter = iter.next        
    def remove_by_value(self,data):
        if self.head is None:
            print("The linked list is empty") 
            return
        if self.head.data == data:
            self.head = self.head.next 
            return 
        iter = self.head 
        while iter.next:
            if iter.next.data == data:
              iter.next = iter.next.next
              break
            iter = iter.next 
class Nodes:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev 
        self.next = next 
class Doublylinkedlist():
    def __init__(self):
        self.head = None 
    def insert_at_begining(self,data):
        node = Nodes(data,next=self.head) 
        self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Nodes(data,next=self.head)  
            return
        iter = self.head 
        while iter.next:
            iter = iter.next    
        iter.next = Nodes(data,prev=iter.prev) 
    def insert_values(self,data_list:list,start=False):
        if start:
          for element in reversed(data_list):
            self.insert_at_begining(element)
        else:
            for element in data_list:
                self.insert_at_end(element)
    def get_length(self):
        count = 0 
        iter = self.head 
        while iter: 
            count+=1
            iter=iter.next
        return count
    def items(self,n=None,cast=False):
        if self.head is None:
            return [] if cast else '[]'
        if n is not None and  n > self.get_length():
            length = self.get_length()
            raise ValueError(f'Linked list has length {length} but n was given {n}')
        if cast:           
          iter = self.head 
          listr = []
          count = 0
          while iter and (n is None or count<n):
            listr.append(iter.data)
            iter = iter.next 
            count+=1
        else:
            iter = self.head 
            listr = '['
            count = 0
            while iter and (n is None or count<n):
               listr+=str(iter.data) 
               iter = iter.next 
               count+=1
               if iter and (n is None or count<n):
                  listr+=' '
            listr+= ']'
        return listr
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index provided') 
        if index == 0:
            self.head.next = self.head.next
        iter = self.head 
        count = 0 
        while iter:
            if count == index - 1:
                iter.next = iter.next.next 
                break 
            iter = iter.next 
            count+=1
    def insert_at(self,index,data):
        if index<0 and index>=self.get_length():
            raise Exception("Invalid index provided") 
        if index == 0:
           self.insert_at_begining(data) 
        count = 0
        iter = self.head 
        while iter:
            if count == index-1:
              node = Nodes(data,prev=iter.prev,next=iter.next) 
              iter.next = node
            iter = iter.next 
            count+=1
    def insert_after_value(self,data_after,data):
        if self.head is None:
            print("linked list is empty") 
            return 
        if self.head.data == data_after:
            self.head.next = Nodes(data,prev=self.head,next=self.head.next.next)
            return 
        iter = self.head 
        while iter:
            if iter.data == data_after:
                iter.next = Nodes(data,prev=iter.prev,next=iter.next) 
                break 
            iter = iter.next 
    def remove_by_value(self,data):
        if self.head is None:
            print("Linked list is empty") 
            return 
        if self.head.data == data:
            self.head = self.head.next
            return 
        iter = self.head 
        while iter.next:
            if iter.next.data == data:
                iter.next = iter.next.next 
                break 
            iter = iter.next