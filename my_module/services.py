import random
import datetime

from .validations import validate_number_is_integer, validate_id_with_Regex
from .utils import convert_string

def populate_array_numbers(array: list, quantity_elements: int) -> list:
    """
    Populates an array with a specified number of integer elements provided by the user.

    Parameters:
        array (list): The array to populate.
        quantity_elements (int): The number of elements to populate in the array.

    Returns:
        :result: list, The populated array.

    Examples:
        >>> populate_array_numbers([], 3)
        Ingrese el 1° número:
        5
        Ingrese el 2° número:
        7
        Ingrese el 3° número:
        10
        [5, 7, 10]
    """
    for i in range(quantity_elements):
        number = input(f"Ingrese el {i + 1}° número:\n")
        number_is_integer = validate_number_is_integer(number)
        while number_is_integer == False:
            print("[ERROR] El número ingresado no es entero.")
            number = input(f"Ingrese el {i + 1}° número nuevamente:\n")
            number_is_integer = validate_number_is_integer(number)
            
        array.append(int(number))
    return array

def populate_options_to_menu() -> list:
    """
    Populates a menu with options provided by the user.

    Returns:
        :result: list, A list containing menu options.

    Example:
        >>> populate_options_to_menu()
        Ingrese la 1° opción
        Option 1
        Desea continuar? y/n
        y
        Ingrese la 2° opción
        Option 2
        Desea continuar? y/n
        n
        ['1) Option 1\n', '2) Option 2\n']
    """
    menu_continue = True
    menu_array = []
    index_of_menu = 1
    while menu_continue:
        option = input(f"Ingrese la {index_of_menu}° opción\n")
        if option == None:
            print("[ERROR] Ingrese nuevamente la opción")
            option = input(f"Ingrese la {index_of_menu}° opción\n")
        else:
            menu_array.append(f"{index_of_menu}) {option}\n")
            index_of_menu += 1
            wish_continue = input("Desea continuar? y/n\n")
            wish_continue = convert_string(wish_continue, "lower")
            if (wish_continue == "n"):
                menu_continue = False
    return menu_array

def array_replace_occurency(array: list, ocurrency: int | str | float, value_replace: int | str | float) -> list:
    """
    Replaces all occurrences of a specific value in a given array with another value.

    Parameters:
        array (list): The array in which to replace occurrences.
        ocurrency (int | str | float): The value to be replaced.
        value_replace (int | str | float): The value to replace occurrences with.

    Returns:
        :result: list, The array with replacements made.

    Example:
        >>> array_replace_occurency([1, 2, 3, 2, 4, 5], 2, 0)
        [1, 0, 3, 0, 4, 5]
        >>> array_replace_occurency(["apple", "banana", "apple", "grape"], "apple", "orange")
        ['orange', 'banana', 'orange', 'grape']
    """
    new_array = []
    for index in range(0, len(array)):
        if array[index] == ocurrency:
            new_array.append(value_replace)
        else:
            new_array.append(array[index])
    return new_array

def array_delete_value_from_array(array: list, value_to_delete: int | float | str) -> list:
    """
    Deletes all occurrences of a specific number from a given array.

    Parameters:
        array (list): The array from which to delete occurrences.
        number_to_delete (int): The number to delete from the array.

    Returns:
        :result: list, The array with occurrences of the specified number removed.

    Example:
        >>> array_delete_number_from_array([1, 2, 3, 2, 4, 5], 2)
        [1, 3, 4, 5]
    """
    new_array = []
    for index in range(0, len(array)):
        if array[index] != value_to_delete:
            new_array.append(array[index])
    return new_array

def array_delete_value_by_index(array: list, index_to_delete: int) -> list:
    """
    Deletes the element at the specified index from a given array.

    Parameters:
        array (list): The array from which to delete the element.
        index_to_delete (int): The index of the element to delete.

    Returns:
        :result: list, The array with the element at the specified index removed.

    Example:
        >>> array_delete_number_from_array_by_index([1, 2, 3, 4, 5], 2)
        [1, 2, 4, 5]
    """
    new_array = []
    for index in range(0, len(array)):
        if index != index_to_delete:
            new_array.append(array[index])
    return new_array

