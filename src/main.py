from app import *

def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("GESTOR INTELIGENTE DE DATOS")
    print("=" * 50)
    print("1. Añadir usuario")
    print("2. Mostrar usuarios")
    print("3. Buscar por ciudad")
    print("4. Buscar por ID")
    print("5. Añadir producto")
    print("6. Modificar precio")
    print("7. Eliminar producto")
    print("8. Mostrar productos")
    print("9. Estadisticas")
    print("0. Salir")
    print("=" * 50)

def main():
    print("Iniciando Gestor...")
    
    while True:
        mostrar_menu_principal()
        op = input("Elige opcion: ").strip()
        
        if op == "1":
            id_u = validar_id(input("ID: "))
            if id_u is None:
                continue         
            nom = validar_nombre(input("Nombre: "))
            if nom is None:
                continue             
            ed = validar_edad(input("Edad: "))
            if ed is None:
                continue             
            ciu = validar_ciudad(input("Ciudad: "))
            if ciu is None:
                continue             
            registrar_usuario(id_u, nom, ed, ciu)
                
        elif op == "2":
            mostrar_usuarios()
            
        elif op == "3":
            ciudad = input("Ciudad: ").strip()
            buscar_por_ciudad(ciudad)
            
        elif op == "4":
            id_buscar = input("ID: ").strip()
            id_val = validar_id(id_buscar)
            if id_val:
                buscar_por_id(id_val)
                
        elif op == "5":
            nombre_prod = input("Nombre producto: ").strip()
            precio_txt = input("Precio: ")
            precio = validar_precio(precio_txt)
            if precio:
                añadir_producto(nombre_prod, precio)
                
        elif op == "6":
            nombre = input("Nombre producto: ").strip()
            precio_txt = input("Nuevo precio: ")
            precio = validar_precio(precio_txt)
            if precio:
                modificar_precio_producto(nombre, precio)
                
        elif op == "7":
            nombre = input("Nombre eliminar: ").strip()
            eliminar_producto(nombre)
            
        elif op == "8":
            mostrar_productos()
            
        elif op == "9":
            mostrar_estadisticas()
            
        elif op == "0":
            print("Saliendo...")
            break
            
        else:
            print("Opcion invalida")
        
        input("Enter para continuar")

if __name__ == "__main__":
    main()
