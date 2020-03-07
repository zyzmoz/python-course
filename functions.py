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