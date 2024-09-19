
"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
print("\n Python Lists: ")

names = ["srinu", "lee", "bruce", "jackie", "jet lee"]
books = ["ontari", "kasyapa yodha", "panchathanthram", "the alchemist"]
names.append("tony")
names.insert(2, "john")
names.extend(books)
# names.remove("lee")
# names.pop()
# names.clear()
# del books

print(names[:5])
print(names)

for name in names:
    print(name)


# List comprehension

print("\nUsing List Comprehension:\n")

[print(name) for name in names]

n = [1, 2, 56, 25, 65, 89, 635, 525, 75, 66, 10]
n.sort()
print(n)
n.sort(reverse= True) # descending order
print(n)

for elements in n:
    names.append(elements)

print(names)

# Tuple 
print("\n Tuple: \n")
tuple_item1 = tuple(("one", "two", "three"))
tuple_item2 = ("four", "five", "six")

tuple_item3 = tuple_item1 + tuple_item2

print(tuple_item1[0])
print(" Tuple items: ",tuple_item3)
print("Length of the Tuple: ",len(tuple_item3))

for item in tuple_item3:
    print(item)

# Tuple unpacking 
print("\n Tuple Unpacking: \n")

(a, b, c, *d) = tuple_item3

print(a)
print(b)
print(c)
print(d)


# Sets
print("\n Sets: \n")

fruits = {"apple", "banana", "cherry", "apple", True, False, 0, 1, 2}
seasonal = {"mango", "papaya"}
# duplicate values are ignored.
# 0, 1 are False, True
print(fruits)
print(len(fruits))

# We can use methods like add(), update()
fruits.add("orange")
print(fruits)

fruits.update(seasonal)

# We can use pop(), del, clear() methods on sets
fruits.remove("cherry")
fruits.discard("cherry")
print(fruits)

set1 = {"a", "b", "c", 1, 2, 4, 5}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set4 = set1 | set2

set5 = set1.intersection(set2)
set10 = set1.intersection_update(set2)
set6 = set1 & set2


set7 = set1.difference(set2)
set8 = set1 - set2
set9 = set2 - set1

set11 = set1.symmetric_difference(set2)
set12 = set1 ^ set2


print(set3)
print(set4)
print(set5)
print(set6)
print(set7)
print(set8)
print(set9)
print(set10)
print(set11)
print(set12)

# Dictionaries
print("\n Dictionary: \n")

car_details = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # This replaces the previous value
}
print(car_details)

car_details["color"] = "Blue"
car_details.update({"year": 2024})

print(car_details)

mydetails = dict(name = "Srinu", age = 25, country = "India")


print(mydetails)
print(mydetails["country"])
print(mydetails.get("name"))
print(mydetails.keys())
print(mydetails.values())
print(mydetails.items())

for item in mydetails.items():
    print(item)

# We can use pop(), popitem(), to remove items from dictionary and  clear(), del are used to erase whole dictionary.

#  Nested Dictionaries
print("\n Nested Dictionary: \n")

father = {
  "name" : "Naidu",
  "year" : 1976
}
mother = {
  "name" : "Surredu",
  "year" : 1981
}
son = {
  "name" : "Srinu",
  "year" : 1999
}
daughter = {
  "name" : "Bhavani",
  "year" : 2006
}

myfamily = {
  "Father" : father,
  "Mother" : mother,
  "Son"    : son,
  "Daughter" : daughter
}

print(myfamily)
print(myfamily["Father"]["name"])
print(myfamily["Mother"])
print(myfamily["Son"]["year"])
print(myfamily["Daughter"])
