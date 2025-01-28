#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John" 
MYVAR = "John"
myvar2 = "John"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Output Variables
x = "Python is awesome"
print(x)

#or
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#or
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 