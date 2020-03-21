class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        self.check_position()

    def turn_left(self):
        dir_dic_left = {"E": "N", "N": "W", "W": "S", "S": "E"}
        self.direction = dir_dic_left.get(self.direction)

    def turn_right(self):
        dir_dic_right = {"N": "E", "W": "N", "S": "W", "E": "S"}
        self.direction = dir_dic_right.get(self.direction)

    def move_forward(self):
        dic_mov_forward = {"N": (self.x, self.y - 1), "S": (self.x, self.y + 1),
                       "E": (self.x + 1, self.y), "W": (self.x -1, self.y)}
        self.x, self.y = dic_mov_forward.get(self.direction)

    def move_backward(self):
        dic_mov_backward = {"N": (self.x, self.y + 1), "S": (self.x, self.y - 1),
                       "E": (self.x - 1, self.y), "W": (self.x + 1, self.y)}
        self.x, self.y = dic_mov_backward.get(self.direction)

    def check_position(self):
        if self.x > self.asteroid.x or self.x < 0:
            raise MissAsteroidError()
        if self.y > self.asteroid.y or self.y < 0:
            raise MissAsteroidError()


class MissAsteroidError(Exception):
    pass
