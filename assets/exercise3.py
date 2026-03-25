while True:
    print("\n--- MENU ---")
    print("1. Dividir dos numeros")
    print("2. Abrir archivo y mostrar primera linea")
    print("3. Salir")

    opcion = input("Opcion: ").strip()

    try:
        if opcion == "1":
            a = float(input("Dividendo: "))
            b = float(input("Divisor: "))
            print("Resultado:", a / b)

        elif opcion == "2":
            nombre = input("Nombre del archivo: ")
            with open(nombre, "r", encoding="utf-8") as f:
                print("Primera linea:", f.readline().strip())

        elif opcion == "3":
            print("Hasta luego")
            break

        else:
            print("Opcion invalida")

    except ValueError:
        print("Error: ingrese un numero valido")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
    except FileNotFoundError:
        print("Error: archivo no encontrado")
    except Exception as e:
        print("Error inesperado:", e)