from exercise5 import is_valid_password


def test_password_valida():
    assert is_valid_password("Abcdefg1") == True

def test_sin_mayuscula():
    assert is_valid_password("abcdefg1") == False

def test_sin_digito():
    assert is_valid_password("ABCDEFGH") == False

def test_muy_corta():
    assert is_valid_password("Ab1") == False

def test_con_espacio():
    assert is_valid_password("Abcde f1") == False

def test_exactamente_8_caracteres():
    assert is_valid_password("Abcdef1!") == True