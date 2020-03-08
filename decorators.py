import re

my_text = "Hello World"

def func():
  new_text = "New Text"
  
  # Print all local variables (Variables inside the function)
  print(locals())
  # Print all global variables such as my_text declared at the top 
  print(globals())
  
  
func()

new_func = func

new_func()

def function2 (name = ''):
  def hello():
    print("Hello {}".format(name))
  def greet():
    print("Greetings {}".format(name))
    
  if (re.findall('a', name)):
    return hello
  else:
    return greet
  
name = input("What's your name?\n")
message = function2(name)

message()