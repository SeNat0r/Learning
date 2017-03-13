class Player(object):
    def __init__(self, nickname):
        self.nickname = nickname
        self.number_of_ships = 10


class Ship(object):
    def __init__(self, decks):
        self.decks = decks

    def position(self, position):
        pass


class Field(object):
    def __init__(self):
        self.height = 10
        self.width = 10


class event_sheet(Player, Ship):
    def attack(self, point):
        pass
