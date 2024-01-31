#boolean

#example1

print(10 > 9)
print(10 == 9)
print(10 < 9)

#example2

a = 200
b = 33
if b>a:
     print("b is greater than a")
else:
     print("b is not reater than a")

#example3 evaluate values and variables

print(bool("Hello"))
print(bool(15))

#or4

x="Hello"
y=15
print(bool(x))
print(bool(y))

#example5
bool("abc")
bool(123)
bool(["apple","cherry","banana"])

#example6

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example6
x = 200
print(isinstance(x, int))
#exersixe
print(10>9)

#python operators

#example1
print(10+5)
#example2
print((6 + 3) - (6 + 3))
#example3
print(100 + 5 * 3)
#example3
print(5 + 4 - 7 + 3)
#exersice
print(10*5)

#python lists
#example1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#example2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#example3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#example4
list1 = ["abc", 34, True, 40, "male"]
#example5
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#access list items
#example1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#exampl2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#example3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#example4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#example5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#change list items
#example1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#example2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#example3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#example4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#example5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add list items
#example
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#remove list items
#example
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#example
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#example
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#loops lists
#example
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#example
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#example
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#example
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#list comprehension example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#example copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#join lists example
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#exersice
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#___________________tuples________________________unchangeable
#example
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#example convert tuple to list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#example
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#loop tuples
#example
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#example
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#exersice
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#_________sets___________
#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes,apple is fruit!")
#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#exersice
fruits = {"apple", "banana", "cherry"}
if "apple" in  fruits:
  print("Yes, apple is a fruit!")

#dictionaries

#ex1
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964   
}
print(car.get("model"))
#ex2
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964   
}
car["year"] = 2020
#ex3
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964   
}
car["color"] = "red"
#ex4
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964   
}
car.pop("model")
#ex5
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964   
}
car.clear()

#exersice
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#if else
#ex1
a = 50
b = 10
if a > b:
    print("Hello World")
#ex2
a = 50
b = 10
if a != b:
    print("Hello World")
#ex3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
#ex4
a = 50
b = 10
if a ==b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
#ex5
if a == b and c == d:
    print("Hello")
#ex6
if a == b or c ==d:
    print("Hello")
#ex7
if 5 >2:
    print("YES")
#ex8
a = 2
b = 5
print("YES") if a == b else print("NO")
#ex9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")
#exersice
a = 50
b = 10
if a > b:
  print("Hello World")

#while loops
#ex1
i = 1
while i < 6:
    print(i)
    i+=1
#ex2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1
#ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
      continue
  print(i)
#ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
    print("i is no longer less than 6")
#exersice
i = 1
while i < 6:
  print(i)
  i += 1    
#for loops
#example1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#example2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  print(x)
#example3
for x in range(6):
    print(x)
#example4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
#exersice
fruits = ["apple", "banana", "cherry"]
for  x  in fruits:
  print(x)