nombre = input("Ingrese el nombre del archivo: ")
archivo = None

try:
    archivo = open(nombre, "r", encoding="utf-8")
except FileNotFoundError:
    print("Error: el archivo no fue encontrado")
except OSError as e:
    print("Error al abrir el archivo:", e)
else:
    lineas = archivo.readlines()
    print("Archivo abierto correctamente. Lineas encontradas:", len(lineas))
finally:
    if archivo:
        archivo.close()
        print("Archivo cerrado")
    print("Proceso finalizado")