def array_delete_value_by_index_return_value_deleted(array: list, index_to_delete: int) : #-> any | None:
    """
    Deletes a value from the array at the specified index and returns the deleted value.

    Parameters:
        array (list): The array from which to delete the value.
        index_to_delete (int): The index of the value to delete.

    Returns:
        :result: any | None, The deleted value from the array, or None if the index is out of range.

    Example:
        >>> array_delete_value_by_index_return_value_deleted(["apple", "banana", "orange"], 1)
        'banana'
    """
    value_deleted = None
    for index in range(0, len(array)):
        if index == index_to_delete:
            value_deleted = array.pop(index)
    return value_deleted

def array_update_value_from_array_by_index(array: list, index_to_update: int, value_to_update: str) -> list:
    """
    Updates a value in the array at the specified index.

    Parameters:
        array (list): The array in which to update the value.
        index_to_update (int): The index of the value to update.
        value_to_update (str): The new value to assign at the specified index.

    Returns:
        :result: list, The updated array.

    Example:
        >>> array_update_value_from_array_by_index(["apple", "banana", "orange"], 1, "grape")
        ['apple', 'grape', 'orange']
    """
    for index in range(0, len(array)):
        if index == index_to_update:
            array[index] = value_to_update
    return array

def generate_id() -> str:
    """
    Generates a unique identifier consisting of a random four-digit number followed by three random lowercase letters.

    Returns:
        :result: str, The generated unique identifier.

    Example:
        >>> generate_id()
        '1234abc'
    """
    uuid = random.randint(1000, 9999)
    uuid = str(uuid)
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    for i in range(3):
        letter += random.choice("abcdefghijklmnopqrstuvwxyz")
    return f"{uuid}{letter}"

def generate_id_v2() -> int:
    """
    Generates a unique identifier consisting of the current date and time followed by two random lowercase letters.

    Returns:
        :result: int, The generated unique identifier.

    Example:
        >>> generate_id_v2()
        20211014123456ab
    """
    actual_datetime = datetime.datetime.now()
    chars = random.choices("abcdefghijklmnopqrstuvwxyz", k=2)
    id = int(actual_datetime.strftime("%Y%m%d%H%M%S"))
    return f"{id}{chars[0]}{chars[1]}" 

def generate_id_product() -> str | None:
    first_four_numbers = random.choices("0123456789", k=4)
    last_two_strings = random.choices("abcdefghijklmnopqrstuvwxyz", k=2)
    first_four_numbers = "".join(first_four_numbers)
    last_two_strings = "".join(last_two_strings).upper()
    new_id = f"{first_four_numbers}-{last_two_strings}"
    if validate_id_with_Regex(new_id):
        return new_id
    else:
        return None

def array_get_appended_array(array: list, value_to_append: any) -> list:
    """
    Appends a value to the given array and returns the modified array.

    Parameters:
        array (list): The array to which the value will be appended.
        value_to_append (int | str | float): The value to append to the array.

    Returns:
        :result: list, The modified array after appending the value.

    Example:
        >>> array_get_appended_array([1, 2, 3], 4)
        [1, 2, 3, 4]
    """
    return array.append(value_to_append)

def create_birtdate_from_string(date: str) -> datetime:
    """
    Creates a datetime object from a string in the format "dd/mm/yyyy".

    Parameters:
        date (str): The date string to convert to a datetime object.

    Returns:
        :result: datetime, The datetime object created from the string.

    Example:
        >>> create_birtdate_from_string("01/01/2000")
        datetime.datetime(2000, 1, 1, 0, 0)
    """
    date = date.split("-")
    print(date)
    return datetime.date(int(date[0]), int(date[1]), int(date[2])).isoformat()
