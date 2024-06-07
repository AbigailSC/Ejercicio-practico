import os

def get_number_with_range(msg: str, msg_error: str, min_number: int, max_number: int, retries: int | None = None) -> int | None:
    """
    Solicita al usuario ingresar un número dentro de un rango especificado y realiza las validaciones correspondientes.

    Parameters:
        msg (str): El mensaje para solicitar al usuario que ingrese el número.
        msg_error (str): El mensaje de error a mostrar si el número ingresado está fuera del rango o no es válido.
        min_number (int): El valor mínimo permitido para el número.
        max_number (int): El valor máximo permitido para el número.
        retries (int | None, opcional): El número máximo de intentos permitidos. Por defecto es None, lo que significa que no hay límite de intentos.

    Returns:
        :result: int | None, El número ingresado por el usuario si es válido y está dentro del rango especificado, None si no se ingresó un número válido o se superó el número de intentos.

    Examples:
        >>> get_number_with_range("Ingrese un número entre 1 y 10: ", "El número ingresado debe estar entre 1 y 10.", 1, 10)
    """
    while retries is None or retries > 0 or retries == -1:
        number_selected = input(msg)
        if number_selected.isdigit():
            number_selected = int(number_selected)
            if number_selected >= min_number and number_selected <= max_number:
                return number_selected
        else:
            print("[ERROR] Debe ingresar un número entero válido.")
        match retries:
            case None:
                break
            case -1:
                print(msg_error)
                print(f"[INFO] Intentos restantes: {retries}")
            case _:
                print(msg_error)
                print(f"[INFO] Intentos restantes: {retries}")
                retries -= 1
    return None

def get_string(msg: str, msg_error: str) -> str:
    """
    Calculate the length of a word.

    Parameters:
        :param msg: Value of the input message
        :param msg_error: Value of the error message

    Return:
        :result: str The length of the word

    Examples of use:
        >>> get_string()
        "Hello"
    """
    value = input(msg)
    while type(value) != str or len(value) == 0:
        print(msg_error)
        value = input(msg)
    return value

def get_float_number(msg: str, msg_error: str, retries: int | None = None) -> float | None:
    """
    Calculates the sum of 2 numerical parameters and returns the result.

    Parameters:
        :param msg: Value of the input message
        :param msg_error: Value of the error message
        :param retries: Value of the retries

    Return:
        :result: float, None The value of input

    Examples of use:
        >>> get_float_number("Enter a number", "Error. Enter a number again", 3)
        4.5
    """
    retry_count = retries

    while retry_count >= 0:
        data_number = float(input(msg))
        if data_number > 0:
            os.system('cls')
            return data_number
        print(msg_error)
        print(f"[INFO] Intentos restantes: {retry_count}")
        retry_count -= 1

def format_float_number(number_to_format: float, decimals_to_show: int | None = 2) -> float | None:
    """
    Formats a number with a specified number of decimals.

    Parameters:
        :param number_to_format: The number to be formatted.
        :param decimals_to_show: Number of decimal places to show. Default is 2.

    Return:
        :result: float, None The formatted number, or None if the input number is not positive.

    Examples of use:
        >>> format_number(31.400000000000002)
        31.4
        >>> format_number(31.400000000000002, 3)
        31.400
    """
    if number_to_format < 1:
        return None
    if type(number_to_format) == int:
        return number_to_format
    number_formatted = f"{number_to_format:.{decimals_to_show}f}"
    return float(number_formatted)

def array_sum_elements(array: list) -> int:
    """
    Calculates the sum of all elements in a given array.

    Parameters:
        array (list): The array containing elements to sum.

    Returns:
        :result: int, The sum of all elements in the array.

    Examples:
        >>> array_sum_elements([1, 2, 3, 4, 5])
        15
        >>> array_sum_elements([-1, -2, -3, -4, -5])
        -15
    """
    sum_elements = 0
    for index in range(len(array)):
        sum_elements += array[index]
    return sum_elements

def array_get_average(array: list) -> float:
    """
    Calculates the average value of elements in a given array.

    Parameters:
        array (list): The array containing elements.

    Returns:
        :result: float, The average value of elements in the array.

    Examples:
        >>> array_get_average([1, 2, 3, 4, 5])
        3.0
        >>> array_get_average([-1, -2, -3, -4, -5])
        -3.0
    """
    sum_elements = array_sum_elements(array)
    average = sum_elements / len(array)
    return average

