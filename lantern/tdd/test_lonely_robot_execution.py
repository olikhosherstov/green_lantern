import pytest
import numpy as np
from lonely_robot import Robot, Asteroid, Obstacle, MissAsteroidError, RobotMovementError


class TestRobotCreation:

    def test_parameters(self):
        # Create asteroid
        x, y = 15, 25
        asteroid = Asteroid(x, y)

        # Create obstacles
        x_a, y_a = 10, 10
        obstacle = Obstacle(x_a, y_a)

        # Add obstacle to Asteroid
        asteroid.add_obstacle(obstacle)
        assert asteroid.get_obstacle_count() == 1
        # Create robot
        direction = "E"
        robot = Robot(x, y, asteroid, direction)

        # Check robot/asteroid/obstacle creation
        assert robot.x == 15
        assert robot.y == 25
        assert robot.direction == direction
        assert robot.asteroid == asteroid
        robot.set_direction("N")
        assert robot.direction == "N"
        assert obstacle.x == 10
        assert obstacle.y == 10


    # Check robot in asteroid landing, obstacle on asteroid creation
    @pytest.mark.parametrize(
        "asteroid_size,robot_obstacle_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_obstacle_coordinates):
        with pytest.raises(MissAsteroidError):
            obstacle = Obstacle(*robot_obstacle_coordinates)
            asteroid = Asteroid(*asteroid_size)
            asteroid.add_obstacle(obstacle)
            Robot(*robot_obstacle_coordinates, asteroid, "W")


class Test_robot_movement:
    # Create asteroid
    x, y = 15, 25
    asteroid = Asteroid(x, y)

    # Test turn left
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

    # Test turn right
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

    #Test move forward
    @pytest.mark.parametrize(
        "current_direction, current_x, current_y, expected_x, expected_y",
        (
                ("N", 8, 25, 8, 26),
                ("S", 7, 0, 7, -1),
                ("E", 15, 7, 16, 7),
                ("W", 0, 7, -1, 7),
        )
    )
    def test_move_forward(self, current_direction, current_x, current_y, expected_x, expected_y):
        robot = Robot(current_x, current_y, self.asteroid, current_direction)
        robot.move_forward()
        assert robot.x == expected_x and robot.y == expected_y
        # Check if it try to falls from asteroid during movement or get obstacle and make corretion of position
        with pytest.raises(RobotMovementError):
            robot.check_position_movement()
            assert current_x == robot.x and current_y == robot.y

    #Test move backward
    @pytest.mark.parametrize(
        "current_direction, current_x, current_y, expected_x, expected_y",
        (
                ("N", 7, 0, 7, -1),
                ("S", 8, 25, 8, 26),
                ("E", 0, 7, -1, 7),
                ("W", 15, 7, 16, 7),
        )
    )
    def test_move_backward(self, current_direction, current_x, current_y, expected_x, expected_y):
        robot = Robot(current_x, current_y, self.asteroid, current_direction)
        robot.move_backward()
        assert robot.x == expected_x and robot.y == expected_y
        # Check if it try to falls from asteroid during movement or get obstacle and make corretion of position
        with pytest.raises(RobotMovementError):
            robot.check_position_movement()
            assert current_x == robot.x and current_y == robot.y


class Test_robot_scan_ability:
    asteroid = Asteroid(4, 4)
    asteroid.add_obstacle(Obstacle(0, 3))
    asteroid.add_obstacle(Obstacle(4, 3))
    asteroid.add_obstacle(Obstacle(2, 0))
    asteroid.add_obstacle(Obstacle(2, 1))
    asteroid.add_obstacle(Obstacle(2, 4))
    asteroid.add_obstacle(Obstacle(1, 1))
    robot = Robot(2, 3, asteroid, "S")
    #map of the asteroid 5x5.
    #legend: 0 - valley; 1 - obstacle; 2 - robot position
    map = np.array([[0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [1, 1, 0, 2, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0]
                   ], 'i')

    def test_spatial_scan(self):
        #This method is test scanned asteroid map creation
        self.robot.scan_create_map()
        assert np.array_equal(self.robot.aster_map, self.map)

    def test_get_obstacle_on_view_direction(self):
        # This method is test finding of obstacles
        self.robot.set_direction("S")
        assert self.robot.get_obstacle_on_view_direction() == [(0,3)]
        self.robot.set_direction("N")
        assert self.robot.get_obstacle_on_view_direction() == [(4, 3)]
        self.robot.set_direction("E")
        assert self.robot.get_obstacle_on_view_direction() == [(2, 0), (2, 1)]
        self.robot.set_direction("W")
        assert self.robot.get_obstacle_on_view_direction() == [(2, 4)]




