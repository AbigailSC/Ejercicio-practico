from datetime import datetime
import re

def validate_number_is_positive(number: int | float, msg: str, msg_error: str) -> int | float:
    """
    Validates that the number entered is positive.

    Parameters:
        :param number: Value of the number
        :param msg: Message to display when prompting the user to input the number
        :param msg_error: Message with the error

    Return:
        :result: int, float The number entered if it is positive or None if it is less than or equal to 0

    Examples of use:
        >>> validate_number_is_positive(5)
        5
        >>> validate_number_is_positive(-3.5)
        "[ERROR] The radius of the circle cannot be less than or equal to 0."
    """
    if type(number) == int:
        return_type = "int"
    else:
        return_type = "float"

    try:
        while number <= 0:
            print(msg_error)
            number = input("Ingrese un número positivo:\n")
            if return_type == "int":
                number = int(number)
            else:
                number = float(number)
        return number
    except ValueError:
        print(msg_error)
        return None

def validate_number_between_range(from_range: int, up_range: int, index: int) -> int | None:
    """
    Validates that the number entered is within the specified range.

    Parameters:
        :param from_range: Value of the minimum range
        :param up_range: Value of the maximum range
        :param index: Value of the index

    Return:
        :result: int, None The number entered if it is within the range, or None if it is not

    Examples of use:
        >>> validate_number_between_range(1, 10, 3)
        5
        >>> validate_number_between_range(1, 10, 30)
        "[ERROR] The number entered must be between 1 and 10"
    """
    try:
        number_to_array = int(input(f"Ingrese el {index + 1}° número:\n"))
        number_validated = number_to_array
        while number_validated < from_range or number_validated > up_range:
                print(f"[ERROR] El número ingresado debe estar entre {from_range} y {up_range}")
                number_validated = int(input(f"Ingrese el {index + 1}° número nuevamente:\n"))
        return number_validated
    except ValueError:
        print("[ERROR] El valor ingresado no es un número.")
        return None

def validate_pair_number(number: int) -> bool:
    """
    Validates if a number is even or odd.

    Parameters:
        :param number: The number to be validated.

    Return:
        :result: bool, True if the number is even, False if it is odd.

    Examples of use:
        >>> get_pair_number(5)
        False
        >>> get_pair_number(8)
        True
    """
    if number % 2 == 0:
        return True
    else:
        return False

def validate_number_positive(number: int) -> bool:
    """
    Validates if a given number is positive.

    Parameters:
        :param number: The number to validate.

    Returns:
        :result: bool, True if the number is positive, False otherwise.

    Examples of use:
        >>> validate_number_positive(5)
        True
        >>> validate_number_positive(-3)
        False
    """
    if number > 0:
        return True
    else:
        return False

def validate_number_is_integer(number_string:str)-> int:
    """
    Validates if a given string represents an integer.

    Parameters:
        number_string (str): The string to validate.

    Returns:
        :result: bool, True if the string represents an integer, False otherwise.

    Examples:
        >>> validate_number_is_integer("123")
        True
        >>> validate_number_is_integer("abc")
        False
    """
    for indice in range(len(number_string)):
        if number_string[indice] < "0" or number_string[indice] > "9":
            return False
    return True

def validate_array_is_empty(array: list, msg_error: str) -> bool:
    """
    Validates if a given array is empty.

    Parameters:
        array (list): The array to validate.
        msg_error (str): The error message to print if the array is empty.

    Returns:
        :result: bool, True if the array is empty, False otherwise.

    Examples:
        >>> validate_array_is_empty([], "The array is empty.")
        The array is empty.
        True
        >>> validate_array_is_empty([1, 2, 3], "The array is empty.")
        False
    """
    if len(array) == 0:
        print(msg_error)
        return True
    return False

def validate_input_length(input_value: str, min_length: int, max_length: int, input_msg: str, error_msg: str) -> str:
    """
    Validate the length of an input value.

    Parameters:
        input_value (str): The input value to be validated.
        min_length (int): The minimum length allowed.
        max_length (int): The maximum length allowed.
        input_msg (str): The message to be displayed when prompting the user to input the value.
        error_msg (str): The error message to be displayed if the input value length is invalid.

    Returns:
        :result: str, The validated input value.

    Example:
        >>> validate_input_length("username", 5, 10, "El nombre de usuario debe tener entre 5 y 10 caracteres.")
        'username'
    """
    try:
        input_value = input_value.strip()
        while len(input_value) < min_length or len(input_value) > max_length:
            print(error_msg)
            input_value = input(input_msg)
        return input_value
    except ValueError:
        print(error_msg)
        return None

