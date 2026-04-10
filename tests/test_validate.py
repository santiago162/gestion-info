import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from validate import (
    validar_nombre,
    validar_email,
    validar_estado,
    validar_usuario,
)


def test_nombre_valido():
    assert validar_nombre("Ana Torres") == "Ana Torres"

def test_nombre_vacio_lanza_error():
    with pytest.raises(ValueError, match="vacío"):
        validar_nombre("")

def test_nombre_muy_corto_lanza_error():
    with pytest.raises(ValueError, match="2 caracteres"):
        validar_nombre("A")

def test_nombre_con_numeros_lanza_error():
    with pytest.raises(ValueError, match="letras"):
        validar_nombre("Ana123")

def test_nombre_con_espacios_se_limpia():
    assert validar_nombre("  Carlos  ") == "Carlos"

def test_email_valido():
    assert validar_email("ana@mail.com") == "ana@mail.com"

def test_email_se_convierte_a_minusculas():
    assert validar_email("ANA@MAIL.COM") == "ana@mail.com"

def test_email_sin_arroba_lanza_error():
    with pytest.raises(ValueError, match="formato"):
        validar_email("anomail.com")

def test_email_sin_dominio_lanza_error():
    with pytest.raises(ValueError, match="formato"):
        validar_email("ana@")

def test_email_vacio_lanza_error():
    with pytest.raises(ValueError, match="formato"):
        validar_email("")


def test_estado_activo_valido():
    assert validar_estado("activo") == "activo"

def test_estado_inactivo_valido():
    assert validar_estado("inactivo") == "inactivo"

def test_estado_mayusculas_se_normaliza():
    assert validar_estado("ACTIVO") == "activo"

def test_estado_invalido_lanza_error():
    with pytest.raises(ValueError, match="activo.*inactivo"):
        validar_estado("suspendido")

def test_estado_vacio_lanza_error():
    with pytest.raises(ValueError):
        validar_estado("")


def test_usuario_completo_valido():
    resultado = validar_usuario(
        nombre="Laura Pérez",
        email="laura@mail.com",
        estado="activo"
    )
    assert resultado['nombre'] == "Laura Pérez"
    assert resultado['email']  == "laura@mail.com"
    assert resultado['estado'] == "activo"

def test_usuario_falta_campo_lanza_error():
    with pytest.raises(ValueError, match="Falta el campo"):
        validar_usuario(nombre="Laura", email="laura@mail.com")

def test_usuario_email_invalido_lanza_error():
    with pytest.raises(ValueError, match="formato"):
        validar_usuario(nombre="Laura", email="no-es-email", estado="activo")