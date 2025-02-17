from linkedlist import SinglyLinkedlist
class HashTable:
    def __init__(self,max:int,probe=False):
        self.max = max
        self.__arr = [None for i in range(self.max)] 
        self.probe = probe
        self.content = {}
    def __str__(self):
        hashstr = """Index   Content\n"""  
        for i in range(len(self.__arr)):
            if self.__arr[i] == None:
                hashstr+=f'{i}\n'
            else:
               hashstr+=f"{i}\t{self.__arr[i]}\n"
        hashstr+=f"length:{len(self.__arr)}\t\tobject:hashtable"
        return hashstr
    def get_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char) 
        return h%self.max
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        if self.probe:
            none_count = sum(1 for element in self.__arr if element is None)
            if none_count == 0:
                raise Exception('Table already full, cannot insert new value')

            original_h = h  
            while self.__arr[h] is not None:
                h = (h + 1) % self.max
                if h == original_h:  
                    raise Exception('Table already full, cannot insert new value')

            self.__arr[h] = (key, val)
            self.content.update({key:val})
        else:
            if self.__arr[h] is None:
                singly = SinglyLinkedlist()
                singly.insert_at_end((key, val))
                self.__arr[h] = singly.items(cast=True)
                self.content.update({key:val})
            else:
                self.__arr[h] = list(self.__arr[h]) 
                self.__arr[h].append((key,val))
                self.content.update({key:val})
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.__arr[h] is not None:
            if self.probe:
                original_h = h
                while self.__arr[h] is not None:
                    if self.__arr[h][0] == key:
                        return self.__arr[h][1]
                    h = (h + 1) % self.max
                    if h == original_h:
                        break
            else:
                for element in self.__arr[h]:
                    if element[0] == key:
                        return element[1]
        return None
    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.__arr[h] is not None:
            if self.probe:
                original_h = h
                while self.__arr[h] is not None:
                    if self.__arr[h][0] == key:
                        self.__arr[h] = None  
                        return
                    h = (h + 1) % self.max
                    if h == original_h:
                        break
            else:
                to_remove = None
                for element in self.__arr[h]:
                    if element[0] == key:
                        to_remove = element
                        break
                if to_remove:
                    self.__arr[h].remove(to_remove)
                    if not self.__arr[h]: 
                        self.__arr[h] = None