def convert_string(string: str, convert_to: str) -> str:
    """
    Converts a string to lowercase or uppercase based on the specified option.

    Parameters:
        string (str): The string to be converted.
        convert_to (str): The conversion option. Use "lower" to convert to lowercase, "upper" to convert to uppercase.

    Returns:
        :result: str, The converted string.

    Examples:
        >>> convert_to_lowercase_or_uppercase("Hello World", "lower")
        'hello world'
        >>> convert_to_lowercase_or_uppercase("Hello World", "upper")
        'HELLO WORLD'
    """
    match convert_to:
        case "lower":
            return string.lower()
        case "upper":
            return string.upper()
        case "capitalize":
            return string.capitalize()
        case "title":
            return string.title()
        case "swap":
            return string.swapcase()
        case _:
            return string

def array_get_total_of_array(array: list) -> int:
    """
    Calculates the total sum of all elements in a given array.

    Parameters:
        array (list): The array to calculate the total sum of.

    Returns:
        :result: int, The total sum of all elements in the array.

    Example:
        >>> array_get_total_of_array([1, 2, 3, 4, 5])
        15
        >>> array_get_total_of_array([-1, -2, -3, -4, -5])
        -15
    """
    total = 0
    for index in range(0, len(array)):
        total += array[index]
    return total

def array_get_negative_numbers(array: list) -> list:
    """
    Retrieves all negative numbers from a given array.

    Parameters:
        array (list): The array to search for negative numbers.

    Returns:
        :result: list, A list containing all negative numbers found in the array.

    Example:
        >>> array_get_negative_numbers([-1, 2, -3, 4, -5])
        [-1, -3, -5]
        >>> array_get_negative_numbers([1, 2, 3, 4, 5])
        []
    """
    negative_numbers = []
    for index in range(0, len(array)):
        if array[index] < 0:
            negative_numbers.append(array[index])
    return negative_numbers

def array_get_count_negative_or_positive_numbers(array: list, condition: str) -> int:
    """
    Counts the number of negative or positive numbers in a given array based on the specified condition.

    Parameters:
        array (list): The array to count numbers in.
        condition (str): The condition to check. Use "negative" to count negative numbers, "positive" to count positive numbers.

    Returns:
        :result: int, The count of numbers that meet the specified condition.

    Example:
        >>> array_get_count_negative_or_positive_numbers([-1, 2, -3, 4, -5], "negative")
        3
        >>> array_get_count_negative_or_positive_numbers([-1, 2, -3, 4, -5], "positive")
        2
    """
    count_condition_numbers = 0
    for index in range(0, len(array)):
        if condition == "negative":
            if array[index] < 0:
                count_condition_numbers += 1
        else:
            if array[index] > 0:
                count_condition_numbers += 1
    return count_condition_numbers

def array_reverse_array (array_to_reverse: list) -> list:
    """
    Reverses the order of elements in a given array.

    Parameters:
        array_to_reverse (list): The array to reverse.

    Returns:
        :result: list, The reversed array.

    Example:
        >>> array_reverse_array([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
    """
    new_array = []
    for index in range(len(array_to_reverse) -1, -1, -1):
        new_array.append(array_to_reverse[index])
    return new_array

def bubble_sort(array:list) -> list:
    """
    Sorts an array using the bubble sort algorithm.

    Parameters:
        array (list): The array to sort.

    Returns:
        :result: list, The sorted array.

    Example:
        >>> bubble_sort([3, 2, 1])
        [1, 2, 3]
    """
    for index in range(len(array) - 1):
        for sub_index in range(index + 1, len(array)):
            if array[index] < array[sub_index]:
                pivot = array[index]
                array[index] = array[sub_index]
                array[sub_index] = pivot
    return array

def selection_sort(array: list) -> list:
    """
    Sorts an array using the selection sort algorithm in place.

    Parameters:
        array (list): The array to sort.

    Returns:
        :result: list, The sorted array.

    Example:
        >>> array = [3, 2, 1]
        >>> selection_sort(array)
        >>> array
        [1, 2, 3]
    """
    for index in range(len(array) - 1):
        index_min = index
        for sub_index in range(index + 1, len(array)):
            if array[index_min] > array[sub_index]:
                index_min = sub_index
        pivot = array[index]
        array[index] = array[index_min]
        array[index_min] = pivot
    return array

def quick_sort(array:list):
    """
    Sorts an array using the quick sort algorithm.

    Parameters:
        array (list): The array to sort.

    Returns:
        :result: list, The sorted array.

    Example:
        >>> quick_sort([3, 2, 1])
        [1, 2, 3]
    """
    if len(array) <= 1:
        return array
    pivot = array.pop()
    min_elements = list()
    max_elements = list()
    for element in array:
        if element > pivot:
            max_elements.append(element)
        else:
            min_elements.append(element)
    return quick_sort(min_elements) + [pivot] + quick_sort(max_elements)
