class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog Barks.")

class Bird(Animal):
    def sound(self):
        print("birds Sing")

pup = Dog()
pup.sound()

crow = Animal()
crow.sound()

cat = Bird()
cat.sound()
