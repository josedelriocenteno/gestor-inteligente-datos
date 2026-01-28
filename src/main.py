usuarios = []
dict_productos = {}

def añadir_producto(nombre_producto, valor_producto):
    dict_productos[nombre_producto] = valor_producto
    print("Producto añadido ", nombre_producto, valor_producto)

def modificar_precio_producto(nombre_producto, valor_producto):
    if nombre_producto in dict_productos:
        dict_productos[nombre_producto] = valor_producto
        print("Precio modificado ", nombre_producto)
    else:
        print("Producto no existe")

def eliminar_producto(nombre_producto):
    if nombre_producto in dict_productos:
        del dict_productos[nombre_producto]
        print("Producto eliminado")
    else:
        print("Producto no existe")

def mostrar_productos():
    if dict_productos:
        print("CATALOGO PRODUCTOS")
        for nombre, precio in dict_productos.items():
            print(nombre, ":", precio)
    else:
        print("Catalogo vacio")

def registrar_usuario(id_usuario, nombre, edad, ciudad):
    usuario = (id_usuario, nombre, edad, ciudad)
    usuarios.append(usuario)
    print("Usuario", nombre, "registrado ID:", id_usuario)

def mostrar_usuarios():
    if not usuarios:
        print("Sin usuarios")
        return
    
    print("LISTA USUARIOS")
    for i, u in enumerate(usuarios, 1):
        print(i, "ID:", u[0], u[1], u[2], "años", u[3])

def buscar_por_ciudad(ciudad):
    encontrados = []
    for u in usuarios:
        if u[3].lower() == ciudad.lower():
            encontrados.append(u)
    if encontrados:
        print("Usuarios en", ciudad)
        for u in encontrados:
            print(u[1], "ID", u[0])
    else:
        print("No hay usuarios en", ciudad)

def buscar_por_id(id_buscar):
    for u in usuarios:
        if u[0] == id_buscar:
            print("Encontrado:", u[1], u[2], "años", u[3])
            return
    print("Usuario ID", id_buscar, "no existe")

def estadisticas_usuarios(usuarios_list):
    total_usuarios = len(usuarios_list)
    if total_usuarios == 0:
        return {"total": 0, "edad_media": 0, "mas_joven": None, "mas_mayor": None}
    
    suma_edades = 0
    for u in usuarios_list:
        suma_edades = suma_edades + u[2]
    edad_media = suma_edades / total_usuarios
    
    mas_joven_edad = 999
    mas_mayor_edad = 0
    mas_joven = None
    mas_mayor = None
    
    for u in usuarios_list:
        if u[2] < mas_joven_edad:
            mas_joven_edad = u[2]
            mas_joven = u
        if u[2] > mas_mayor_edad:
            mas_mayor_edad = u[2]
            mas_mayor = u
    
    return {
        "total": total_usuarios,
        "edad_media": round(edad_media, 1),
        "mas_joven": mas_joven,
        "mas_mayor": mas_mayor,
    }

def estadisticas_productos(productos_dict):
    total_productos = len(productos_dict)
    if total_productos == 0:
        return {"total": 0, "precio_medio": 0.0}
        
    precios = []
    for precio in productos_dict.values():
        precios.append(precio)

    precio_medio = sum(precios) / total_productos
    
    return {
        "total": total_productos,
        "precio_medio": round(precio_medio, 2)
    }

def mostrar_estadisticas():
    stats_u = estadisticas_usuarios(usuarios)
    print("USUARIOS:", stats_u['total'])
    print("Edad media:", stats_u['edad_media'])
    
    stats_p = estadisticas_productos(dict_productos)
    print("PRODUCTOS:", stats_p['total'])
    print("Precio medio:", stats_p['precio_medio'])

def validar_id(texto):
    try:
        id_val = int(texto.strip())
        if id_val > 0:
            return id_val
        print("ID debe ser > 0")
        return None
    except ValueError:
        print("ID debe ser numero entero")
        return None

def validar_edad(texto):
    try:
        edad = int(texto.strip())
        if 16 <= edad <= 100:
            return edad
        print("Edad entre 16-100")
        return None
    except ValueError:
        print("Edad debe ser numero")
        return None

def validar_precio(texto):
    try:
        precio = float(texto.strip())
        if precio > 0:
            return precio
        print("Precio debe ser > 0")
        return None
    except ValueError:
        print("Precio debe ser numero")
        return None

def validar_nombre(texto):
    nombre = texto.strip()
    if 1 <= len(nombre) <= 50:
        return nombre.title()
    print("Nombre 1-50 letras")
    return None

def validar_ciudad(texto):
    ciudad = texto.strip().title()
    if len(ciudad) >= 2:
        return ciudad
    print("Ciudad minimo 2 chars")
    return None

def validar_usuario_completo():
    id_u = validar_id(input("ID: "))
    if not id_u: return None
    
    nom = validar_nombre(input("Nombre: "))
    if not nom: return None
    
    ed = validar_edad(input("Edad: "))
    if not ed: return None
    
    ciu = validar_ciudad(input("Ciudad: "))
    if not ciu: return None
    
    return (id_u, nom, ed, ciu)

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
