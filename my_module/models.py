from enum import Enum

from my_module.controllers import get_descripcion, get_opcion, get_opcion_tipo, get_precio, listar_productos, seleccionar_producto_modificar, get_limite_lista, get_lista_producto_tipo
from my_module.basic_functions import read_json, custom_find_with_return_value, custom_reduce, custom_filter
id_producto = 0

class Nacionalidad(Enum):
    EEUU = 1
    CHINA = 2
    OTRO = 3

class Tipo(Enum):
    IPHONE = 1
    MAC = 2
    IPAD = 3
    ACCESORIOS = 4

class Producto:
    id_producto = 0
    def __init__(self, descripcion: str, nacionalidad: int, tipo: int, precio: float):
        Producto.id_producto += 1
        self.id_producto = Producto.id_producto
        self.descripcion = descripcion
        self.nacionalidad = nacionalidad
        self.tipo = tipo
        self.precio = precio
    def __str__(self) -> str:
        return f"[ID]: {self.id} [DESCRIPCIÓN]: {self.descripcion} [NACIONALIDAD]: {self.nacionalidad} [TIPO]: {self.tipo} [PRECIO]: {self.precio}"
    def __len__(self) -> int:
        pass
    def create_id(self, acum) -> int:
        return acum + 1
    
class TipoProducto:
    def __init__(self, id_tipo: int, descripcion_tipo: str):
        self.id_tipo = id_tipo
        self.descripcion_tipo = descripcion_tipo

def crear_producto(lista_tipo_producto: list[TipoProducto]) -> dict:
    descripcion = get_descripcion()
    nacionalidad = get_opcion("Seleccione la nacionalidad del producto: ", list(Nacionalidad), None)
    tipo = get_opcion_tipo("Seleccione el tipo del producto: ", lista_tipo_producto, 0)
    precio = get_precio("Ingrese el precio del producto: ")
    new_product = Producto(descripcion, nacionalidad, tipo, precio)
    return new_product.__dict__

def eliminar_producto(lista_productos: list[Producto]) -> list[Producto]:
    index_to_delete = listar_productos(lista_productos, "[INPUT] Seleccione el producto que desea eliminar: ")
    producto_eliminado = lista_productos.pop(index_to_delete)
    print(f"[INFO] Se elimino el producto con id {producto_eliminado["id_producto"]}")
    return lista_productos

def modificar_producto(lista_productos: list[Producto], lista_tipo_producto: list[TipoProducto]) -> list[Producto]:
    dict_productos_a_modificar = seleccionar_producto_modificar(lista_productos)
    index_a_modificar = dict_productos_a_modificar["producto_index"]
    match dict_productos_a_modificar["tipo_modificacion"]:
        case 1:
            lista_productos[index_a_modificar]["tipo"] = get_opcion_tipo("Seleccione el nuevo tipo del producto: ", lista_tipo_producto, 0)
        case 2:
            lista_productos[index_a_modificar]["precio"] = get_precio("Ingrese el nuevo precio del producto: ")
        case _:
            print("[ERROR] Seleccione una opción valida")
    print(f"[INFO] Producto con id {lista_productos[index_a_modificar]["id_producto"]} actualizado con exito")
    return lista_productos

def listado_productos_caros(productos_ordenados: list[Producto]) -> None:
    cantidad_productos_listar = get_limite_lista(productos_ordenados, "[INPUT] Ingrese la cantidad de productos a listar: ")
    for index in range(cantidad_productos_listar):
        print(f"{index + 1}) {productos_ordenados[index]["id_producto"]} - {productos_ordenados[index]["descripcion"]} - {productos_ordenados[index]["precio"]}")

def listado_precio_promedio_tipo(lista_productos: list[Producto], lista_tipo_producto: list[TipoProducto]) -> None:
    productos_filtrados = get_lista_producto_tipo(lista_productos, lista_tipo_producto)
    total_precio_productos = custom_reduce(productos_filtrados, lambda a, b: a["precio"] + b["precio"])
    promedio_por_tipo = total_precio_productos / len(productos_filtrados)
    tipo_producto_name = custom_find_with_return_value(lista_tipo_producto,productos_filtrados[0]["tipo"])
    print(f"[INFO] El precio promedio de los productos de tipo {tipo_producto_name} es: {promedio_por_tipo}")

def listado_productos_descripcion_tipo(lista_productos: list[Producto], lista_tipo_producto: list[TipoProducto]) -> None:
    for index in range(0, len(lista_productos)):
        tipo_producto_name = custom_find_with_return_value(lista_tipo_producto,lista_productos[index]["tipo"])
        print(f"{index + 1}) [ID]: {lista_productos[index]["id_producto"]} - [DESCRIPCIÓN]: {lista_productos[index]["descripcion"]} - [NACIONALIDAD]: {lista_productos[index]["nacionalidad"]} - [TIPO_DESCRIPCIÓN]: {tipo_producto_name} - [PRECIO]: {lista_productos[index]["precio"]}")

def listado_productos_por_tipo(lista_productos: list[Producto], lista_tipo_producto: list[TipoProducto]) -> None:
    for tipo_producto in lista_tipo_producto:
        productos_filtrados_tipo = custom_filter(lista_productos, lambda a: a["tipo"] == tipo_producto["id_tipo"])
        print(f"[INFO] Listado de productos de tipo {tipo_producto["descripcion_tipo"]}:")
        if len(productos_filtrados_tipo) == 0:
            print("[INFO] No hay productos de este tipo")
        else:
            listado_productos_descripcion_tipo(productos_filtrados_tipo, lista_tipo_producto)
        print("\n")