from faker import Faker
from service import new_register

fake = Faker('es_CO')


def generar_usuario_falso() -> dict:
    """
    Genera un usuario falso con Faker.
    Usa **kwargs al llamar new_register.
    """
    datos = {
        'nombre': fake.name(),
        'email':  fake.unique.email(),
        'estado': fake.random_element(elements=('activo', 'inactivo')),
    }
    return new_register(**datos)


def generar_usuarios_falsos(*args, cantidad: int = 10) -> tuple:
    """
    Genera múltiples usuarios falsos.
    - *args: etiquetas opcionales de identificación (ej: 'demo', 'prueba')
    - cantidad: cuántos usuarios generar (por defecto 10)
    Retorna tupla (lista de creados, número de errores).
    """
    if args:
        print(f"   Etiqueta de generación: {', '.join(str(a) for a in args)}")

    creados = []
    errores = 0

    for _ in range(cantidad):
        try:
            usuario = generar_usuario_falso()
            creados.append(usuario)
        except ValueError:
            errores += 1

    return creados, errores