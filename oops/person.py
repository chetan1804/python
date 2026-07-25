class Person:
  species = "Human"

  def __init__(self,name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello {self.species}, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Chetan", 32)
p1.greet()  
print(f"Species: {p1.species}")