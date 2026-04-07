import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from service import inicializar, new_register, list_records, search_record, update_record, delete_record


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
        usuario = new_register(nombre=nombre, email=email, estado=estado)
        print(f"✅ Usuario creado exitosamente. ID asignado: {usuario['id']}")
    except ValueError as e:
        print(f"⚠️  Error: {e}")


def opcion_listar():
    print("\n📋 Listar usuarios")
    imprimir_linea()
    filtro  = input("¿Mostrar solo activos? (s/n): ").strip().lower()
    ordenar = input("Ordenar por (nombre/email/estado): ").strip().lower() or 'nombre'

    usuarios = list_records(solo_activos=(filtro == 's'), ordenar_por=ordenar)

    if not usuarios:
        print("  Sin registros para mostrar.")
    else:
        for u in usuarios:
            imprimir_usuario(u)

    print(f"\n  Total: {len(usuarios)} usuario(s)")

def opcion_buscar():
    print("\n🔍 Buscar usuario")
    imprimir_linea()
    print("  1. Buscar por ID")
    print("  2. Buscar por email")
    criterio = input("Opción: ").strip()

    try:
        if criterio == '1':
            id_u = input("ID: ").strip()
            u = search_record(id_usuario=id_u)
        elif criterio == '2':
            email = input("Email: ").strip()
            u = search_record(email=email)
        else:
            print("❌ Opción no válida.")
            return

        print("\n  Usuario encontrado:")
        imprimir_usuario(u)
    except ValueError as e:
        print(f"⚠️  {e}")


def opcion_actualizar():
    print("\n✏️  Actualizar usuario")
    imprimir_linea()
    try:
        id_u = input("ID del usuario a actualizar: ").strip()

        
        search_record(id_usuario=id_u)

        print("  Deja en blanco los campos que no quieras cambiar.")
        nombre = input("Nuevo nombre   : ").strip()
        email  = input("Nuevo email    : ").strip()
        estado = input("Nuevo estado (activo/inactivo): ").strip()

        
        cambios = {}
        if nombre: cambios['nombre'] = nombre
        if email:  cambios['email']  = email
        if estado: cambios['estado'] = estado

        if not cambios:
            print("⚠️  No se realizaron cambios.")
            return

        usuario = update_record(id_u, **cambios)
        print(f"✅ Usuario '{usuario['id']}' actualizado correctamente.")
        imprimir_usuario(usuario)
    except ValueError as e:
        print(f"⚠️  Error: {e}")


def opcion_eliminar():
    print("\n🗑️  Eliminar usuario")
    imprimir_linea()
    try:
        id_u = input("ID del usuario a eliminar: ").strip()

        
        u = search_record(id_usuario=id_u)
        print(f"\n  Usuario a eliminar:")
        imprimir_usuario(u)

        confirmar = input("\n  ¿Confirmas la eliminación? (s/n): ").strip().lower()
        if confirmar != 's':
            print("  Eliminación cancelada.")
            return

        delete_record(id_u)
        print(f"✅ Usuario '{id_u}' eliminado correctamente.")
    except ValueError as e:
        print(f"⚠️  Error: {e}")




OPCIONES = {
    "1": ("Crear usuario",      opcion_crear),
    "2": ("Listar usuarios",    opcion_listar),
    "3": ("Buscar usuario",     opcion_buscar),
    "4": ("Actualizar usuario", opcion_actualizar),
    "5": ("Eliminar usuario",   opcion_eliminar),
    "0": ("Salir",              None),
}


def mostrar_menu():
    print("\n╔══════════════════════════════╗")
    print("║    GESTIÓN DE USUARIOS       ║")
    print("╠══════════════════════════════╣")
    for clave, (descripcion, _) in OPCIONES.items():
        print(f"║  {clave}. {descripcion:<26}║")
    print("╚══════════════════════════════╝")


def main():
    print("Sistema listo")
    inicializar()

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