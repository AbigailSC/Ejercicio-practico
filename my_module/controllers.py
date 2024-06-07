from my_module.data import get_index_producto, bussiness_get_value_of_array, array_sub_menu_options, array_options_simple
from my_module.validations import validate_input_length, validate_number_is_positive, validate_is_float_with_msg, validate_is_number_with_msg
from my_module.utils import get_number_with_range

def get_descripcion() -> str:
    try:
        msg_detalle_input = "[INPUT] Ingrese la descripción del producto:\n"
        descripcion = input(msg_detalle_input)
        descripcion = validate_input_length(descripcion, 1, 50, msg_detalle_input, "[ERROR] La descripción debe tener entre 1 y 50 caracteres.")
        descripcion = descripcion.capitalize()
        return descripcion
    except ValueError:
        print("[ERROR] La descripción del producto solo debe contener solo letras.")

def get_opcion(msg_input: str, list_enum) -> int:
    try:
        opcion_selected = bussiness_get_value_of_array(list_enum, msg_input, "[ERROR] Opción invalida")
        return opcion_selected.value
    except ValueError:
        print("[ERROR] El importe debe ser un número.")

def get_precio(msg_input: str) -> int:
    precio = input(msg_input)
    precio = validate_is_float_with_msg(precio, msg_input, "[ERROR] El precio debe ser un número.")
    precio = validate_number_is_positive(precio, msg_input, "[ERROR] El precio debe ser un número positivo.")
    return precio

def listar_productos(list_productos: list, msg_input: str) -> int:
    array_sub_menu_options(list_productos)
    index_to_delete = get_number_with_range(msg_input, "[ERROR] Opción incorrecta, intentelo nuevamente.", 0, len(list_productos), 5)
    return index_to_delete - 1

def seleccionar_producto_modificar(list_prods: list) -> dict:
    index_to_update = listar_productos(list_prods, "[INPUT] Seleccione el producto que desea modificar: ")
    lista_opciones_modificar = ["Tipo", "Precio"]
    array_options_simple(lista_opciones_modificar)
    index_to_modificar = get_number_with_range("[INPUT] Seleccione el atributo a modificar: ", "[ERROR] Opción incorrecta, intentelo nuevamente.", 0, len(lista_opciones_modificar), 5)
    dict_to_return = {
        "producto_index": index_to_update,
        "tipo_modificacion": index_to_modificar
    }
    return dict_to_return

def get_limite_lista(list_productos: list, mgs_input: str) -> int:
    cantidad_productos = input(mgs_input)
    cantidad_productos = validate_is_number_with_msg(cantidad_productos, mgs_input, "[ERROR] La cantidad de valores a listar debe ser un número.")
    cantidad_productos = validate_number_is_positive(cantidad_productos, mgs_input, "[ERROR] La cantidad de valores a listar debe ser un número positivo.")
    while cantidad_productos > len(list_productos):
        print("[ERROR] El número de productos a mostrar no puede ser mayor a la cantidad de productos existentes.")
        cantidad_productos = input(mgs_input)
        cantidad_productos = validate_is_number_with_msg(cantidad_productos, mgs_input, "[ERROR] La cantidad de valores a listar debe ser un número.")
        cantidad_productos = validate_number_is_positive(cantidad_productos, mgs_input, "[ERROR] La cantidad de valores a listar debe ser un número positivo.")
    return cantidad_productos