def validate_word_is_empty(word: str, msg_error: str, msg_input: str) -> str:
    """
    Validates that a word is not empty.

    Parameters:
        word (str): The word to validate.
        msg_error (str): The error message to display if the word is empty.
        msg_input (str): The message to display when prompting the user to input the word.

    Returns:
        :result: str, The validated non-empty word.

    Example:
        >>> validate_word_is_empty("hello", "La palabra no puede estar vacía", "Ingrese una palabra: ")
        'hello'
    """
    try:
        wordValidated = word.strip()
        while wordValidated == None or len(wordValidated) == 0:
            print(msg_error)
            wordValidated = input(msg_input)
        return wordValidated
    except ValueError:
        print(msg_error)
        return None

def validate_word_contains_chars(word_main: str, word_to_search: str) -> bool:
    """
    Checks if a word contains another word as a substring.

    Parameters:
        word_main (str): The main word to search within.
        word_to_search (str): The word to search for within the main word.

    Returns:
        :result: bool, True if the word_to_search is found within word_main, False otherwise.

    Example:
        >>> word_contains_chars("hello", "ell")
        True
        >>> word_contains_chars("world", "hello")
        False
    """
    return word_to_search in word_main

def validate_word_is_in_array(array: list, word_to_search: str) -> list:
    """
    Searches for a word in a given array.

    Parameters:
        array (list): The array to search in.
        word_to_search (str): The word to search for.

    Returns:
        :result: list, The array with the word added if it is not found.

    Example:
        >>> validate_word_is_in_array(["apple", "banana", "orange"], "app")
        ['apple']
    """
    new_array = list()
    for index in range(0, len(array)):
        if validate_word_contains_chars(array[index].name, word_to_search):
            new_array.append(array[index])
    return new_array

def validate_word_exists_in_array(array: list, word_to_search: str) -> bool:
    """
    Searches for a word in a given array.

    Parameters:
        array (list): The array to search in.
        word_to_search (str): The word to search for.

    Returns:
        :result: bool, True if the word is found in the array, False otherwise.

    Example:
        >>> validate_word_exists_in_array(["apple", "banana", "orange"], "banana")
        True
        >>> validate_word_exists_in_array(["apple", "banana", "orange"], "grape")
        False
    """
    for index in range(0, len(array)):
        if array[index] == word_to_search:
            return True
    return False

def validate_word_is_alpha(word: str, msg: str, msg_error: str) -> str:
    """
    Validates if a given word contains only alphabetic characters.

    Parameters:
        word (str): The word to validate.
        msg (str): The message to display when prompting the user to input the word.
        msg_error (str): The error message to display if the word contains non-alphabetic characters.

    Returns:
        :result: str, The validated word containing only alphabetic characters.

    Examples:
        >>> validate_word_is_alpha("hello", "Enter a word: ", "The word must contain only alphabetic characters.")
        'hello'
        >>> validate_word_is_alpha("123", "Enter a word: ", "The word must contain only alphabetic characters.")
        Enter a word: 123
    """
    while not word.isalpha(): # Loopear caracter por caracter y verificar si es alfabético o distinto a "1", "2", etc.
        print(msg_error)
        word = input(msg)
    return word

def validate_is_number(input_value: str) -> bool:
    """
    Validates if a given string represents a number.

    Parameters:
        input_value (str): The string to validate.

    Returns:
        :result: bool, True if the string represents a number, False otherwise.

    Examples:
        >>> validate_is_number("123")
        True
        >>> validate_is_number("abc")
        False
    """
    return input_value.isdigit()

def validate_is_float(input_value: str) -> bool:
    """
    Validates if a given string represents a float.

    Parameters:
        input_value (str): The string to validate.

    Returns:
        :result: bool, True if the string represents a float, False otherwise.

    Examples:
        >>> validate_is_float("123.5")
        True
        >>> validate_is_float("abc")
        False
    """
    try:
        float(input_value)
        return True
    except ValueError:
        return False

def validate_is_number_with_msg(input_value: str, msg: str, msg_error: str) -> int:
    """
    Validates if a given string represents a number.

    Parameters:
        input_value (str): The string to validate.
        msg (str): The message to display when prompting the user to input the number.
        msg_error (str): The error message to display if the input value is not a number.

    Returns:
        :result: int, The validated number.

    Examples:
        >>> validate_is_number_with_msg("123", "Enter a number: ", "The value entered is not a number.")
        123
        >>> validate_is_number_with_msg("abc", "Enter a number: ", "The value entered is not a number.")
        Enter a number: abc
    """
    while not validate_is_number(input_value):
        print(msg_error)
        input_value = input(msg)
    input_value = int(input_value)
    return input_value

def validate_is_float_with_msg(input_value: str, msg: str, msg_error: str) -> float:
    """
    Validates if a given string represents a float.

    Parameters:
        input_value (str): The string to validate.
        msg (str): The message to display when prompting the user to input the float.
        msg_error (str): The error message to display if the input value is not a float.

    Returns:
        :result: float, The validated float.

    Examples:
        >>> validate_is_float_with_msg("123.5", "Enter a float: ", "The value entered is not a float.")
        123.5
        >>> validate_is_float_with_msg("abc", "Enter a float: ", "The value entered is not a float.")
        Enter a float: abc
    """
    while not validate_is_float(input_value):
        print(msg_error)
        input_value = input(msg)
    input_value = float(input_value)
    return input_value

