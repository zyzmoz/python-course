import random


# Get Number

def get_number():
  return list(input("Please enter your guess:\n"))

# Generate Code 

def generate_code():
  digits = [str(num) for num in range(10)]
  random.shuffle(digits)
  
  return digits[:3]

code = generate_code()

# Generate Tips

def tips(code, user_number):
  if (code == user_number):
    return "You cracked the code"
  
  for num in user_number: 
    if (num in code):
      return "You got a match"
  
  return "Nope! Try again!"

# Game Logic
user_number = []
# print(code)
while code != user_number:
  user_number = get_number()
  result = tips(code, user_number)
  print(result)
 
 