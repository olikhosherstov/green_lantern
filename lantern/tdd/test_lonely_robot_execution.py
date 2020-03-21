import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


class TestRobotCreation:

    def test_parameters(self):
        x, y = 15, 25
        asteroid = Asteroid(x, y)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 15
        assert robot.y == 25
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class Test_robot_movement:
    x, y = 15, 25
    asteroid = Asteroid(x, y)

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N"),
        )
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("W", "N"),
                ("S", "W"),
                ("E", "S"),
                ("N", "E"),
        )
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.direction = current_direction
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, current_x, current_y, expected_x, expected_y",
        (
                ("N", 7, 0, 7, -1),
                ("S", 8, 25, 8, 26),
                ("E", 15, 7, 16, 7),
                ("W", 0, 7, -1, 7),
        )
    )
    def test_move_forward(self, current_direction, current_x, current_y, expected_x, expected_y):
        robot = Robot(current_x, current_y, self.asteroid, current_direction)
        robot.move_forward()
        assert robot.x == expected_x and robot.y == expected_y
        # Check if it falls from asteroid during movement
        with pytest.raises(MissAsteroidError):
            robot.check_position()

    @pytest.mark.parametrize(
        "current_direction, current_x, current_y, expected_x, expected_y",
        (
                ("N", 8, 25, 8, 26),
                ("S", 7, 0, 7, -1),
                ("E", 0, 7, -1, 7),
                ("W", 15, 7, 16, 7),
        )
    )
    def test_move_backward(self, current_direction, current_x, current_y, expected_x, expected_y):
        robot = Robot(current_x, current_y, self.asteroid, current_direction)
        robot.move_backward()
        assert robot.x == expected_x and robot.y == expected_y
        #Check if it falls from asteroid during movement
        with pytest.raises(MissAsteroidError):
            robot.check_position()
