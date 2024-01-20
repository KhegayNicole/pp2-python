#introduction to puthon
print("Hello,World!")

#python syntax


#example
if 5>2:
    print("Five is greater than two!")

#example
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#python variables example 

x = 5
y = "Hello,World!"

print("Hello,World")

#exaple
x = 5
y = "John"
print(x)
print(y)

#example
x = 4       #x is of type int 
x = "Sally" #x is now type str
print(x)

#casting examples
x = str(3)  #x will be '3'
y = int(3)  #y will be 3
z = float(3)  #z will be 3.0

#get the type example

x = 5
y = "John"
print(type(x))
print(type(y))

#single or double quotes example
x = "John"
# is the same as
x = 'John'

#case-sensitive example
a = 4
A = "Sally"
#A will not overwrite a

#variable names example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
illeal var. names
2myvar = "John"
my-var = "John"
my var = "John"
"""
#multiple variables example1
x = y = z = "Orange"
print(x)
print(y)
print(z)
#multiple variables example2
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables example1
x = "Python is awesome"
print(x)

#output variables example2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#putput variables example3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#global variables example1
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#global variables example2
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#global variables example3
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#exercise
carname="Volvo"


#Python comments

#examples
#this is a comment.
print("Hello,World!")

print("Hello,World!") #This is a comment

#print("Hello,World!")
print("Cheers,Mate!")

#multiline comments
#example
#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in 
more just one line
"""

print("Hello, World!")

#This is a comment

#python data types
x = 5
print(type(x))
#output is "int"

#python numbers

#example1
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#example2 
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#example3 

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#example4
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
#example5
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
#example6
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number example
import random

print(random.randrange(1, 10))

#exercise

x = 5
x = float(x)

#python casting 
#example1

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#example2

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#example3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#python strings

#example1
print("Hello")
print('Hello')
#example2
a = "Hello"
print(a)
#example3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#example4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#example5
a = "Hello, World!"
print(a[1])
#example6
for x in "banana":
  print(x)
#example7
a = "Hello, World!"
print(len(a))

#check strings
#example1
txt = "The best things in life are free!"
print("free" in txt)
#example2
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#example3
txt = "The best things in life are free!"
print("expensive" not in txt)
#example4
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
