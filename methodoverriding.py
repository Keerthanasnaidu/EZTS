class Animal:
    def speak():
        return "Animal is speaking"
class Dog(Animal):
    def speak():
        return "dog is barking"
class Cat(Animal):
    def speak():
        return "cat does meow moew"
animal=Animal
dog=Dog
cat=Cat
print(animal.speak())
print(dog.speak())
print(cat.speak())

# calculator
class calculator:
    intro="hey"