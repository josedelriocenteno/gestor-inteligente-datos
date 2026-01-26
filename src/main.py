# main.py
from data.usuarios import anadir_usuario, mostrar_usuarios, buscar_por_ciudad, buscar_por_id
from data.productos import anadir_producto, mostrar_productos, modificar_producto, eliminar_producto
from services.estadisticas import mostrar_estadisticas
from utils.validaciones import Validaciones

def mostrar_menu():
    print("\n" + "="*50)
    print("🛒 GESTOR INTELIGENTE DE DATOS - STARTUP")
    print("="*50)
    print("1.  ➕ Añadir usuario")
    print("2.  📋 Mostrar usuarios")
    print("3.  🔍 Buscar usuarios por ciudad")
    print("4.  🆔 Buscar usuario por ID")
    print("5.  📦 Añadir producto")
    print("6.  💰 Modificar precio producto")
    print("7.  🗑️  Eliminar producto")
    print("8.  📊 Mostrar productos")
    print("9.  📈 ESTADÍSTICAS")
    print("0.  ❌ SALIR")
    print("="*50)

def main():
    print("🚀 Iniciando Gestor Inteligente de Datos...")
    
    while True:
        mostrar_menu()
        opcion = input("Elige opción (0-9): ").strip()
        
        try:
            if opcion == "1":
                anadir_usuario()
            elif opcion == "2":
                mostrar_usuarios()
            elif opcion == "3":
                ciudad = input("Ciudad a buscar: ").strip()
                buscar_por_ciudad(ciudad)
            elif opcion == "4":
                id_buscar = input("ID a buscar: ")
                buscar_por_id(id_buscar)
            elif opcion == "5":
                anadir_producto()
            elif opcion == "6":
                nombre = input("Nombre producto: ").strip()
                precio_nuevo = input("Nuevo precio: ")
                modificar_producto(nombre, precio_nuevo)
            elif opcion == "7":
                nombre = input("Nombre a eliminar: ").strip()
                eliminar_producto(nombre)
            elif opcion == "8":
                mostrar_productos()
            elif opcion == "9":
                mostrar_estadisticas()
            elif opcion == "0":
                print("👋 ¡Gracias por usar el Gestor!")
                break
            else:
                print("❌ Opción inválida (0-9)")
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Saliendo...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
