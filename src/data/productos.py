from dataclasses import dataclass, field

@dataclass
class Producto:
    nombre: str
    precio: float
    dict_productos: dict[str, float] = field(default_factory=dict, init=False)

    def añadir_producto(self, nombre_producto: str, valor_producto: float):
        self.dict_productos[nombre_producto] = valor_producto
        
    def modificar_precio_producto(self, nombre_producto: str, valor_producto: float):
        try:
            self.dict_productos[nombre_producto] = valor_producto
        except:
            print("Producto no existe")
            
    def eliminar_producto(self, nombre_producto: str):
        try:
            del self.dict_productos[nombre_producto]
        except:
            print("Producto no existe")
            
    def mostrar_productos(self):
        print(self.dict_productos)