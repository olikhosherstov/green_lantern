class Cat:
    """
    Write Class Cat which will receive age from user
    * Add to class average_speed variable which will get it's values
      from private method _set_average_speed()
    * Add to class saturation_level variable with value 50
    * Implement private methods _increase_saturation_level and _reduce_saturation_level
      that will receive value and add/subtract from saturation_level this value
      if saturation_level is less than 0, return 0
      if saturation_level is grosser than 100, return 100
    * Implement method eat which will receive from user product value
      if product eq fodder use _increase_saturation_level with value eq 10
      if product eq apple use _increase_saturation_level with value eq 5
      if product eq milk use _increase_saturation_level with value eq 2
    * Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6
    * Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run less or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50
      return text like this: f"Your cat ran {ran_km} kilometers"
    * Implement get_saturation_level and return saturation_level
      if saturation_level eq 0 return text like this: "Your cat is dead :("
    * Implement get_average_speed and return average_speed
    """

    def __init__(self, age):
        self.age = age
        self.average_speed = self._set_average_speed()
        self.saturation_level = 50

    def eat(self, product):
        meal = {'fodder': 10, 'apple': 5, 'milk': 2}
        self._increase_saturation_level(meal.get(product, 0))

    def _reduce_saturation_level(self, value):
        self.saturation_level -= value
        if self.saturation_level < 0: self.saturation_level = 0

    def _increase_saturation_level(self, value):
        self.saturation_level += value
        if self.saturation_level > 100: self.saturation_level = 100

    def _set_average_speed(self):
        return {
            self.age > 10: 6,
            self.age <= 10: 9,
            self.age <= 7: 12
        }.get(True)

    def run(self, hours):
        km = self.average_speed * hours
        self._reduce_saturation_level({
                                          km > 200: 50,
                                          km <= 200: 25,
                                          km <= 100: 15,
                                          km <= 50: 5,
                                          km <= 25: 2
                                      }.get(True))
        return f"Your cat was ran {km} kilometers. :-)"

    def get_saturation_level(self):
        return self.saturation_level if self.saturation_level > 0 else 'Your cat is died :('

    def get_average_speed(self):
        return self.average_speed


class Cheetah(Cat):
    """
    * Inherit from class Cat
    * Redefine method eat from parent class it will receive product value
      if product eq gazelle use _increase_saturation_level from parent class with value 30
      if product eq rabbit use _increase_saturation_level from parent class with value 15
    * Redefine method _set_average_speed
      if age less or eq 5 return 90
      if age between 5 and 15(including) return 75
      if age grosser 15(not including) return 40
    """

    def __init__(self, age):
        super().__init__(age)

    def eat(self, product):
        meal = {'gazelle': 30, 'rabbit': 15}
        self._increase_saturation_level(meal.get(product, 0))

    def _set_average_speed(self):
        return {
            self.age > 15: 40,
            self.age <= 15: 75,
            self.age <= 5: 90
        }.get(True)


class Wall:
    """
    * Implement class Wall which receives such parameters: width and height

    * Implement method wall_square which return result of simple square formula of rectangle

    * Implement method number_of_rolls_of_wallpaper which receives such parameters: roll_width_m, roll_length_m
      (_m in the parameters name means meters) return number of rolls of wallpaper

      Example:
          count of lines in roll eq roll length in meters divide height of the wall (use rounding down)
          count of lines eq width of the wall divide roll width in meters
          number of rolls of wallpaper eq count of lines divide  count of lines in roll
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        from math import floor
        return floor(self.width / roll_width_m) / floor(roll_length_m / self.height)


class Roof:
    """
        * Implement class Roof which receives such parameters: width, height and roof_type
        * Implement method roof_square that returns square of the roof
          if roof_type eq "gable" the roof square if simple rectangle square formula multiplied 2
          if roof_type eq "single-pitch" the roof square if simple rectangle square formula
          if other roof_type raise ValueError like this "Sorry there is only two types of roofs"
    """

    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        d_roof = {'gable': lambda h, w: h * w * 2,
                  'single-pitch': lambda h, w: h * w}
        if self.roof_type in d_roof:
            return d_roof.get(self.roof_type)(self.height, self.width)
        else:
            raise ValueError('Sorry there is only two types of roofs')


class Window:
    """
       * Implement class Window which receives such parameters: width and height
       * Implement method window_square which return result of simple square formula of rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        return self.height * self.width


