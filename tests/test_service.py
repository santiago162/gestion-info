import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import service
import validate


def reset():
    """
    Limpia el estado global entre pruebas.
    Resetea la lista de usuarios y los sets de control.
    """
    service._usuarios.clear()
    validate._ids_usados.clear()
    validate._emails_usados.clear()



def test_crear_usuario_retorna_dict():
    reset()
    u = service.new_register(nombre="Pedro Gil", email="pedro@mail.com", estado="activo")
    assert isinstance(u, dict)
    assert u['nombre'] == "Pedro Gil"
    assert u['email']  == "pedro@mail.com"
    assert u['estado'] == "activo"
    assert 'id' in u

def test_crear_usuario_genera_id_automatico():
    reset()
    u = service.new_register(nombre="Marta López", email="marta@mail.com", estado="inactivo")
    assert u['id'] is not None
    assert len(u['id']) == 8

def test_crear_usuario_email_duplicado_lanza_error():
    reset()
    service.new_register(nombre="Luis Vera", email="luis@mail.com", estado="activo")
    with pytest.raises(ValueError, match="ya está registrado"):
        service.new_register(nombre="Otro Luis", email="luis@mail.com", estado="activo")

def test_crear_usuario_nombre_invalido_lanza_error():
    reset()
    with pytest.raises(ValueError):
        service.new_register(nombre="", email="x@mail.com", estado="activo")



def test_listar_todos_los_usuarios():
    reset()
    service.new_register(nombre="Ana Gil",    email="ana@mail.com",    estado="activo")
    service.new_register(nombre="Carlos Paz", email="carlos@mail.com", estado="inactivo")
    assert len(service.list_records()) == 2

def test_listar_solo_activos():
    reset()
    service.new_register(nombre="Ana Gil",    email="ana@mail.com",    estado="activo")
    service.new_register(nombre="Carlos Paz", email="carlos@mail.com", estado="inactivo")
    activos = service.list_records(solo_activos=True)
    assert len(activos) == 1
    assert activos[0]['nombre'] == "Ana Gil"

def test_listar_ordenado_por_nombre():
    reset()
    service.new_register(nombre="Zoila Ríos", email="zoila@mail.com", estado="activo")
    service.new_register(nombre="Ana Gil",    email="ana@mail.com",   estado="activo")
    resultado = service.list_records(ordenar_por='nombre')
    assert resultado[0]['nombre'] == "Ana Gil"
    assert resultado[1]['nombre'] == "Zoila Ríos"

def test_listar_retorna_lista_vacia_si_no_hay_usuarios():
    reset()
    assert service.list_records() == []



def test_buscar_por_id_existente():
    reset()
    u = service.new_register(nombre="Elena Mar", email="elena@mail.com", estado="activo")
    encontrado = service.search_record(id_usuario=u['id'])
    assert encontrado['email'] == "elena@mail.com"

def test_buscar_por_email_existente():
    reset()
    service.new_register(nombre="Elena Mar", email="elena@mail.com", estado="activo")
    encontrado = service.search_record(email="elena@mail.com")
    assert encontrado['nombre'] == "Elena Mar"

def test_buscar_id_inexistente_lanza_error():
    reset()
    with pytest.raises(ValueError, match="No existe"):
        service.search_record(id_usuario="xxxxxxxx")

def test_buscar_sin_criterio_lanza_error():
    reset()
    with pytest.raises(ValueError, match="ID o un email"):
        service.search_record()



def test_actualizar_nombre():
    reset()
    u = service.new_register(nombre="Juan Ruiz", email="juan@mail.com", estado="activo")
    actualizado = service.update_record(u['id'], nombre="Juan Carlos Ruiz")
    assert actualizado['nombre'] == "Juan Carlos Ruiz"

def test_actualizar_estado():
    reset()
    u = service.new_register(nombre="Juan Ruiz", email="juan@mail.com", estado="activo")
    actualizado = service.update_record(u['id'], estado="inactivo")
    assert actualizado['estado'] == "inactivo"

def test_actualizar_id_inexistente_lanza_error():
    reset()
    with pytest.raises(ValueError, match="No existe"):
        service.update_record("xxxxxxxx", nombre="Nuevo")

def test_actualizar_sin_campos_lanza_error():
    reset()
    u = service.new_register(nombre="Juan Ruiz", email="juan@mail.com", estado="activo")
    with pytest.raises(ValueError, match="al menos un campo"):
        service.update_record(u['id'])

def test_actualizar_campo_no_permitido_lanza_error():
    reset()
    u = service.new_register(nombre="Juan Ruiz", email="juan@mail.com", estado="activo")
    with pytest.raises(ValueError, match="no es editable"):
        service.update_record(u['id'], telefono="123456")



def test_eliminar_usuario_existente():
    reset()
    u = service.new_register(nombre="Rosa Díaz", email="rosa@mail.com", estado="activo")
    service.delete_record(u['id'])
    assert len(service.list_records()) == 0

def test_eliminar_libera_email_para_reusar():
    reset()
    u = service.new_register(nombre="Rosa Díaz", email="rosa@mail.com", estado="activo")
    service.delete_record(u['id'])
    u2 = service.new_register(nombre="Rosa Nueva", email="rosa@mail.com", estado="activo")
    assert u2['email'] == "rosa@mail.com"

def test_eliminar_id_inexistente_lanza_error():
    reset()
    with pytest.raises(ValueError, match="No existe"):
        service.delete_record("xxxxxxxx")