# lista
usuarios = []

# registrar usuarios
def registrar_usuario(id_usuario, nombre, edad, ciudad):
    # creacion de tupla
    usuario = (id_usuario, nombre, edad, ciudad)
    # guardar en lista
    usuarios.append(usuario)