class Person:
  def __init__(self, name, age):
    self.__name = name  # Private attribute
    self.__age = age    # Private attribute

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age >= 0:
      self.__age = age
    else:
      print("Age cannot be negative.")

p1 = Person("Chetan", 32)
# print(f"Name: {p1.__name}")   # This will raise an AttributeError because __name is private
# print(f"Age: {p1.__age}")     # This will raise an AttributeError because __age is private
print(f"Name: {p1.get_name()}")
print(f"Age: {p1.get_age()}")