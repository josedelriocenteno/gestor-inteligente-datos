class Validaciones:
    @staticmethod
    def validar_id(texto: str):
        try:
            id_val = int(texto.strip())
            if id_val > 0:
                return id_val
            print("ID debe ser > 0")
            return None
        except ValueError:
            print("ID debe ser número entero")
            return None

    @staticmethod
    def validar_edad(texto: str):
        try:
            edad = int(texto.strip())
            if 16 <= edad <= 100:
                return edad
            print("Edad entre 16-100")
            return None
        except ValueError:
            print("Edad debe ser número")
            return None

    @staticmethod
    def validar_precio(texto: str):
        try:
            precio = float(texto.strip())
            if precio > 0:
                return precio
            print("Precio debe ser > 0")
            return None
        except ValueError:
            print("Precio debe ser número")
            return None

    @staticmethod
    def validar_nombre(texto: str):
        nombre = texto.strip()
        if 1 <= len(nombre) <= 50 and nombre.isalpha() or " " in nombre:
            return nombre.title()
        print("Nombre 1-50 letras")
        return None

    @staticmethod
    def validar_ciudad(texto: str):
        ciudad = texto.strip().title()
        if len(ciudad) >= 2:
            return ciudad
        print("Ciudad mínimo 2 chars")
        return None

    @staticmethod
    def validar_usuario():
        id_u = Validaciones.validar_id(input("ID: "))
        if not id_u: return None
        
        nom = Validaciones.validar_nombre(input("Nombre: "))
        if not nom: return None
        
        ed = Validaciones.validar_edad(input("Edad: "))
        if not ed: return None
        
        ciu = Validaciones.validar_ciudad(input("Ciudad: "))
        if not ciu: return None
        
        return (id_u, nom, ed, ciu)
