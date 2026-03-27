import re

_ids_usados = set()
_emails_usados = set()

ESTADOS_VALIDOS = {"activo", "inactivo"}


def validar_nombre(nombre: str) -> str:
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    if len(nombre) < 2:
        raise ValueError("El nombre debe tener al menos 2 caracteres.")
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', nombre):
        raise ValueError("El nombre solo puede contener letras y espacios.")
    return nombre


def validar_email(email: str) -> str:
    email = email.strip().lower()
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(patron, email):
        raise ValueError(f"El email '{email}' no tiene un formato válido.")
    return email


def validar_estado(estado: str) -> str:
    estado = estado.strip().lower()
    if estado not in ESTADOS_VALIDOS:
        raise ValueError(f"El estado debe ser 'activo' o 'inactivo'. Se recibió: '{estado}'")
    return estado


def validar_email_unico(email: str):
    if email in _emails_usados:
        raise ValueError(f"El email '{email}' ya está registrado.")


def registrar_id(id_usuario: str):
    _ids_usados.add(id_usuario)


def liberar_id(id_usuario: str):
    _ids_usados.discard(id_usuario)


def registrar_email(email: str):
    _emails_usados.add(email)


def liberar_email(email: str):
    _emails_usados.discard(email)


def validar_usuario(**kwargs) -> dict:
    """
    Valida los campos de un usuario usando **kwargs.
    El ID no se valida aquí porque se genera automáticamente.
    """
    campos = ['nombre', 'email', 'estado']
    for campo in campos:
        if campo not in kwargs:
            raise ValueError(f"Falta el campo requerido: '{campo}'")

    return {
        'nombre': validar_nombre(kwargs['nombre']),
        'email':  validar_email(kwargs['email']),
        'estado': validar_estado(kwargs['estado']),
    }