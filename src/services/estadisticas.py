from typing import Dict, Any, List, Tuple
from dataclasses import dataclass, field


@dataclass
class EstadisticasUsuarios:
    usuarios_list: List[Tuple[int, str, int, str]] = field(default_factory=list)
    
    def calcular(self) -> Dict[str, Any]:
        total_usuarios = len(self.usuarios_list)
        if total_usuarios == 0:
            return {"total": 0, "edad_media": 0, "mas_joven": None, "mas_mayor": None}
        
        edades = [u[2] for u in self.usuarios_list]
        edad_media = sum(edades) / total_usuarios
        
        mas_joven = min(self.usuarios_list, key=lambda u: u[2])
        mas_mayor = max(self.usuarios_list, key=lambda u: u[2])
        
        return {
            "total": total_usuarios,
            "edad_media": round(edad_media, 1),
            "mas_joven": mas_joven,
            "mas_mayor": mas_mayor,
        }
    
    def mostrar(self):
        stats = self.calcular()
        print(f"USUARIOS: {stats['total']}")
        print(f"Edad media: {stats['edad_media']} años")
        if stats['mas_joven']:
            print(f"Mas joven: {stats['mas_joven']}")
        if stats['mas_mayor']:
            print(f"Mas mayor: {stats['mas_mayor']}")


@dataclass
class EstadisticasProductos:
    productos_dict: Dict[str, float] = field(default_factory=dict)
    
    def calcular(self) -> Dict[str, float]:
        total_productos = len(self.productos_dict)
        if total_productos == 0:
            return {"total": 0, "precio_medio": 0.0}
            
        precios = list(self.productos_dict.values())
        precio_medio = sum(precios) / total_productos
        
        return {
            "total": total_productos,
            "precio_medio": round(precio_medio, 2)
        }
    
    def mostrar(self):
        stats = self.calcular()
        print(f"PRODUCTOS: {stats['total']}")
        print(f"Precio medio: €{stats['precio_medio']}")
