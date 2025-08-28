class Animal:
    def move(self):
        print("This animal moves in some way.")

# Subclass: Dog
class Dog(Animal):
    def move(self):
        print("Dog runs on four legs.")

# Subclass: Bird
class Bird(Animal):
    def move(self):
        print("Bird flies in the sky.")

# Subclass: Fish
class Fish(Animal):
    def move(self):
        print("Fish swims in water.")

# List of animals
animals = [Dog(), Bird(), Fish()]

# Demonstrate polymorphism
for animal in animals:
    animal.move()
