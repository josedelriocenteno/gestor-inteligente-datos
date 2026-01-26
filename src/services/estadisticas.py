def estadisticas_usuarios(usuarios):
    total_usuarios = len(usuarios)
    if total_usuarios == 0:
        return {
            "total":0,
            "edad_media":0,
            "mas_joven":0,
            "mas_mayor":0,
        }
        
    edades = [u[2] for u in usuarios]
    edad_media = sum(edades) / total_usuarios
    
    mas_joven = min(usuarios, key=lambda u: u[2])
    mas_mayor = max(usuarios, key=lambda u: u[2])
    
    return {
        "total":total_usuarios,
        "edad_media":edad_media,
        "mas_joven":mas_joven,
        "mas_mayor":mas_mayor,
    }
    
def estadisticas_productos(productos):
    total_productos = len(productos)
    if total_productos == 0:
        return{
            "total":0,
            "precio_media":0
        }
            
    precios = list(productos.values())
    precio_medio = sum(precios) / total_productos
        
    return {
        "total": total_productos,
        "precio_media": precio_medio
    }