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

