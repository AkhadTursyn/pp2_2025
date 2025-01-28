list1 = ['apple', 'banana', 'cherry', 'orange', 'berry', 'kiwi', 'melon']
for i in range(len(list1)):
    if list1[i]== 'banana':
        print('banana index equal to ', i)
print(i)
x = list1.index('kiwi')             #alternative
print(x)

print('\n', '____________________________', '\n')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)

print('\n', '____________________________', '\n')

list = (1, 2, 5, 4, 3, 2, 8)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list