from modelos.usuario import Usuario
from modelos.registro import RegistroSistema


class GestorUsuarios:

    def __init__(self, ruta_log: str):

        # Inicializa el gestor y crea un sistema de registro
        self.usuarios = []
        self.registro = RegistroSistema(ruta_log)

    def registrar_usuario(self, nombre: str, email: str):

        # Crea un usuario y lo almacena
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)
        self.registro.escribir(f"Usuario registrado: {nombre} - {email}")
        return usuario

    def desactivar_usuario(self, usuario: Usuario):
        # Desactiva un usuario existente
        usuario.desactivar()
        self.registro.escribir(f"Usuario desactivado: {usuario.nombre}")

    def listar_usuarios(self):
        # Devuelve lista de usuarios
        return self.usuarios
