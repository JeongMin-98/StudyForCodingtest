"""

    building : Room, porch

    Room => windows
    windows per room

    Porch

    class Room
    class Porch
    class House
    class HouseBuilder

"""


class Room(object):
    """ 방 => 창문있음 """

    def __init__(self, n_windows=2, n_door=1, direction='S'):
        self.n_windows = n_windows
        self.n_door = n_door
        self.direction = direction

    def __str__(self):
        return "방 <방향: %s, 창문 개수: %d>" % (self.direction, self.n_windows)


class Porch(object):
    """ 복도 """

    def __init__(self, n_doors=2, direction='W'):
        self.n_doors = n_doors
        self.direction = direction

    def __str__(self):
        return "복도 <방향: %s, 문 개수: %d>" % (self.direction, self.n_doors)


class House(object):

    def __init__(self, n_windows, n_porches, n_rooms):
        # windows per rooms
        self.n_windows = n_windows
        self.n_porches = n_porches
        self.n_rooms = n_rooms
        self.rooms = []
        self.porches = []

    def __str__(self):
        msg = 'House <방 개수: %d, 복도 개수: %d>\n' % (self.n_rooms, self.n_porches)

        for room in self.rooms:
            msg += str(room) + '\n'

        for porch in self.porches:
            msg += str(porch) + '\n'

        return msg

    def add_room(self, room):
        self.rooms.append(room)

    def add_porch(self, porch):
        self.porches.append(porch)


class HouseBuilder(object):

    def __init__(self, *arg, **kwargs):
        self.house = House(*arg, **kwargs)

    def build(self):

        self.build_rooms()
        self.build_porches()
        return self.house

    def build_rooms(self):

        for i in range(self.house.n_rooms):
            room = Room(n_windows=self.house.n_windows)
            self.house.add_room(room)

    def build_porches(self):
        for i in range(self.house.n_porches):
            porch = Porch()
            self.house.add_porch(porch)


builder = HouseBuilder(n_rooms=2, n_porches=1, n_windows=1)
print(builder.build())
