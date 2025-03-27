# Basic class definition
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    # Method to get the person's name
    def get_name(self):
        return self.name

    # Method to get the person's age
    def get_age(self):
        return self.age

    # Method to set the person's name
    def set_name(self, name):
        self.name = name

    # Method to set the person's age
    def set_age(self, age):
        self.age = age

# Creating an object of the Person class
person1 = Person("Alice", 30)
print(person1.get_name())  # Output: Alice
print(person1.get_age())   # Output: 30

# Using setter methods to change the object's attributes
person1.set_name("Bob")
person1.set_age(25)
print(person1.get_name())  # Output: Bob
print(person1.get_age())   # Output: 25

# Alternative approach using properties
class PersonWithProperties:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

# Creating an object of the PersonWithProperties class
person2 = PersonWithProperties("Charlie", 40)
print(person2.name)  # Output: Charlie
print(person2.age)   # Output: 40

# Using property setters to change the object's attributes
person2.name = "Dave"
person2.age = 35
print(person2.name)  # Output: Dave
print(person2.age)   # Output: 35

# Automation example: Class with a method to increment age
class PersonWithAutomation:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increment_age(self):
        self.age += 1

# Creating an object of the PersonWithAutomation class
person3 = PersonWithAutomation("Eve", 20)
print(person3.age)  # Output: 20

# Incrementing the age using the method
person3.increment_age()
print(person3.age)  # Output: 21

# Another approach: Using class methods
class PersonWithClassMethod:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2023
        age = current_year - birth_year
        return cls(name, age)

# Creating an object using the class method
person4 = PersonWithClassMethod.from_birth_year("Frank", 1990)
print(person4.name)  # Output: Frank
print(person4.age)   # Output: 33

# Static method example
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Using the static method without creating an object
result = MathOperations.add(5, 3)
print(result)  # Output: 8
