import csv
import json
import datetime

def calculate_power_recursion(number: int | float, power: int) -> int | float | None:
    """
    Calculates the power of a number using recursion.

    Parameters:
    :param number: The base number.
    :param power: The exponent.

    Return:
    :result: int, float, None The result of raising the base number to the power of the exponent, or None if the exponent is negative.

    Examples of use:
    >>> calculate_power_recursion(2, 3)
    8
    >>> calculate_power_recursion(5, 2)
    25
    """
    match power:
        case 0:
            return 1
        case 1:
            return number
        case _ if power < 0:
            return None
        case _:
            power -= 1
            return number * calculate_power_recursion(number, power)
        
def es_primo(number) -> bool:
    """
    Checks if a given number is a prime number.

    Parameters:
        number (int): The number to check for primality.

    Returns:
        :result: bool, True if the number is prime, False otherwise.

    Examples:
        >>> es_primo(7)
        True
        >>> es_primo(12)
        False
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    else:
        raiz_cuadrada = int(number ** 0.5)
        for divisor in range(2, raiz_cuadrada + 1, 2):
            if number % divisor == 0:
                return False
        return True

def array_search_binary(array: list, elem_to_search: str | int | float) -> str | None:
    """
    Searches for an element in a sorted array using the binary search algorithm.

    Parameters:
        array (list): The sorted array to search in.
        elem_to_search (str): The element to search for.

    Returns:
        :result: int | None, The index of the element if found, otherwise None.

    Example:
        >>> array_search_binary(['apple', 'banana', 'orange'], 'banana')
        1
    """
    index_min = 0
    index_max = len(array) - 1
    while index_min <= index_max:
        index_midle = (index_min + index_max) // 2 # Redondea al entero minimo
        if array[index_midle] == elem_to_search:
            return index_midle
        else:
            if array[index_midle] < elem_to_search:
                index_min = index_midle + 1
            else:
                index_max = index_midle - 1
    return None

def custom_map(list_to_map: list, fn) -> list:
    """
    Applies a function to each element of a list.

    Parameters:
    :param list_to_map: The list to apply the function to.
    :param fn: The function to apply to the list.

    Return:
    :result: list, The list with the function applied to each element.

    Examples of use:
    >>> custom_map([1, 2, 3], lambda x: x ** 2)
    [1, 4, 9]
    """
    copy_list = list_to_map.copy()
    for element in range(len(copy_list)):
        copy_list[element] = fn(copy_list[element])
    return copy_list

def custom_filter(list_to_filter: list, fn) -> list:
    """
    Filters a list based on a function.

    Parameters:
    :param list_to_filter: The list to filter.
    :param fn: The function to filter the list.

    Return:
    :result: list, The filtered list.

    Examples of use:
    >>> custom_filter([1, 2, 3, 4], lambda x: x % 2 == 0)
    [2, 4]
    """
    copy_list = list()
    for element in range(len(list_to_filter)):
        if fn(list_to_filter[element]):
            copy_list.append(list_to_filter[element])
    return copy_list

def custom_reduce(list_to_reduce: list, fn):
    """
    Reduces a list to a single value based on a function.

    Parameters:
    :param list_to_reduce: The list to reduce.

    Return:
    :result: int | float, The reduced value.

    Examples of use:
    >>> custom_reduce([1, 2, 3, 4], lambda x, y: x + y)
    """
    copy_list = list_to_reduce.copy()
    result = copy_list[0]
    for element in range(1, len(copy_list)):
        result = fn(result, copy_list[element])
    return result

def custom_sorted(list_to_sort: list, fn) -> list:
    """
    Sorts a list based on a function.

    Parameters:
    :param list_to_sort: The list to sort.
    :param fn: The function to sort the list.

    Return:
    :result: list, The sorted list.

    Examples of use:
    >>> custom_sorted([3, 2, 1], lambda x: x)
    [1, 2, 3]
    """
    copy_list = list_to_sort.copy()
    for i in range(len(copy_list)):
        for j in range(i + 1, len(copy_list)):
            if fn(copy_list[i]) > fn(copy_list[j]):
                pivot = copy_list[i]
                copy_list[i] = copy_list[j]
                copy_list[j] = pivot
    return copy_list

def read_txt(path: str, mode: str) -> str:
    try:
        with open(path, mode, encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('No se encontro el archivo')

def write_txt(path: str, mode: str, data: str):
    try:
        with open(path, mode, encoding='utf-8') as file:
            file.write(data + '\n')
    except FileNotFoundError:
        print('No se encontro el archivo')

def append_to_txt(path: str, data: str):
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
    except FileNotFoundError:
        print('No se encontro el archivo')

def find_value_in_txt(path: str, mode: str, value: str) -> bool:
    try:
        with open(path, mode, encoding='utf-8') as file:
            for line in file:
                if value in line:
                    return True
                return False
    except FileNotFoundError:
        print('No se encontro el archivo')

def read_csv_with_return(path: str, mode: str):
    try:
        with open(path, mode, newline='', encoding='utf-8') as file:
            read_csv = csv.DictReader(file, delimiter=',')
            data = []
            for row in read_csv:
                data.append(row)
            return data
    except FileNotFoundError:
        print('No se encontro el archivo')

def write_csv(path: str, mode: str, data: list):
    try:
        fieldnames = ['CODIGO', 'DETALLE', 'USD COMPRA', 'USD VENTA', 'PESO']
        with open(path, mode, newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for row in data:
                print(row)
                writer.writerow(row)
    except FileNotFoundError:
        print('No se encontro el archivo')

def append_to_csv(path: str, new_data: object):
    try:
        fieldnames = ['CODIGO', 'DETALLE', 'USD COMPRA', 'USD VENTA', 'PESO']
        with open(path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(new_data)
    except FileNotFoundError:
        print('No se encontro el archivo')

def read_json(path: str, mode: str):
    try:
        with open(path, mode, encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('No se encontro el archivo')

def write_json(path: str, mode: str, data: list):
    try:
        with open(path, mode, encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print('No se encontro el archivo')

def append_to_json(path: str, new_data: dict):
    try:
        data = read_json(path, 'r')
        data.append(new_data)
        write_json(path, 'w', data)
    except FileNotFoundError:
        print('No se encontro el archivo')

def custom_find(array: list, value: str | int | float) -> bool:
    for element in array:
        if element == value:
            return True
    return False

def custom_reduce_bussiness(list_to_reduce: list, fn):
    """
    Reduces a list to a single value based on a function.

    Parameters:
    :param list_to_reduce: The list to reduce.

    Return:
    :result: int | float, The reduced value.

    Examples of use:
    >>> custom_reduce([1, 2, 3, 4], lambda x, y: x + y)
    """
    copy_list = list_to_reduce.copy()
    result = copy_list[0]["recaudacion"]
    for element in range(1, len(copy_list)):
        result = fn(result, copy_list[element]["recaudacion"])
    return result

def custom_filter_bussiness(list_to_filter: list, fn) -> list:
    """
    Filters a list based on a function.

    Parameters:
    :param list_to_filter: The list to filter.
    :param fn: The function to filter the list.

    Return:
    :result: list, The filtered list.

    Examples of use:
    >>> custom_filter([1, 2, 3, 4], lambda x: x % 2 == 0)
    [2, 4]
    """
    list_to_return = list()
    copy_list = list_to_filter.copy()
    for element in range(len(copy_list)):
        if fn(copy_list[element]):
            list_to_return.append(copy_list[element])
    return list_to_return

def generate_id_db(path: str) -> int:
    list_db = read_json(path, "r")
    new_id = len(list_db) + 1
    return new_id

def custom_sorted_bussiness(list_to_sort: list, fn):
    """
    Sorts a list based on a function.

    Parameters:
    :param list_to_sort: The list to sort.
    :param fn: The function to sort the list.

    Return:
    :result: list, The sorted list.

    Examples of use:
    >>> custom_sorted([3, 2, 1], lambda x: x)
    [1, 2, 3]
    """
    copy_list = list_to_sort.copy()
    for i in range(len(copy_list)):
        for j in range(i + 1, len(copy_list)):
            if fn(copy_list[i]) < fn(copy_list[j]):
                pivot = copy_list[i]
                copy_list[i] = copy_list[j]
                copy_list[j] = pivot
    return copy_list