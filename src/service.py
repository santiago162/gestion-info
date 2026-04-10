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


def inicializar() -> None:
    """
    Carga los usuarios desde el archivo al arrancar el programa.
    Reconstruye los sets de IDs y emails usados para mantener
    la integridad de los datos en memoria.
    """
    global _usuarios
    _usuarios = load_data()
    for u in _usuarios:
        registrar_id(u['id'])
        registrar_email(u['email'])


def new_register(**kwargs) -> dict:
    """
    Crea un usuario validado, lo agrega en memoria y persiste en archivo.

    Args:
        **kwargs: nombre (str), email (str), estado (str)

    Returns:
        dict: usuario creado con ID generado automáticamente.

    Raises:
        ValueError: si algún campo es inválido o el email ya existe.
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
    Retorna la lista de usuarios en memoria.

    Args:
        solo_activos (bool): si True, filtra solo usuarios con estado 'activo'.
        ordenar_por (str): campo por el cual ordenar ('nombre', 'email', 'estado').

    Returns:
        list[dict]: lista de usuarios ordenada.
    """
    campos_validos = {'nombre', 'email', 'estado', 'id'}
    if ordenar_por not in campos_validos:
        ordenar_por = 'nombre'
    resultado = [u for u in _usuarios if u['estado'] == 'activo'] if solo_activos else _usuarios[:]
    resultado.sort(key=lambda u: u[ordenar_por].lower())
    return resultado


def search_record(id_usuario: str = None, email: str = None) -> dict:
    """
    Busca un usuario por ID o por email usando filter y lambda.

    Args:
        id_usuario (str): ID del usuario a buscar.
        email (str): email del usuario a buscar.

    Returns:
        dict: usuario encontrado.

    Raises:
        ValueError: si no se proporciona criterio o no se encuentra el usuario.
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
    Actualiza los campos de un usuario existente por ID.

    Args:
        id_usuario (str): ID del usuario a actualizar.
        **kwargs: campos a actualizar (nombre, email, estado).

    Returns:
        dict: usuario con los datos actualizados.

    Raises:
        ValueError: si el ID no existe, no hay campos o un campo no es editable.
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
    Elimina un usuario por ID y persiste el cambio en archivo.

    Args:
        id_usuario (str): ID del usuario a eliminar.

    Returns:
        dict: usuario eliminado.

    Raises:
        ValueError: si el ID no existe.
    """
    global _usuarios

    usuario = search_record(id_usuario=id_usuario)

    _usuarios = [u for u in _usuarios if u['id'] != id_usuario]

    liberar_id(usuario['id'])
    liberar_email(usuario['email'])

    save_data(_usuarios)
    return usuario