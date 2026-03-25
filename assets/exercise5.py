# ============================================================
# EJERCICIO 5: Validador de contraseñas
# ============================================================

def has_minimum_length(password: str) -> bool:
    return len(password) >= 8

def has_digit(password: str) -> bool:
    for char in password:
        if char.isdigit():
            return True
    return False

def has_uppercase(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def has_no_spaces(password: str) -> bool:
    return " " not in password

def is_valid_password(password: str) -> bool:
    """
    Valida que una contraseña cumpla las siguientes reglas:
    - Minimo 8 caracteres
    - Al menos un digito
    - Al menos una mayuscula
    - Sin espacios
    """
    if not has_minimum_length(password):
        return False
    if not has_digit(password):
        return False
    if not has_uppercase(password):
        return False
    if not has_no_spaces(password):
        return False
    return True