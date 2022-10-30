from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """ An Employee class """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return "{} - {}, {} years old {}".format(self.__class__.__name__,
                                                 self.name,
                                                 self.age,
                                                 self.gender
                                                 )


class Engineer(Employee):
    """ Engineer Employee """

    def get_role(self):
        return "engineering"


class Accountant(Employee):
    """ Accountant Employee """

    def get_role(self):
        return 'Accountant'


class Admin(Employee):
    """ An Admin Employee """

    def get_role(self):
        return 'Administration'


class EmployeeFactory(object):
    """ Employee Factory class """

    @classmethod
    def create(cls, name, *args):

        name = name.lower().strip()

        if name == 'engineer':
            return Engineer(*args)
        elif name == 'accountant':
            return Accountant(*args)
        elif name == 'admin':
            return Admin(*args)


if __name__ == '__main__':
    factory = EmployeeFactory()
    print(factory.create('engineer', 'Kim', 25, 'M'))
    print(factory.create('engineer', 'Wang', 25, 'F'))
    accountant = factory.create('accountant', 'Hema', 39, 'F')
    print(accountant)
    print(accountant.get_role())
    admin = factory.create('Admin', 'Supritha', 32, 'F')
    print(admin.get_role())
