import os
from my_module.basic_functions import es_primo
from my_module.validations import validate_array_is_empty
from my_module.utils import get_number_with_range, convert_string

def array_get_max_or_min_value(array: list) -> int:
    """
    Finds the maximum value in a given array.

    Parameters:
        array (list): The array to search for the maximum value.

    Returns:
        :result: int, The maximum value found in the array.

    Examples:
        >>> array_get_maximum_value([3, 7, 2, 9, 5])
        9
        >>> array_get_maximum_value([-5, -2, -10, -3])
        -2
    """
    maximum_value = array[0]
    for index in range(1, len(array)):
        if array[index] > maximum_value:
            maximum_value = array[index]
    return maximum_value

def array_get_minimum_value(array: list) -> int:
    """
    Finds the minimum value in a given array.

    Parameters:
        array (list): The array to search for the minimum value.

    Returns:
        :result: int, The minimum value found in the array.

    Examples:
        >>> array_get_minimum_value([3, 7, 2, 9, 5])
        2
        >>> array_get_minimum_value([-5, -2, -10, -3])
        -10
    """
    minimum_value = array[0]
    for index in range(1, len(array)):
        if array[index] < minimum_value:
            minimum_value = array[index]
    return minimum_value

def array_get_number_prim(array: list) -> int:
    """
    Counts the number of prime numbers in a given array.

    Parameters:
        array (list): The array to search for prime numbers.

    Returns:
        :result: int, The count of prime numbers found in the array.

    Examples:
        >>> array_get_number_prim([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        4
        >>> array_get_number_prim([11, 12, 13, 14, 15])
        3
    """
    count_numbers_primos = 0
    for index in range(len(array)):
        if es_primo(index):
            count_numbers_primos += 1
    return count_numbers_primos

def array_get_value_by_index(array: list, index: int) -> int | str | float | None:
    """
    Returns the number in a given array at the specified index.

    Parameters:
        array (list): The array to search for the number.
        index (int): The index of the number to retrieve.

    Returns:
        :result: int | str | float | None, The number at the specified index, or None if the index is out of range.

    Examples:
        >>> array_get_number_by_index([1, 2, 3, 4, 5], 2)
        3
        >>> array_get_number_by_index([1, 2, 3, 4, 5], 10)
        [ERROR] Index number is invalid
        None
    """
    number = None
    index_in_array = 0
    if validate_array_is_empty(array, "[ERROR] Array is empty"):
        return None
    if index > len(array) or index < 0:
        return print("[ERROR] Index number is invalid")
    for number in array:
        if index_in_array == index:
            return number
        else:
            index_in_array += 1
    return number

def show_menu (menu_options: list, title: str | None = None) -> None:
    """
    Displays a menu with the given options and returns the selected option.

    Parameters:
        menu_options (list): A list of strings representing the menu options.
        title (str | None): Optional. The title of the menu. Defaults to None.

    Returns:
        :result: str, The selected menu option.

    Example:
        >>> show_menu(["Option 1", "Option 2", "Option 3"], "Main Menu")
        Main Menu

        1) Option 1
        2) Option 2
        3) Option 3

        Ingrese la opción
    """
    os.system('cls')
    index_option = 1
    if title != None:
        print(f"{title}\n")
    for index in menu_options:
        print(f"{index_option}) {index}")
        index_option += 1

def wish_continue(msg) -> bool:
    """
    Asks the user if they wish to continue based on the provided message.

    Parameters:
        msg (str): The message to prompt the user for input.

    Returns:
        :result: bool, True if the user wishes to continue, False otherwise.

    Example:
        >>> wish_continue("Desea continuar? s/n\n")
        Desea continuar? s/n
        s
        True
        >>> wish_continue("Desea continuar? s/n\n")
        Desea continuar? s/n
        n
        False
    """
    option = input(msg)
    option = convert_string(option, "lower")
    if option == "s":
        return True
    else:
        return False

def select_option_from_menu(menu_options: list) -> int:
    option = get_number_with_range("\nIngrese la opción:\n", "[ERROR] Ingrese nuevamente la opción", 0, len(menu_options), 3)
    return option

