import uuid
from validate import (
    validar_usuario,
    validar_email_unico,
    registrar_id,
    registrar_email,
    liberar_id,
    liberar_email,
    validar_nombre,
    validar_email,
    validar_estado,
)
from file import load_data, save_data

_usuarios: list[dict] = []


def inicializar():
    """Carga los usuarios desde el archivo al arrancar. Reconstruye los sets."""
    global _usuarios
    _usuarios = load_data()
    
    for u in _usuarios:
        registrar_id(u['id'])
        registrar_email(u['email'])


def new_register(**kwargs) -> dict:
    """
    Crea un usuario validado, lo guarda en memoria y persiste en archivo.
    ID generado automáticamente con uuid.
    """
    datos = validar_usuario(**kwargs)
    
    validar_email_unico(datos['email'])

    id_generado = str(uuid.uuid4())[:8]
    
    registrar_id(id_generado)
    registrar_email(datos['email'])

    usuario = {'id': id_generado, **datos}
    _usuarios.append(usuario)
    
    save_data(_usuarios)
    return usuario


def list_records(solo_activos: bool = False, ordenar_por: str = 'nombre') -> list[dict]:
    """
    Lista usuarios en memoria.
    - solo_activos: filtra con list comprehension.
    - ordenar_por: ordena con lambda ('nombre', 'email', 'estado').
    """
    campos_validos = {'nombre', 'email', 'estado', 'id'}
    if ordenar_por not in campos_validos:
        ordenar_por = 'nombre'
    resultado = [u for u in _usuarios if u['estado'] == 'activo'] if solo_activos else _usuarios[:]
    resultado.sort(key=lambda u: u[ordenar_por].lower())
    return resultado


def search_record(id_usuario: str = None, email: str = None) -> dict:
    """
    Busca un usuario por ID o por email.
    Usa lambda dentro de filter() para la búsqueda.
    Lanza ValueError si no se encuentra.
    """
    if not id_usuario and not email:
        raise ValueError("Debes proporcionar un ID o un email para buscar.")

    if id_usuario:
        encontrado = next(
            filter(lambda u: u['id'] == id_usuario.strip(), _usuarios),
            None
        )
        if not encontrado:
            raise ValueError(f"No existe un usuario con ID '{id_usuario}'.")
        return encontrado

    if email:
        email = email.strip().lower()
        encontrado = next(
            filter(lambda u: u['email'] == email, _usuarios),
            None
        )
        if not encontrado:
            raise ValueError(f"No existe un usuario con email '{email}'.")
        return encontrado


def update_record(id_usuario: str, **kwargs) -> dict:
    """
    Actualiza nombre, email o estado de un usuario por ID.
    Solo actualiza los campos que se pasen en **kwargs.
    Persiste los cambios en archivo.
    """
    usuario = search_record(id_usuario=id_usuario)

    if not kwargs:
        raise ValueError("Debes enviar al menos un campo para actualizar.")

    campos_validos = {'nombre', 'email', 'estado'}
    for campo in kwargs:
        if campo not in campos_validos:
            raise ValueError(f"El campo '{campo}' no es editable.")

    if 'nombre' in kwargs:
        usuario['nombre'] = validar_nombre(kwargs['nombre'])

    if 'email' in kwargs:
        nuevo_email = validar_email(kwargs['email'])
        if nuevo_email != usuario['email']:
            validar_email_unico(nuevo_email)
            liberar_email(usuario['email'])
            registrar_email(nuevo_email)
            usuario['email'] = nuevo_email

    if 'estado' in kwargs:
        usuario['estado'] = validar_estado(kwargs['estado'])

    save_data(_usuarios)
    return usuario


def delete_record(id_usuario: str) -> dict:
    """
    Elimina un usuario por ID.
    Libera el ID y email de los sets de control.
    Persiste los cambios en archivo.
    """
    global _usuarios

    usuario = search_record(id_usuario=id_usuario)

    _usuarios = [u for u in _usuarios if u['id'] != id_usuario]

    liberar_id(usuario['id'])
    liberar_email(usuario['email'])

    save_data(_usuarios)
    return usuario