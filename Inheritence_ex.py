#Inheritance is the procedure in which one class inherits the attributes and methods of another class.
# The class whose properties and methods are inherited is known as the Parent class.
# And the class that inherits the properties from the parent class is the Child class


class Animal(): ##This is the base class

    def __init__(self):
        print("Animal class created")

    def who_am_i(self):
        print("i am animal")

    def eating(self):
        print("i am eating")

my_animal=Animal()

class Dog(Animal): #This is the base class and inheriting properties of animal class.

    def __init__(self):
        Animal.__init__(self)
        print("Dog class created")

    def breed(self):
        print("indian breed")

    def eating(self):
        print("i am dog and i am eating")
my_dog=Dog()

my_dog.eating()
my_dog.who_am_i()
