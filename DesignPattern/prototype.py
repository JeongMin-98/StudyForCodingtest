import copy

"""
    copy 얕은 복사를 사용할 경우
    모든 객체가 참조를 통해 복사됨을 알 수 있음
    튜플이나 문자열 같은 불변 객체는 변경할 수 없기 때문에 아무런 문제가 되지않지만,
    리스트나 딕셔너리 같이 변경 가능한 객체는 인스턴스의 상태가 인스턴스에 의해 완전히 소유되지않고 공유되기 때문에
    문제가 된다. 한 인스턴스에서 변경한 모든 수정사항은 복제된 인스턴스의 동일한 객체를 수정할 것이다. 
"""


class SPrototype(object):
    """ A prototype base class with use shallow copy """

    def clone(self):
        return copy.copy(self)


class SRegister(SPrototype):

    def __init__(self, names=[]):
        self.names = names


class Prototype(object):
    """ A prototype base class """

    def clone(self):
        """ Return a clone of self """
        return copy.deepcopy(self)


class Register(Prototype):
    """ A student Register class """

    def __init__(self, names=[]):
        self.names = names


"""
    make Prototype class with metaclass
"""


class MetaPrototype(type):
    """ A metaclass for Prototypes """

    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.clone = lambda self: copy.deepcopy(self)


class MetaSingletonPrototype(type):
    """ A metaclass for singleton & prototype patterns """

    def __init__(cls, *args):
        print(cls, "__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None
        cls.clone = lambda self: copy.deepcopy(cls.instance)

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance


class PrototypeM(metaclass=MetaSingletonPrototype):
    pass


class ItemCollection(PrototypeM):
    def __init__(self, items=[]):
        self.items = items


if __name__ == '__main__':
    r1 = Register(names=['amy', 'stu', 'jack'])
    r2 = r1.clone()

    rs1 = SRegister(names=['amy', 'stu', 'jack'])
    rs2 = rs1.clone()

    print(r1)
    print(r2)
    print(r2.__class__)

    print('Prototype base class with shallow copy')
    print(rs1)
    print(rs1)

    rs1.names.append('bob')
    print(rs2.names)

    print(r1.names is r2.names)

    print('============MetaClass for singleton========')
    i1 = ItemCollection(items=['apple', 'samsung', 'Kakao'])
    print(i1)
    i2 = i1.clone()
    print(i2)
    print(i2.items is i1.items)
    i3 = ItemCollection(items=['apple', 'samsung', 'Kakao'])
    print(i3 is i1)
