import ht
# without probing 
hash_no_probe = ht.HashTable(10)
hash_no_probe['aa'] = 'Hello' 
hash_no_probe['bb'] = 'World' 
hash_no_probe['ac'] = 'Hey'
del hash_no_probe['bb']
print(hash_no_probe['aa']) #Hello
print(hash_no_probe['bb']) #None
hash_no_probe['bb'] = 'everybody'
print(hash_no_probe)
# Sample Output:
# Index   Content
# 0
# 1
# 2
# 3
# 4       [('aa', 'Hello')]
# 5
# 6       [('ac', 'Hey'), ('bb', 'everybody')]
# 7
# 8
# 9
# length:10               object:hashtable
# with probing
hash_probe = ht.HashTable(10,probe=True)
hash_probe['aa'] = 'Hello' 
hash_probe['bb'] = 'World' 
hash_probe['ac'] = 'Hey'
del hash_probe['bb']
print(hash_probe['aa']) #Hello
print(hash_probe['bb']) #None
hash_probe['bb'] = 'everybody'
print(hash_probe)
# Sample Output:
# Index   Content
# 0
# 1
# 2
# 3
# 4       ('aa', 'Hello')
# 5
# 6       ('bb', 'everybody')
# 7       ('ac', 'Hey')
# 8
# 9
# length:10               object:hashtable
print(hash_no_probe.content) #{'aa': 'Hello', 'bb': 'everybody', 'ac': 'Hey'}