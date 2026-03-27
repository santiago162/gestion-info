import uuid
from validate import (
    validar_usuario,
    validar_email_unico,
    registrar_id,
    registrar_email,
    liberar_id,
    liberar_email,
)

_usuarios: list[dict] = []


def crear_usuario(**kwargs) -> dict:
    """
    Crea un usuario validado y lo guarda en memoria.
    El ID se genera automáticamente con uuid.
    """
    datos = validar_usuario(**kwargs)

    validar_email_unico(datos['email'])

    id_generado = str(uuid.uuid4())[:8]

    registrar_id(id_generado)
    registrar_email(datos['email'])

    usuario = {'id': id_generado, **datos}
    _usuarios.append(usuario)
    return usuario


def listar_usuarios(solo_activos: bool = False) -> list[dict]:
    """
    Lista usuarios en memoria.
    Si solo_activos=True filtra con list comprehension.
    """
    if solo_activos:
        return [u for u in _usuarios if u['estado'] == 'activo']
    return _usuarios[:]