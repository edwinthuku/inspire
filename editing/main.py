#oop
#definiing a classand its attribute.
#creating instances (object) of a class.
#class methods(functinig belonging to a class)
#Inheritance & Polymorphism.
#Method overriding.

class Dog:
    def __init__(self , no_of_eye , color):
        self.no_of_eyes=no_of_eye
        self.color=color

         
        german_shephard=Dog(no_of_eye=2, color='grey')
        dodger = Dog(color='white',no_of_eyes=1)
        dobberman=Dog(2,"brown")
        print(german_shephard.color,german_shephard.no_of_eyes)
        print(dodger.no_of_eyes,dodger.color)
        print(dobberman.no_of_eyes,dobberman)

dobberman.color="black"
print(dobberman.color)


german_shephard=Dog(no_of_eye=2, color='white')
dodger = Dog(color='white',no_of_eye=3)
print(german_shephard.color,german_shephard.no_of_eyes)
print(dorger.color,dorger.no_of_eyes)