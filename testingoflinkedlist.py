import linkedlist 
singly = linkedlist.SinglyLinkedlist() 
singly.insert_at_end(10) # Inserting first element in the linkedlist
singly.insert_values([1,2,3]) # Insert multiple values from behind in the linked list
singly.insert_values([4,5,7],start=True) #Insert multiple values from front in the linked list 
# Getting all the items in the singly linked list in string notation
print(singly.items()) #[4 5 7 10 1 2 3]
# Getting all the items in the singly linked list as a python list
print(singly.items(cast=True)) #[4, 5, 7, 10, 1, 2, 3] 
#Getting the number of items in a linked list
print(singly.get_length()) # 7
# Getting specific numbers of items from the linked list 
print(singly.items(3)) #[4 5 7] 
print(singly.items(3,cast=True)) #[4, 5, 7] 
# Using next pointer to print all the elements of the linked list 
iter = singly.head 
while iter:
    print(iter.data) 
    iter = iter.next 
