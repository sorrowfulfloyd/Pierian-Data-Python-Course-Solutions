'''
While functions can take different arguments,
methods belonging to functions can take this one step further.
Polymorphism refers to the way in which different object classes-
can share the same method name, and those methods can be called from
the same place even though a variety of different objects might be passed in.
'''

# In example:

class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says meow!'

NIKO = Dog('Niko')
FELIX = Cat('Felix')

print(Niko.speak())
print(Felix.speak())
