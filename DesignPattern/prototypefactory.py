from borg import Borg


class PrototypeFactory(Borg):
    """ A prototype factory/registry class """

    def __init__(self):
        self._registry = {}

    def register(self, instance):
        self._registry[instance.__class__] = instance

    def clone(self, klass):
        instance = self._registry.get(klass)
        if instance is None:
            print('Error: ', klass, 'not registered')
        else:
            return instance.clone()
