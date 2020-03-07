def my_func(param1 = False):
  """
  THIS FUNCTION RETURNS WHAT YOU'VE TYPED
  """
  print("You said {}".format(param1))

my_func()
my_func("Hello")

def hello():
  return 'Hello world'

my_message = hello()

print(my_message)

# Type checking

def addNum(num1, num2):
  if(type(num1) == type(num2) == type(10)):
    return num1 + num2
  else:
    return "Only Integers are allowed!"
  
result = addNum(2,3)
print(result)

result = addNum(2, "3")
print(result)

# Filter Function

my_list = [1,2,3,4,5,6]

def even_bool(num):
  return num%2 == 0

even = filter(even_bool, my_list)

print(list(even))

# Lambda Expression
even = filter(lambda num:num%2 == 0, my_list)

print("lambda {}".format(list(even)))