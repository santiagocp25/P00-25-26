from servicios.gestor_usuarios import GestorUsuarios


def main():
    print("=== INICIO DEL PROGRAMA ===")

    # Se crea el gestor → se ejecuta __init__ de RegistroSistema
    gestor = GestorUsuarios("log_sistema.txt")

    # Se ejecuta __init__ de Usuario
    u1 = gestor.registrar_usuario("Ana", "ana@email.com")
    u2 = gestor.registrar_usuario("Luis", "luis@email.com")

    gestor.desactivar_usuario(u2)

    print("\nUsuarios actuales:")
    for u in gestor.listar_usuarios():
        print(u)

    print("\nEliminando referencia a un usuario...")
    del u1  # Puede disparar __del__ de Usuario

    print("=== FIN DE main() ===")


if __name__ == "__main__":
    main()

    print("Programa finalizado. Python puede ejecutar destructores ahora.")
