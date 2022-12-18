"""List
    1) Lists are used to store multiple items in a single variable
    2) One of 4 built-in data types in Python used to store collections of data
""" 

list1 = ['Apple', 'Mango', 'Orange', 'Apple', 'Orange', 1, 5, True, False, False]
# list2 = list(('Apple', 'Mango', 'Orange', 'Apple', 'Orange', 1, 5, True, False, False))
# Note Double round-brackets
print(f"TYPE : {type(list1)} - \nLIST : {list1}")
print(f"LENGTH : {len(list1)} ")

"""Action Items
    1) Accessing Elements
    2) Modifying Elements
    3) Adding/Removing Elements
    4) Looping Lists
    5) List Comprehension
    6) Sorting List
    7) Copy List
    8) Joining Two or More Lists
"""

# Accessing Elements
print(f"LIST ITEM AT 1 : {list1[1]}")
print(f"LIST ITEM AT -3 : {list1[-3]}")
print(f"LIST ITEMS FROM 3 TO -1 : {list1[3:-1]}") # Similarly like String Accessors

if "Mango" in list1:
  print("Yes, 'Mango' is in the fruits list")
  
# Modifying Elements
list1[2] = "Watermelon"
print(f"Modified List : {list1}")
list1[1:4] = ["Potato", "Tomato", "Ladyfingers"]
print(f"Modified By Range List 1 : {list1}")
list1[1:4] = ["Potato"]
print(f"Modified By Range List 2 : {list1}")

# Adding/Removing List Items
# Append
list1.append("Potato")
print(f"Append : {list1}") # Append can take tupples, list, dictionary & sets items also
# Insert
list1.insert(1, "Mango")
print(f"Insert : {list1}") # Insert can take tupples, list, dictionary & sets items also
# Extend
list2 = [["A", "B"], "Cherry", "Kiwi"]
list1.extend(list2) # Extend can take tupples, list, dictionary & sets items also
print(f"Extend : {list1}")

# Removing
list1.remove('Potato')
print(f"Remove : {list1}") # Removes first occurrence
# Popping Items
list1.pop(8) # Popping out item without index will remove last item 
print(f"Popping From 8: {list1}")
# Deleting Item
del list1[8] # `del list1` will delete entire list
print(f"Delete From 8 : {list1}")
list1.clear()
print(f"Clear : {list1}")

del list1
del list2
# print(f"Deleting Lists : {list1} {list2}")
print('\n')
""" Output
      Traceback (most recent call last):
        File "c:\\Users\\DELL\\Documents\\projects\\PythonFundamentals\\4.lists.py", line 59, in <module>
          print(f"Deleting Lists : {list1} {list2}")
      NameError: name 'list1' is not defined. Did you mean: 'list'?
"""

# Looping Lists
loopableList = ['Apple', 'Mango', 'Orange', 'Cherry', 'Kiwi']
# For Loop
print("For Loop Iterations : ")
# Looping through items 
for item in loopableList:
  print(f"Item : {item}")

# Looping through indexes
for index in range(len(loopableList)):
  print(f"Item at {index} : {loopableList[index]}")

# While Loop
print("While Loop Iterations : ")
i = 0
while i < len(loopableList):
  print(f"Item at {i} : {loopableList[i]}")
  i = i + 1

print('\n')

# List Comprehension
# newlist1 = [expression for item in iterable if condition == True]
# newlist2 = [expression for item in iterable]
print('List Comprehension : ')
# Looping Using List Comprehension
[print(f"Item : {item}") for item in loopableList]

# Uncomprehened list
normalList = []
for x in loopableList:
  if "e" in x:
    normalList.append(x)

print(f"Uncomprehened List : {normalList}")

comprehendList = [item for item in loopableList if "e" in item]

print(f"Comprehend List : {comprehendList}")

# Sorting

sortList = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortList.sort(reverse = True)

print(f"Sorted Reverse : {sortList}")

sortList.sort(reverse = False)
# sortList.sort() # Ascending Sort

print(f"Sorted Reverse False : {sortList}")
print('\n')

# Copy List
copiedList = sortList.copy()
# copiedList = list(sortList) # This is also the same thing

print(f"Copied list : {copiedList}")
print('\n')

# Joining List

jointList = copiedList + sortList
# jointList = copiedList.extend(sortList)
print(f"Joined list : {jointList}")