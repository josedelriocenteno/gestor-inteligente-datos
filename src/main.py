from data.usuarios import GestorUsuarios
from data.productos import Producto
from services.estadisticas import EstadisticasUsuarios, EstadisticasProductos
from utils.validaciones import Validaciones


def mostrar_menu_principal():
    print("\n" + "=" * 60)
    print("GESTOR DE DATOS")
    print("=" * 60)
    print("1. Añadir usuario")
    print("2. Mostrar usuarios")
    print("3. Buscar por ciudad")
    print("4. Buscar por ID")
    print("5. Añadir producto")
    print("6. Modificar precio")
    print("7. Eliminar producto")
    print("8. Mostrar productos")
    print("9. Estadísticas completas")
    print("0. Salir")
    print("=" * 60)


def main():
    gestor_usuarios = GestorUsuarios()
    catalogo_productos = Producto("Catálogo General", 0.0)

    print("Iniciando Gestor de Datos...")

    while True:
        mostrar_menu_principal()
        op = input("Elige opción (0-9): ").strip()

        if op == "1":
            gestor_usuarios.registrar_usuario_interactivo()

        elif op == "2":
            gestor_usuarios.mostrar_usuarios()

        elif op == "3":
            ciudad = input("Ciudad a buscar: ").strip()
            gestor_usuarios.buscar_por_ciudad(ciudad)

        elif op == "4":
            id_buscar = input("ID a buscar: ").strip()
            gestor_usuarios.buscar_por_id(Validaciones.validar_id(id_buscar))

        elif op == "5":
            nombre_prod = input("Nombre producto: ").strip()
            precio = Validaciones.validar_precio(input("Precio: "))
            if precio:
                catalogo_productos.añadir_producto(nombre_prod, precio)

        elif op == "6":
            nombre = input("Nombre producto: ").strip()
            precio_nuevo = Validaciones.validar_precio(input("Nuevo precio: "))
            if precio_nuevo:
                catalogo_productos.modificar_precio_producto(nombre, precio_nuevo)

        elif op == "7":
            nombre = input("Nombre a eliminar: ").strip()
            catalogo_productos.eliminar_producto(nombre)

        elif op == "8":
            catalogo_productos.mostrar_productos()

        elif op == "9":
            stats_usuarios = EstadisticasUsuarios(gestor_usuarios.obtener_usuarios())
            stats_usuarios.mostrar()
            stats_productos = EstadisticasProductos(catalogo_productos.dict_productos)
            stats_productos.mostrar()

        elif op == "0":
            print("\nGracias por usar el Gestor de Datos.")
            print("Proyecto listo para Moodle 30/01/2026")
            break

        else:
            print("Opción inválida. Elige 0-9.")

        input("\nPulsa Enter para continuar...")


if __name__ == "__main__":
    main()
