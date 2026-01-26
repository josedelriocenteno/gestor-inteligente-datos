from dataclasses import dataclass, field

@dataclass
class Producto:
    nombre: str
    precio: float
    dict_productos: dict[str, float] = field(default_factory=dict, init=False)

    def añadir_producto(self, nombre_producto: str, valor_producto: float):
        self.dict_productos[nombre_producto] = valor_producto
        
    def modificar_precio_producto(self, nombre_producto: str, valor_producto: float):
        if nombre_producto in self.dict_productos:
            self.dict_productos[nombre_producto] = valor_producto
        else:
            print("❌ Producto no existe")
            
    def eliminar_producto(self, nombre_producto: str):
        if nombre_producto in self.dict_productos:
            del self.dict_productos[nombre_producto]
            print("✅ Producto eliminado")
        else:
            print("❌ Producto no existe")
            
    def mostrar_productos(self):
        if self.dict_productos:
            for nombre, precio in self.dict_productos.items():
                print(f"📦 {nombre}: €{precio:.2f}")
        else:
            print("📭 Catálogo vacío")