# singleton.py
# 파이썬을 활용한 소프트웨어 아키텍처를 참고함
class Singleton(object):
    """ singleton in python """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


def test_single(cls):
    return cls() == cls()


class MetaSingleton(type):

    def __init__(cls, *args):
        print(cls, "__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance


class SingletonM(metaclass=MetaSingleton):
    pass


