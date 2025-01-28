list1 = ['apple', 'banana', 'cherry', 'orange', 'berry', 'kiwi', 'melon']
list2 = [1, 8, 5, 4, 5, 7, 0]
list3 = [True, False, True, True, False]
print(type(list1))
print(type(list2))
print(type(list3))

print('\n', '____________________________', '\n')

print(list1[0],' >> ', type(list1[0]))
print(list2[0],' >> ', type(list2[0]))
print(list3[0],' >> ', type(list3[0]))

print('\n', '____________________________', '\n')

print(list2[2:5])           #elemenets which index [2, 5)

print('\n', '____________________________', '\n')

list0 = ['apple', 'banana', 'cherry']
list0[1:] = 'orange', 'berry'             #we can change elements of list
print(list0)

print('\n', '____________________________', '\n')

list0.append('kiwi')               #we can add elements to the already existed list (not like in c++ :) ! )
print(list0)
list0.insert(1, 'melon')            #adding with index
print(list0)

print('\n', '____________________________', '\n')

listthislist = ["apple", "banana", "cherry"]
listthislist.remove('banana')       #first appearance of banana
listthislist.pop(1)                 #deleting by index
del listthislist                    #deleting whole list