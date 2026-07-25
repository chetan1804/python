class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    pass

d1 = Dog("Rex")
d1.speak()  # Output: Rex makes a sound.