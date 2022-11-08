class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog) :
    def speak(self, sound ="Bark"):
        return f"{self.name} says {sound}"

biscuit = Dog("Biscuit",2)
cookie = GoldenRetriever("Cookie", 10)

print(biscuit.speak("Ouaf ouaf"))
print(cookie.speak())
print(biscuit.species)
print(cookie)

print(isinstance(cookie,Dog))