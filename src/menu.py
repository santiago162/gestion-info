from colorama import init, Fore, Style
from service import (
    new_register, list_records, search_record,
    update_record, delete_record
)
from integration import generar_usuarios_falsos

init(autoreset=True)



def ok(msg):     print(Fore.GREEN  + f"✅ {msg}")
def error(msg):  print(Fore.RED    + f"⚠️  {msg}")
def info(msg):   print(Fore.CYAN   + f"   {msg}")
def titulo(msg): print(Fore.YELLOW + Style.BRIGHT + f"\n{msg}")
def linea():     print(Fore.WHITE  + Style.DIM + "-" * 45)


def imprimir_usuario(u: dict):
    icono = Fore.GREEN + "🟢" if u['estado'] == 'activo' else Fore.RED + "🔴"
    print(
        icono +
        Fore.WHITE + f" [{u['id']}] " +
        Fore.CYAN  + Style.BRIGHT + u['nombre'] +
        Fore.WHITE + f" — {u['email']}"
    )



def opcion_crear():
    titulo("📝 CREAR USUARIO")
    linea()
    try:
        nombre = input(Fore.CYAN + "Nombre   : " + Style.RESET_ALL).strip()
        email  = input(Fore.CYAN + "Email    : " + Style.RESET_ALL).strip()
        estado = input(Fore.CYAN + "Estado (activo/inactivo): " + Style.RESET_ALL).strip()

        usuario = new_register(nombre=nombre, email=email, estado=estado)
        ok(f"Usuario creado exitosamente. ID asignado: {Fore.YELLOW}{usuario['id']}")
    except ValueError as e:
        error(e)


def opcion_listar():
    titulo("📋 LISTAR USUARIOS")
    linea()

    filtro  = input(Fore.CYAN + "¿Mostrar solo activos? (s/n): " + Style.RESET_ALL).strip().lower()
    ordenar = input(Fore.CYAN + "Ordenar por (nombre/email/estado): " + Style.RESET_ALL).strip().lower() or 'nombre'

    usuarios = list_records(solo_activos=(filtro == 's'), ordenar_por=ordenar)

    linea()
    if not usuarios:
        info("Sin registros para mostrar.")
    else:
        for u in usuarios:
            imprimir_usuario(u)

    print(Fore.YELLOW + f"\n   Total: {len(usuarios)} usuario(s)")


def opcion_buscar():
    titulo("🔍 BUSCAR USUARIO")
    linea()
    print(Fore.WHITE + "  1. Buscar por ID")
    print(Fore.WHITE + "  2. Buscar por email")

    try:
        criterio = input(Fore.CYAN + "Opción: " + Style.RESET_ALL).strip()

        if criterio == '1':
            id_u = input(Fore.CYAN + "ID: " + Style.RESET_ALL).strip()
            u = search_record(id_usuario=id_u)
        elif criterio == '2':
            email = input(Fore.CYAN + "Email: " + Style.RESET_ALL).strip()
            u = search_record(email=email)
        else:
            error("Opción no válida.")
            return

        linea()
        info("Usuario encontrado:")
        imprimir_usuario(u)
    except ValueError as e:
        error(e)


def opcion_actualizar():
    titulo("✏️  ACTUALIZAR USUARIO")
    linea()
    try:
        id_u = input(Fore.CYAN + "ID del usuario a actualizar: " + Style.RESET_ALL).strip()

        u_actual = search_record(id_usuario=id_u)
        info("Usuario actual:")
        imprimir_usuario(u_actual)

        print(Fore.WHITE + Style.DIM + "\n   Deja en blanco los campos que no quieras cambiar.")
        nombre = input(Fore.CYAN + "Nuevo nombre   : " + Style.RESET_ALL).strip()
        email  = input(Fore.CYAN + "Nuevo email    : " + Style.RESET_ALL).strip()
        estado = input(Fore.CYAN + "Nuevo estado (activo/inactivo): " + Style.RESET_ALL).strip()

        cambios = {}
        if nombre: cambios['nombre'] = nombre
        if email:  cambios['email']  = email
        if estado: cambios['estado'] = estado

        if not cambios:
            error("No se realizaron cambios.")
            return

        usuario = update_record(id_u, **cambios)
        ok("Usuario actualizado correctamente.")
        imprimir_usuario(usuario)
    except ValueError as e:
        error(e)


