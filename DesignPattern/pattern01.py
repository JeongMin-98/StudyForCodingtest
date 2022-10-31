"""

    use prototype factory


"""

from prototype import SPrototype
from prototypefactory import PrototypeFactory


class Name(SPrototype):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return ' '.join((self.first, self.second))


class Animal(SPrototype):

    def __init__(self, name, type='Wild'):
        self.name = name
        self.type = type

    def __str__(self):
        return ' '.join((self.name, self.type))


if __name__ == '__main__':
    name = Name('Jeongmin', 'kim')
    animal = Animal('Dog', 'house')
    print(name)
    print(animal)

    factory = PrototypeFactory()

    factory.register(animal)
    factory.register(name)

    Name1 = factory.clone(Name)
    animal1 = factory.clone(Animal)

    print(name is Name1)
    print(animal is  animal1)
