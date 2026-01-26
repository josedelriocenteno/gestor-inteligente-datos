usuarios = []
productos = {}

def anadir_usuario():
    try:
        id_u = int(input("ID: "))
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        ciudad = input("Ciudad: ")
        usuarios.append((id_u, nombre, edad, ciudad))
        print("Añadido.")
    except ValueError:
        print("ID/edad inválidos.")

def mostrar_usuarios():
    for u in usuarios:
        print(u)

def estadisticas():
    if usuarios:
        edades = [u[2] for u in usuarios]
        print(f"Usuarios: {len(usuarios)}, Media edad: {sum(edades)/len(usuarios):.1f}")
        print(f"Más joven: {min(usuarios, key=lambda x: x[2])}")
        print(f"Más mayor: {max(usuarios, key=lambda x: x[2])}")
    if productos:
        precios = list(productos.values())
        print(f"Productos: {len(productos)}, Precio medio: {sum(precios)/len(precios):.2f}")

# Añade resto: anadir_producto(), modificar_producto(), eliminar_producto(), mostrar_productos(),
# buscar_ciudad(), buscar_id() similar.

while True:
    print("\n1.Añadir usuario 2.Mostrar usuarios 3.Añadir producto 4.Mostrar productos")
    print("5.Estadísticas 6.Búsquedas 7.Salir")
    op = input("Elige: ")
    if op == "1": anadir_usuario()
    elif op == "2": mostrar_usuarios()
    elif op == "5": estadisticas()
    elif op == "7": break
    else: print("Opción inválida.")