def array_get_value_in_array(array: list, value: any) -> str | None:
    """
    Busca un valor dentro de un array y devuelve la primera coincidencia encontrada.

    Parameters:
        array (list): El array en el que buscar el valor.
        value (str | int | float): El valor a buscar en el array.

    Returns:
        :result: str | None, El valor encontrado en el array, o None si no se encontró.

    Example:
        >>> array_get_value_in_array(["apple", "banana", "orange"], "banana")
        'banana'
        >>> array_get_value_in_array([1, 2, 3, 4, 5], 6)
        None
    """
    for index in range(0, len(array)):
        if array[index] == value:
            return array[index]
    return None

def array_sub_menu_options(sub_menu: list) -> list:
    """
    Displays the options of a submenu along with their indices.

    Parameters:
        sub_menu (list): The list of submenu options.

    Returns:
        :result: str | None, The value found in the array, or None if not found.

    Example:
        >>> array_sub_menu_options(["Option 1", "Option 2", "Option 3"])
        1) Option 1
        2) Option 2
        3) Option 3
    """
    for index in range(0, len(sub_menu)):
        print(f"{index + 1}) {sub_menu[index]["id_producto"]} - {sub_menu[index]["descripcion"]}")

def array_sub_menu_options_objects(employee: list, employee_personal_data: list, attribute_to_show: str | None) -> list:
    """
    Displays the options of a submenu along with their indices.

    Parameters:
        sub_menu (list): The list of submenu options.
        attribute_to_show (str | None): The attribute to show. Defaults to None.

    Returns:
        :result: str | None, The value found in the array, or None if not found.

    Example:
        >>> array_sub_menu_options_objects(["Option 1", "Option 2", "Option 3"], "fullname")
        1) Option 1
        2) Option 2
        3) Option 3
    """
    aux_index = 0
    for employee_index, employee_data_index in zip(employee, employee_personal_data):
        match attribute_to_show:
            case "fullname":
                print(f"{aux_index + 1}) {employee_data_index.legajo} | {employee_index.get_fullname()}")
            case "document":
                print(f"{aux_index + 1}) {employee_index.document} | {employee_index.get_fullname()}")
            case _:
                print(f"{aux_index + 1}) {employee_index}")

def array_print_two_arrays(array1: list, array2: list) -> None:
    """
    Prints two arrays side by side.

    Parameters:
        array1 (list): The first array to print.
        array2 (list): The second array to print.

    Returns:
        :result: None

    Example:
        >>> array_print_two_arrays([1, 2, 3], ['a', 'b', 'c'])
        1 | a
        2 | b
        3 | c
    """
    for first_element, second_element in zip(array1, array2):
        print(f"{first_element} | {second_element}")

def get_index_of_array(list_values: list, msg: str, msg_error: str) -> int:
    """
    Displays the options of a submenu along with their indices.

    Parameters:
        list_values (list): The list of submenu options.
        msg (str): The message to display.
        msg_error (str): The error message to display.

    Returns:
        :result: int, The index selected by the user.

    Example:
        >>> get_index_of_array(["Option 1", "Option 2", "Option 3"], "Select an option:\n", "Invalid option")
        Select an option:
        1) Option 1
        2) Option 2
        3) Option 3
    
    """
    array_sub_menu_options(list_values)
    index_selected = get_number_with_range(msg, msg_error, 0, len(list_values), 5)
    return index_selected - 1

def map_logs(path_logs: str) -> None:
    try:
        with open(path_logs, "r") as file:
            logs = file.readlines()
            for index in range(len(logs) -1, 0, -1):
                print(logs[index])
    except Exception:
        print("[ERROR] No se pudo mapear los logs.")

def bussiness_array_sub_menu_options(lista) -> None:
    for index in range(0, len(lista)):
        print(f"{index + 1}) {lista[index].name}")

def bussiness_get_value_of_array(list_values, msg: str, msg_error: str) -> int:
    bussiness_array_sub_menu_options(list_values)
    index_selected = get_number_with_range(msg, msg_error, 0, len(list_values), 5)
    return list_values[index_selected - 1]

def get_index_producto(lista_productos: list, msg: str, msg_error: str) -> int:
    bussiness_array_sub_menu_options(lista_productos)
    index_selected = get_number_with_range(msg, msg_error, 0, len(lista_productos), 5)
    return index_selected

def array_options_simple(list: list) -> None:
    for index in range(0, len(list)):
        print(f"{index + 1}) {list[index]}")