class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ == self.__shared_state


class IBorg(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.state = 'init'

    def __str__(self):
        return self.state

