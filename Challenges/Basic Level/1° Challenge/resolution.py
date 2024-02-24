class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hello {self.name}, it's a pleasure to have you here! \n Let's code and explore the world."

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


p = Person("Leonardo", "25")
s = p.greeting()
print(s)
