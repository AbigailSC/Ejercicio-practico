from my_module.basic_functions import read_json, write_json, custom_sorted_bussiness, custom_map
from my_module.data import show_menu, wish_continue, select_option_from_menu, array_sub_menu_options
from my_module.models import crear_producto, eliminar_producto, modificar_producto, listado_productos_caros, listado_productos_caros, listado_precio_promedio_tipo

p1 = {"id_producto": 1, "descripcion": "algo", "nacionalidad": 2, "tipo": 1, "precio": 123.0}
p2 = {"id_producto": 2, "descripcion": "algo2", "nacionalidad": 2, "tipo": 1, "precio": 323.0}
p3 = {"id_producto": 3, "descripcion": "algoasdasdasd", "nacionalidad": 2, "tipo": 2, "precio": 20.0}

def main() -> None:
    OPTIONS = read_json("OPTIONS.json", "r")
    TIPOPRODUCTO = read_json("TIPOPRODUCTO.json", "r")
    PRODUCTOS = [p1, p2, p3]
    option_continue = True
    while option_continue:
        show_menu(OPTIONS, "Gestión de productos")
        option_selected = select_option_from_menu(OPTIONS)
        match option_selected:
            case 1:
                new_product = crear_producto()
                PRODUCTOS.append(new_product)
            case 2:
                if len(PRODUCTOS) == 0:
                    print("[ERROR] Todavia no ha cargado ningun producto.")
                else:
                    PRODUCTOS = eliminar_producto(PRODUCTOS)
            case 3:
                if len(PRODUCTOS) == 0:
                    print("[ERROR] Todavia no ha cargado ningun producto.")
                else:
                    PRODUCTOS = modificar_producto(PRODUCTOS)
            case 4:
                if len(PRODUCTOS) == 0:
                    print("[ERROR] Todavia no ha cargado ningun producto.")
                else:
                    array_sub_menu_options(PRODUCTOS)
            case 5:
                if len(PRODUCTOS) == 0:
                    print("[ERROR] Todavia no ha cargado ningun producto.")
                else:
                    products_sorted = custom_sorted_bussiness(PRODUCTOS, lambda a: a["precio"])
                    print("[INFO] Productos ordenados por precio:")
                    custom_map(products_sorted, lambda a: print(f"[ID]: {a["id_producto"]} - [PRECIO]: {a["precio"]}"))
            case 6:
                if len(PRODUCTOS) == 0:
                    print("[ERROR] Todavia no ha cargado ningun producto.")
                else:
                    products_sorted = custom_sorted_bussiness(PRODUCTOS, lambda a: a["descripcion"])
                    print("[INFO] Productos ordenados por descripción:")
                    custom_map(products_sorted, lambda a: print(f"[ID]: {a["id_producto"]} - [DESCRIPCIÓN]: {a["descripcion"]}"))
            case 7:
                if len(PRODUCTOS) == 0:
                    print("[ERROR] Todavia no ha cargado ningun producto.")
                else:
                    products_sorted = custom_sorted_bussiness(PRODUCTOS, lambda a: a["precio"])
                    print("[INFO] Productos ordenados por precio:")
                    listado_productos_caros(products_sorted)
            case 8:
                if len(PRODUCTOS) == 0:
                    print("[ERROR] Todavia no ha cargado ningun producto.")
                else:
                    listado_precio_promedio_tipo(PRODUCTOS)
            case 9:
                pass
            case 10:
                pass
            case 11:
                print("[EXIT] Gracias por utilizar el sistema de gestión de estacionamientos")
                break
            case _:
                print("[INFO] Opción inválida")
        option_continue = wish_continue("[INFO] Desea continuar? Presione 's' para continuar o cualquier tecla para salir: ")
        if not option_continue:
            print("[EXIT] Gracias por utilizar el sistema de gestión de estacionamientos")
            break
main()