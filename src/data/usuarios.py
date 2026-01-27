from typing import List, Tuple
from dataclasses import dataclass, field
from utils.validaciones import Validaciones


@dataclass
class GestorUsuarios:
    usuarios: List[Tuple[int, str, int, str]] = field(default_factory=list)
    
    def registrar_usuario(self, id_usuario: int, nombre: str, edad: int, ciudad: str):
        usuario = (id_usuario, nombre, edad, ciudad)
        self.usuarios.append(usuario)
        print(f"Usuario {nombre} registrado (ID: {id_usuario})")
    
    def registrar_usuario_interactivo(self):
        usuario = Validaciones.validar_usuario_completo()
        if usuario:
            self.registrar_usuario(*usuario)
    
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("Sin usuarios registrados")
            return
        
        print("\nLISTA USUARIOS:")
        print("-" * 50)
        for i, u in enumerate(self.usuarios, 1):
            print(f"{i}. ID:{u[0]} | {u[1]} | {u[2]} años | {u[3]}")
    
    def buscar_por_ciudad(self, ciudad: str):
        encontrados = [u for u in self.usuarios if u[3].lower() == ciudad.lower()]
        if encontrados:
            print(f"\nUsuarios en {ciudad}:")
            for u in encontrados:
                print(f"  {u[1]} (ID:{u[0]}, {u[2]} años)")
        else:
            print(f"No hay usuarios en {ciudad}")
    
    def buscar_por_id(self, id_buscar: int):
        for u in self.usuarios:
            if u[0] == id_buscar:
                print(f"Encontrado: {u[1]}, {u[2]} años, {u[3]}")
                return
        print(f"Usuario ID {id_buscar} no existe")
    
    def obtener_usuarios(self) -> List[Tuple[int, str, int, str]]:
        return self.usuarios
