import numpy as np


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obstacles = []

    def add_obstacle(self, obstacle: Obstacle):
        self.obstacles.append(obstacle)

    def check_obstacle_position(self, obstacle: Obstacle):
        if any([self.x < obstacle.x, obstacle.x < 0, self.y < obstacle.y, obstacle.y < 0]):
            raise MissAsteroidError()

    def get_asteroid_size(self):
        return (self.x, self.y)

    def get_obstacle_count(self):
        # method return number of obstacles
        return len(self.obstacles)


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        self.aster_map = np.zeros([self.asteroid.x + 1, self.asteroid.y + 1])

    def set_direction(self, direction: str):
        self.direction = direction

    def turn_left(self):
        dir_dic_left = {"E": "N", "N": "W", "W": "S", "S": "E"}
        self.direction = dir_dic_left.get(self.direction)

    def turn_right(self):
        dir_dic_right = {"N": "E", "W": "N", "S": "W", "E": "S"}
        self.direction = dir_dic_right.get(self.direction)

    def move_forward(self):
        dic_mov_forward = {"N": (self.x, self.y + 1), "S": (self.x, self.y - 1),
                           "E": (self.x + 1, self.y), "W": (self.x - 1, self.y)}
        self.x, self.y = dic_mov_forward.get(self.direction)

    def move_backward(self):
        dic_mov_backward = {"N": (self.x, self.y - 1), "S": (self.x, self.y + 1),
                            "E": (self.x - 1, self.y), "W": (self.x + 1, self.y)}
        self.x, self.y = dic_mov_backward.get(self.direction)

    def check_position_on_asteroid(self):
        # this method check if robot crashed during landing on asteroid
        if any([self.asteroid.x < self.x, self.x < 0, self.asteroid.y < self.y, self.y < 0]):
            raise MissAsteroidError()

    def check_for_block(self):
        for barrier in self.asteroid.obstacles:
            if all([self.x == barrier.x, self.y == barrier.y]):
                raise ObstacleCrashError()

    def scan_create_map(self):
        # this method create map with obstacles and robot position
        self.aster_map[self.x, self.y] = 2
        for block in self.asteroid.obstacles:
            self.aster_map[block.x, block.y] = 1

    def get_obstacle_on_view_direction(self):
        # This method return obstacles on view direction
        resalt = []
        if self.direction == "N":
            for i in np.where(self.aster_map[self.x:, self.y] == 1)[0]:
                resalt.append((i + self.x, self.y))
            return resalt
        if self.direction == "S":
            for i in np.where(self.aster_map[:self.x, self.y] == 1)[0]:
                resalt.append((i, self.y))
            return resalt
        if self.direction == "E":
            for i in np.where(self.aster_map[self.x, :self.y] == 1)[0]:
                resalt.append((self.x, i))
            return resalt
        if self.direction == "W":
            for i in np.where(self.aster_map[self.x, self.y:] == 1)[0]:
                resalt.append((self.x, self.y + i))
            return resalt


class MissAsteroidError(Exception):
    pass


class ObstacleCrashError(Exception):
    pass
