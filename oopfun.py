class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says woof'

class Cat():
    def __init__(self,*name):
        self.name = name
    def speak(self):
        for i in self.name:
            return ' and '.join((self.name)) + ' says meow'

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('One must use a subclass to use that functionality.')

def pet_speak(pet):
    print(pet.speak())

bruh = Dog('Huh')
kek = Cat('Kek', 'Xd')

pet_speak(kek)