def opcion_eliminar():
    titulo("🗑️  ELIMINAR USUARIO")
    linea()
    try:
        id_u = input(Fore.CYAN + "ID del usuario a eliminar: " + Style.RESET_ALL).strip()

        u = search_record(id_usuario=id_u)
        info("Usuario a eliminar:")
        imprimir_usuario(u)

        confirmar = input(Fore.RED + "\n   ¿Confirmas la eliminación? (s/n): " + Style.RESET_ALL).strip().lower()
        if confirmar != 's':
            info("Eliminación cancelada.")
            return

        delete_record(id_u)
        ok(f"Usuario '{id_u}' eliminado correctamente.")
    except ValueError as e:
        error(e)


def opcion_generar_falsos():
    titulo("🤖 GENERAR USUARIOS FALSOS")
    linea()
    try:
        entrada = input(Fore.CYAN + "¿Cuántos usuarios generar? (Enter = 10): " + Style.RESET_ALL).strip()

        if entrada == "":
            cantidad = 10
        else:
            cantidad = int(entrada)
            if cantidad <= 0:
                error("La cantidad debe ser mayor a 0.")
                return
            if cantidad > 100:
                error("Máximo 100 usuarios por generación.")
                return

        print(Fore.WHITE + Style.DIM + f"\n   Generando {cantidad} usuario(s)...\n")

        creados, errores = generar_usuarios_falsos("demo", cantidad=cantidad)

        linea()
        for u in creados:
            imprimir_usuario(u)

        linea()
        ok(f"{len(creados)} usuario(s) generado(s) y guardados en archivo.")
        if errores > 0:
            info(f"{errores} usuario(s) omitidos por email duplicado.")

    except ValueError:
        error("Debes ingresar un número entero válido.")


OPCIONES = {
    "1": ("Crear usuario",           opcion_crear),
    "2": ("Listar usuarios",         opcion_listar),
    "3": ("Buscar usuario",          opcion_buscar),
    "4": ("Actualizar usuario",      opcion_actualizar),
    "5": ("Eliminar usuario",        opcion_eliminar),
    "6": ("Generar usuarios falsos", opcion_generar_falsos),
    "0": ("Salir",                   None),
}


def mostrar_menu():
    print(Fore.YELLOW + Style.BRIGHT + "\n╔════════════════════════════════════╗")
    print(Fore.YELLOW + Style.BRIGHT +   "║      GESTIÓN DE USUARIOS           ║")
    print(Fore.YELLOW + Style.BRIGHT +   "╠════════════════════════════════════╣")
    for clave, (descripcion, _) in OPCIONES.items():
        color = Fore.RED if clave == "0" else Fore.WHITE
        print(Fore.YELLOW + Style.BRIGHT + "║" + color + f"  {clave}. {descripcion:<32}" + Fore.YELLOW + Style.BRIGHT + "║")
    print(Fore.YELLOW + Style.BRIGHT +   "╚════════════════════════════════════╝")


def ejecutar_menu():
    """
    Bucle principal del menú.
    No se rompe si el usuario escribe letras o deja vacío.
    """
    while True:
        mostrar_menu()

        try:
            opcion = input(Fore.CYAN + "Selecciona una opción: " + Style.RESET_ALL).strip()
        except (KeyboardInterrupt, EOFError):
            print()
            info("Salida forzada. Hasta luego.")
            break

        if opcion == "0":
            print(Fore.GREEN + "\n👋 Hasta luego.")
            break
        elif opcion in OPCIONES:
            _, accion = OPCIONES[opcion]
            accion()
        elif opcion == "":
            error("Debes escribir una opción.")
        else:
            error(f"Opción '{opcion}' no válida. Elige entre 0 y 6.")