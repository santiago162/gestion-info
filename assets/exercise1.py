entrada = input("Ingrese enteros separados por comas: ")
tokens = entrada.split(",")

numeros = []

for token in tokens:
    try:
        numero = int(token.strip())
        numeros.append(numero)
    except ValueError:
        print("Se ignoro el valor:", token.strip(), "porque no es un entero")

if numeros:
    promedio = sum(numeros) / len(numeros)
    print("Promedio:", promedio)
else:
    print("No se ingresaron numeros validos")