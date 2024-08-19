

def my_planet(method):
    def inner(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if self.name == "Earth":
            print("You are on Earth")
        return result
    return inner


def planet_age(method):
    def inner(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if self.age < 18:
            print("You are a baby planet")
        else:
            print("You are an adult planet")
        return result
    return inner


class Planet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @my_planet
    def say_name(self):
        return f"Hello, I am {self.name}"

    @planet_age
    def planet_age(self):
        return f"I am {self.age} years old"


earth = Planet("Earth", 19)
earth.say_name()
earth.planet_age()
