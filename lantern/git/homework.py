"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
<<<<<<< HEAD
    return first == second
=======

    if (isinstance(first, (list, tuple, set))) & (isinstance(second, (list, tuple, set))):
        return len(set(first).intersection(set(second))) == len(set(first)) == len(set(second))
    else:
        return first == second

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
<<<<<<< HEAD
=======

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860
    return first is second


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise TypeError
    Raises:
        TypeError
    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
<<<<<<< HEAD
=======

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860
    if not isinstance(first_value, int) or not isinstance(second_value, int):
        raise TypeError("Input data must be integer")
    return first_value * second_value


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError
    Args:
        first_value: number for multiply
        second_value: number for multiply
    Raises:
        ValueError
    Returns: multiple of two numbers.
    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    try:
<<<<<<< HEAD
        first_value = int(first_value)
        second_value = int(second_value)
        return first_value * second_value
    except (ValueError, TypeError):
        raise ValueError("Not valid input data")
=======
        first_value_c = int(first_value)
        second_value_c = int(second_value)
        return first_value_c * second_value_c
    except (ValueError, TypeError):
        raise Exception(ValueError)

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.
    Args:
        word: Searchable substring
        text: Text for search
    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
<<<<<<< HEAD
        >>> False
=======

      #  >>> False

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860
    """
    return word in text


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
<<<<<<< HEAD
    return [i for i in range(0, 13) if i != 6 and i != 7]
=======

    chk = [6, 7]

    return [x for x in range(0, 13) if x not in chk]

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
<<<<<<< HEAD
    return [i for i in data if i > 0]
=======

    return [x for x in data if x >= 0]

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860


def alphabet() -> dict:
    """
    Create dict which keys are alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
<<<<<<< HEAD
    from string import ascii_lowercase
    return dict(enumerate(ascii_lowercase, start=1))
=======

    return {chr(96 + i) : i for i in range(1, 27)}

>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860

def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    """
<<<<<<< HEAD
    sorted_list = []
    new_data = data.copy()
    while new_data:
        minimum = new_data[0]
        for i in new_data:
            if i < minimum:
                minimum = i
        sorted_list.append(minimum)
        new_data.remove(minimum)

    return sorted_list
=======

    result = data[:]
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


>>>>>>> e6737f0753107c3ebb27b8d61a6ea5aa0f82c860
