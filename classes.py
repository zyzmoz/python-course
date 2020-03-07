class Dog():
  # Class Object Attribute
  species = "Mammal"
  
  def __init__(self, breed, name):
    self.breed = breed
    self.name = name
    # pass
  
  

mydog = Dog("Pug", "No One")

print(mydog.breed)
print(mydog.name)
print(mydog.species)

# mydog.species = "Troll"
# print(mydog.species)

class Circle():
  pi = 3.14
  
  def __init__(self, radius = 1):
    self.radius = radius
  
  def area(self):
    return self.radius * self.radius * Circle.pi
  
  def set_radius(self, radius):
    self.radius = radius
    
    
my_circle = Circle(3)

my_circle.set_radius(999)

print(my_circle.area())