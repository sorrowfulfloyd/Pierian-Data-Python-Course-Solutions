'''
TRIED TO GET 10/10 IN PYLINT FOR THIS ONE
An example for 'Inheritance', where you form new classes,
using classes already defined by a base class.
Newly formed classes are called derived classes.
The classes we derive from are called base classes.
Important benefits of using inheritance are code reuse and reduction of complexity.
!Derived classes override or may extend the functionality of base classes!'''

class Animal():
    '''
    BASE CLASS, FOR OTHER ALIKE CLASSES TO GET DERIVED FROM.
    '''
    #METHODS, basically functions inside a class
    def __init__(self):
        print("Animal created")
    @classmethod
    def who_am_i(cls):
        """
        Prints out the name given
        """
        print("Animal")
    @classmethod
    def eat(cls):
        """
        Prints out the name given
        """
        print("Eating")

# Derived class 1, where it uses the base class' 'speak' method.
class Dog(Animal):
    '''
    DERIVED CLASS OF 'Animal'
    This takes and overrides the 'whoAmI' method, and creates some more methods too.
    '''
    def __init__(self):
        """
        When you create an __init__ for a derived class, It no longer uses the base class' class.
        To use the Base class' init func we have to call it first.
        Here, this class inherits the parent's 'eat' method.
        The derived class then also modifies an inherited method.
        And, finally it extends the base functionality of the parent's class
        by adding another method.
        """
        Animal.__init__(self)
        print("Dog created")
    @classmethod
    def who_am_i(cls):
        """
        Prints out the name given
        """
        print("Dog")
    @classmethod
    def bark(cls):
        """
        Makes the dog bark
        """
        print("Woof!")

D = Dog()
print(D.bark())
