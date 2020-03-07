class Animal():
  def __init__(self):
    print("Animal created")
  
  def who_am_i(self):
    print("Animal")
  
  def eat(self):
    print("Eat")


class Dog(Animal):
  def __init__(self):
    # This isnt necessary but still a good practice
    Animal.__init__(self)
    print("Dog created")  
  
  def bark(self):
    print("Wof")
    
  # Override
  def eat(self):
    print("Dog eating")
    
  # String representation
  def __str__(self):
    return "Name {}".format("Test")
    
    
my_dog = Dog()

print(my_dog)

my_dog.who_am_i()
my_dog.eat()
