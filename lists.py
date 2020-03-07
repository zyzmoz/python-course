list1 = [
  "Bread",
  "Milk",
  "Cocoa"
]

print(len(list1))

list1[0] = "Cheese"

print(list1)

# Add a Item to the list
list1.append('Coconut')

print(list1)

# Delete the last item
list1.pop(-1)

print(list1)

list2 = [
  "Banana",
  "Apple"
]

# Add all items of list2 to list1
list1.extend(list2)

print(list1)

# reverses the list
list1.reverse()

print(list1)

# Sort list
list1.sort()

print(list1)
