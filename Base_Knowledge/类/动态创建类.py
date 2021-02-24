def __init__(self, name):
    self.name = name

Dog = type("Dog", (object,), {'role':'dog', "__init__":__init__})

print(Dog)

dog = Dog('Abb')

print(dog)

print(dog.role, dog.name)