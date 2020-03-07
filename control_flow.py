if (2<3):
  print('yes')
else:
  print('no')
  
if (2 > 3):
  print('yes')
elif (3==3):
  print("no")
  
  
sequence = [1,2,3,4,5,6]

for item in sequence:
  print(item)
  
dictionary = {1: "Daniel", 2:"Mike", 3:"Loona"}

for key in dictionary:
  print("{} is {}".format(dictionary[key], key))

list1 = [(1,2), (3,4), (5,6)]

for (t1,t2) in list1:
  print("{}, {}".format(t1,t2))
  
i = 0

while i<5:
  print("i is {}".format(i))
  i = i + 1
