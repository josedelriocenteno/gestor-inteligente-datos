# src/main.py
from data.usuarios import GestorUsuarios
from data.productos import Producto  # Asumiendo tienes data/productos.py
from services.estadisticas import EstadisticasUsuarios, EstadisticasProductos
from utils.validaciones import Validaciones

def mostrar_menu_principal():
    print("\n" + "="*60)
    print("🛒 GESTOR INTELIGENTE DE DATOS - STARTUP DAM 25-26")
    print("="*60)
    print("1️⃣  ➕ Añadir usuario")
    print("2️⃣  📋 Mostrar usuarios") 
    print("3️⃣  🔍 Buscar por ciudad")
    print("4️⃣  🆔 Buscar por ID")
    print("5️⃣  📦 Añadir producto")
    print("6️⃣  💰 Modificar precio")
    print("7️⃣  🗑️  Eliminar producto")
    print("8️⃣  📊 Mostrar productos")
    print("9️⃣  📈 ESTADÍSTICAS COMPLETAS")
    print("0️⃣  ❌ SALIR")
    print("="*60)

def main():
    # Instancias globales
    gestor_usuarios = GestorUsuarios()
    catalogo_productos = Producto("Catálogo General", 0.0)
    
    print("🚀 Iniciando Gestor Inteligente de Datos...")
    
    while True:
        mostrar_menu_principal()
        op = input("👉 Elige opción (0-9): ").strip()
        
        if op == "1":
            gestor_usuarios.registrar_usuario_interactivo()
            
        elif op == "2":
            gestor_usuarios.mostrar_usuarios()
            
        elif op == "3":
            ciudad = input("🏙️ Ciudad a buscar: ").strip()
            gestor_usuarios.buscar_por_ciudad(ciudad)
            
        elif op == "4":
            id_buscar = input("🆔 ID a buscar: ").strip()
            gestor_usuarios.buscar_por_id(Validaciones.validar_id(id_buscar))
            
        elif op == "5":
            nombre_prod = input("📦 Nombre producto: ").strip()
            precio = Validaciones.validar_precio(input("💰 Precio: "))
            if precio:
                catalogo_productos.añadir_producto(nombre_prod, precio)
                
        elif op == "6":
            nombre = input("📦 Nombre producto: ").strip()
            precio_nuevo = Validaciones.validar_precio(input("💰 Nuevo precio: "))
            if precio_nuevo:
                catalogo_productos.modificar_precio_producto(nombre, precio_nuevo)
                
        elif op == "7":
            nombre = input("🗑️  Nombre a eliminar: ").strip()
            catalogo_productos.eliminar_producto(nombre)
            
        elif op == "8":
            catalogo_productos.mostrar_productos()
            
        elif op == "9":
            # Estadísticas usuarios
            stats_usuarios = EstadisticasUsuarios(gestor_usuarios.obtener_usuarios())
            stats_usuarios.mostrar()
            
            # Estadísticas productos
            stats_productos = EstadisticasProductos(catalogo_productos.dict_productos)
            stats_productos.mostrar()
            
        elif op == "0":
            print("\n👋 ¡Gracias por usar el Gestor Inteligente!")
            print("📤 Proyecto listo para Moodle 30/01/2026 ✅")
            break
            
        else:
            print("❌ Opción inválida. Elige 0-9")
        
        input("\n⏸️  Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
