class OperacionInvalidaError(ValueError):
    pass

class DivisionPorCeroError(ZeroDivisionError):
    pass


def calc(a, b, op):
    if op == "suma":
        return a + b
    elif op == "resta":
        return a - b
    elif op == "multi":
        return a * b
    elif op == "divi":
        if b == 0:
            raise DivisionPorCeroError("No se puede dividir entre cero")
        return a / b
    else:
        raise OperacionInvalidaError("Operacion no reconocida: " + op)


try:
    op = input("Ingrese operacion (suma, resta, multi, divi): ").strip()
    a  = float(input("Ingrese primer numero: "))
    b  = float(input("Ingrese segundo numero: "))

    resultado = calc(a, b, op)
    print("Resultado:", resultado)

except OperacionInvalidaError as e:
    print("Operacion invalida:", e)
except DivisionPorCeroError as e:
    print("Division por cero:", e)
except ValueError:
    print("Error: ingrese numeros validos")