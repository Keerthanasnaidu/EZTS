#single inheritence
class parent:
    def parent_method():
        return "I'm parent method"
class child(parent):
    def child_method():
        return "i'm child method,derived from parent method"
        
obj1=child
print(obj1.child_method())
print(obj1.parent_method())

#multilevel inheritence
class animal:
    def animal_level_1_method():
        return "im animal method"
    
class dog(animal):
    def dog_level_2_method():
        return "im dog method,im inherited form class animal"
    
class puppy(dog):
    def puppy_level_3_method():
        return "im puppy method, iminherited form class dog"

obj1=puppy
print(obj1.animal_level_1_method())
print(obj1.dog_level_2_method())
print(obj1.puppy_level_3_method())
