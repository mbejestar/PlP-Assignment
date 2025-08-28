class Superhero:
    def __init__(self, name, power):
        self.__name = name  # Encapsulated attribute
        self.__power = power

    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def fight(self):
        print(f"{self.__name} fights with {self.__power}!")

# Derived class: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, flight_speed):
        super().__init__(name, power)
        self.__flight_speed = flight_speed

    def fly(self):
        print(f"{self.get_name()} is flying at {self.__flight_speed} km/h!")

# Usage
hero1 = Superhero("Iron Fist", "Martial Arts")
hero2 = FlyingSuperhero("Superman", "Super Strength", 900)

hero1.fight()
hero2.fight()
hero2.fly()