def validate_document(document_to_validate: str) -> int:
    """
    Valida que el documento ingresado sea un número entero de 8 dígitos.

    Parameters:
        document_to_validate (str): El documento a validar.

    Returns:
        :result: int, El documento validado.

    Example:
        >>> validate_document("12345678")
        12345678
    """
    try:
        document_to_validate = validate_is_number_with_msg(document_to_validate, "Ingrese el número de documento:\n", "[ERROR] El documento debe ser un número entero.")
        while document_to_validate < 10000000 or document_to_validate > 99999999:
            print("[ERROR] El documento debe tener 8 dígitos.")
            document_to_validate = int(input("Ingrese el documento nuevamente:\n"))
        return document_to_validate
    except ValueError:
        print("[ERROR] El documento debe ser un número entero.")
        return None

def validate_age(age_to_validate: str, min_value: int, max_value: int) -> int:
    """
    Valida que la edad ingresada sea un número entero entre 18 y 65 años.

    Parameters:
        age_to_validate (str): La edad a validar.
        min_value (int): El valor mínimo de la edad.
        max_value (int): El valor máximo de la edad.

    Returns:
        :result: int, La edad validada.
    
    Example:
        >>> validate_age("30", 18, 65)
        30
    """
    try:
        age_to_validate = validate_is_number_with_msg(age_to_validate, "Ingrese la edad:\n", "[ERROR] La edad debe ser un número entero.")
        while age_to_validate < min_value or age_to_validate > max_value:
            print(f"[ERROR] La edad debe estar entre {min_value} y {max_value} años.")
            age_to_validate = int(input("Ingrese la edad nuevamente:\n"))
        return age_to_validate
    except ValueError:
        print("[ERROR] La edad debe ser un número entero.")
        return None

def validate_date(date: str, msg_input: str, msg_error: str) -> str:
    """
    Valida que la fecha ingresada sea válida.

    Parameters:
        date (str): La fecha a validar.
        msg_input (str): El mensaje a mostrar al solicitar al usuario que ingrese la fecha.
        msg_error (str): El mensaje de error a mostrar si la fecha no es válida.

    Returns:
        :result: str, La fecha validada.

    Example:
        >>> validate_date("2021-12-31", "Ingrese la fecha de nacimiento (AAAA-MM-DD):\n", "[ERROR] La fecha ingresada no es válida.")
        2021-12-31
    """
    list_date = date.split("-")
    day = int(list_date[2])
    month = int(list_date[1])
    year = int(list_date[0])
    while day < 1 or day > 31 or month < 1 or month > 12 or year < 1900 or year > datetime.now().year:
        print(msg_error)
        date = input(msg_input)
        list_date = date.split("-")
        day = int(list_date[2])
        month = int(list_date[1])
        year = int(list_date[0])
    return date

def validate_email(email: str) -> str:
    """
    Valida que el email ingresado contenga un "@" y un ".".

    Parameters:
        email (str): El email a validar.

    Returns:
        :result: str, El email validado.

    Example:
        >>> validate_email("pepe@gmail.com")
        pepe@gmail.com
    """
    pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    while not re.match(pattern_email, email):
        print("[ERROR] El email no es válido.")
        email = input("Ingrese el email nuevamente:\n")
    return email

def validate_password(password: str) -> str:
    """
    Validates that the password entered contains at least 8 characters, a lowercase letter, an uppercase letter, a number, and a special character.

    Parameters:
        password (str): The password to validate.

    Returns:
        :result: str, The validated password.

    Example:
        >>> validate_password("P@ssw0rd")
        P@ssw0rd
    """
    pattern_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    while not re.match(pattern_password, password):
        print("[ERROR] La contraseña debe tener al menos 8 caracteres, una letra minúscula, una letra mayúscula, un número y un carácter especial.")
        password = input("Ingrese la contraseña nuevamente:\n")
    return password

def validate_id_with_Regex(id: str) -> bool:
    example_id = "4568-SR"
    pattern = r"^\d{4}-[A-Z]{2}$"
    if re.match(pattern, id):
        return True
    else:
        print(f"El ID {id} no es válido. Ejemplo de ID válido: {example_id}")
        return False
    
def validate_cuit_regex(cuit: str) -> bool:
    example_cuit = "20-12345678-5"
    pattern = r"^\d{2}-\d{8}-\d$"
    if re.match(pattern, cuit):
        return True
    else:
        print(f"El CUIT {cuit} no es válido. Ejemplo de CUIT válido: {example_cuit}")
        return False
    
def validate_patente_regex(patente: str) -> bool:
    example_patente = "ABC123"
    pattern = r"^[A-Z]{3}\d{3}$"
    if re.match(pattern, patente):
        return True
    else:
        print(f"La patente {patente} no es válida. Ejemplo de patente válida: {example_patente}")
        return False