class Door:
    """
     * Implement class Door which receives such parameters: width and height
      add variables wood_price eq 10, metal_price eq 3
     * Implement method door_square which return result of simple square formula of rectangle
     * Implement method door_square which receives material value as a parameter
       if material eq wood return door_square multiplied on wood_price
       if material eq metal return door_square multiplied on metal_price
       if material value is another one (not metal or wood) raise ValueError "Sorry we don't have such material"
     *  Implement method update_wood_price which receives new_price value and updates your old price
     *  Implement method update_metal_price which receives new_price value and updates your old price
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wood_price = 10
        self.metal_price = 3

    def door_square(self):
        return self.height * self.width

    def door_price(self, value):
        # if value == "wood":
        #     return self.door_square() * self.wood_price
        # elif value == "metal":
        #     return self.door_square() * self.metal_price
        # else:
        #     raise ValueError("Sorry we don't have such material")
        dic_mat = {"wood": self.wood_price,
                   "metal": self.metal_price}
        if dic_mat.get(value):
            return self.door_square() * dic_mat.get(value)
        else:
            raise ValueError('Sorry we don\'t have such material')

    def update_wood_price(self, new_price):
        self.wood_price = new_price

    def update_metal_price(self, new_price):
        self.metal_price = new_price


def null_check(width, height):
    if width <= 0 or height <= 0:
        raise ValueError('Value must be not 0')


class House:
    """
    !!!! DON'T WRITE NEW METHODS TO THIS CLASS EXCEPT FOR THOSE LISTED BELOW !!!

    * Add super private variable __walls and its value will be empty list
    * Add super private variable __windows and its value will be empty list
    * Add super private variable __roof and its value will be None
    * Add super private variable __door and its value will be None

    * Implement method create_wall which will create new wall using class Wall and add it to the __walls list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      if user have more than 4 walls raise ValueError "Our house can not have more than 4 walls"

    * Implement method create_roof which will create new roof using class Roof and assign it to the __roof variable
      it receives parameters width, height and roof_type
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another roof if we already have another one,
              otherwise raise ValueError "The house can not have two roofs"

    * Implement method create_window which will create new window using class Window and add it to the __windows list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"

    * Implement method create_door which will create new door using class Door and assign it to the __door variable
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another door if we already have another one,
              otherwise raise ValueError "The house can not have two doors"

    * Implement method get_count_of_walls that returns count of walls

    * Implement method get_count_of_windows that returns count of windows

    * Implement method get_door_price that receives material value and returns price of the door

    * Implement method update_wood_price that receives new_wood_price and updates old one

    * Implement method update_metal_price that receives new_metal_price and updates old one

    * Implement method get_roof_square that returns the roof square

    * Implement method get_walls_square that returns sum of all walls square that we have

    * Implement method get_windows_square that returns sum of all windows square that we have

    * Implement method get_door_square that returns the square of the door

    * Implement method get_number_of_rolls_of_wallpapers that returns sum of the number of rolls of wallpapers
      needed for all our walls
      it receives roll_width_m, roll_length_m parameters
      Check if roll_width_m or roll_length_m eq 0 raise ValueError "Sorry length must be not 0"

    * Implement method get_room_square that returns the square of our room
      (from walls_square divide windows and door square)

    """

    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None
        # Declare pet on the house :-)
        self.__pet = None

    def create_wall(self, width, height):
        null_check(width, height)
        if len(self.__walls) == 4:
            raise ValueError('Our house can not have more than 4 walls')

        self.__walls.append(Wall(width, height))

        # is our house have rectangle or square form?
        if len(self.__walls) == 4:
            form_factor = [i_wall.width for i_wall in self.__walls]
            if len(set(form_factor)) > 2:
                self.__walls = []
                raise ValueError('Your are have not rectangle or square form factor :-(')

    def create_roof(self, width, height, roof_type):
        r_type = ['gable', 'single-pitch']
        null_check(width, height)
        if self.__roof:
            raise ValueError('The house can not have two roofs')
        if roof_type not in r_type:
            raise ValueError('Sorry there is only two types of roofs: gable and single-pitch')
        self.__roof = Roof(width, height, roof_type)

    def create_window(self, width, height):
        null_check(width, height)
        self.__windows.append(Window(width, height))

    def create_door(self, width, height):
        null_check(width, height)
        if self.__door:
            raise ValueError('The house can not have two doors')
        self.__door = Door(width, height)

    # Put pet on the house :-)
    def __create_pet(self, age):
        self.__pet = Cat(age)

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material):
        return self.__door.door_price(material)

    def update_wood_price(self, new_wood_price):
        self.__door.update_wood_price(new_wood_price)

    def update_metal_price(self, new_metal_price):
        self.__door.update_metal_price(new_metal_price)

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        return sum(i_wall.wall_square() for i_wall in self.__walls)

    def get_windows_square(self):
        return sum(i_window.window_square() for i_window in self.__windows)

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        null_check(roll_width_m, roll_length_m)
        return sum(wall.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m) for wall in self.__walls)

    def get_room_square(self):
        return self.get_walls_square() - self.get_windows_square() - self.get_door_square()

    # Pet action :-)
    def __damage_wallpapers(self, hours):
        if self.__pet.run(hours) * 1000 * 0.1 >= self.get_walls_square():
            return 'Wallpapers is need repair!'
        else:
            return f'Pet was damage {self.__pet.run(hours) * 1000 * 0.1} sq.m of wallpapers'


if __name__ == '__main__':
    from math import floor

    house = House()
    try:
        house.create_wall(11, 2.5)
        house.create_wall(10, 2.5)
        house.create_wall(15, 2.5)
        house.create_wall(14, 2.5)
    except ValueError:
        print('try to create none rectangle house. everything ok')

    house.create_wall(10, 2.5)
    house.create_wall(10, 2.5)
    house.create_wall(14, 2.5)
    house.create_wall(14, 2.5)

    try:
        house.create_wall(14, 2.5)
    except ValueError:
        print('try to create fifth wall. everything ok')
    try:
        house.create_roof(10, 6, 'some type')
    except ValueError:
        print('try to create some_type roof . everything ok')

    house.create_roof(10, 6, 'single-pitch')

    house.create_door(1, 2)
    house.create_window(3, 1)

    print("Test house:")
    print(f'Walls square -> {house.get_walls_square()}')
    print(f'Windows square -> {house.get_windows_square()}')
    print(f'Door square -> {house.get_door_square()}')
    print(f'Actual number of wallpaper: {house.get_number_of_rolls_of_wallpapers(0.53, 10)}')
    print(f'Except number of wallpaper: {22}')
