from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int


p1= Person("Chetan", 32)
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")
p1.name = "Kiran"  # This is allowed because the dataclass is mutable
p1.age = 40
print(f"Updated Name: {p1.name}")
print(f"Updated Age: {p1.age}")


@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int


p2 = ImmutablePerson("Pravin", 30)
print(f"Name: {p2.name}")
print(f"Age: {p2.age}")

#p2.name = "Piyush"  # This will raise an error because the dataclass is frozen
#p2.age = 38  # This will also raise an error because the dataclass is frozen

# print(f"Updated Name: {p2.name}")
# print(f"Updated Age: {p2.age}")