import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from service import crear_usuario, listar_usuarios


def imprimir_linea():
    print("-" * 45)


def imprimir_usuario(u: dict):
    estado_icono = "🟢" if u['estado'] == 'activo' else "🔴"
    print(f"  {estado_icono} [{u['id']}] {u['nombre']} — {u['email']}")


def opcion_crear():
    print("\n📝 Crear usuario")
    imprimir_linea()
    try:
        nombre = input("Nombre   : ").strip()
        email  = input("Email    : ").strip()
        estado = input("Estado (activo/inactivo): ").strip()

        usuario = crear_usuario(nombre=nombre, email=email, estado=estado)
        print(f"✅ Usuario creado exitosamente. ID asignado: {usuario['id']}")
    except ValueError as e:
        print(f"⚠️  Error: {e}")


def opcion_listar():
    print("\n📋 Listar usuarios")
    imprimir_linea()
    filtro = input("¿Mostrar solo activos? (s/n): ").strip().lower()
    solo_activos = filtro == 's'

    usuarios = listar_usuarios(solo_activos=solo_activos)

    if not usuarios:
        print("  Sin registros para mostrar.")
    else:
        for u in usuarios:
            imprimir_usuario(u)

    print(f"\n  Total: {len(usuarios)} usuario(s)")


OPCIONES = {
    "1": ("Crear usuario",   opcion_crear),
    "2": ("Listar usuarios", opcion_listar),
    "0": ("Salir",           None),
}


def mostrar_menu():
    print("\n╔══════════════════════════════╗")
    print("║    GESTIÓN DE USUARIOS        ║")
    print("╠═══════════════════════════════╣")
    for clave, (descripcion, _) in OPCIONES.items():
        print(f"║  {clave}. {descripcion:<26}║")
    print("╚═══════════════════════════════╝")


def main():
    print("Sistema listo")
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "0":
            print("👋 Hasta luego.")
            break
        elif opcion in OPCIONES:
            _, accion = OPCIONES[opcion]
            accion()
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()