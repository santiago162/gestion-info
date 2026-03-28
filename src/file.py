import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')


def load_data() -> list[dict]:
    """
    Carga los registros desde el archivo JSON.
    - Si no existe el archivo, retorna lista vacía.
    - Si el archivo está dañado, muestra mensaje y retorna lista vacía.
    """
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            if not isinstance(datos, list):
                raise ValueError("El archivo no contiene una lista válida.")
            print(f"📂 {len(datos)} registro(s) cargado(s) desde archivo.")
            return datos

    except FileNotFoundError:
        print("📂 Archivo no encontrado. Iniciando con lista vacía.")
        return []

    except json.JSONDecodeError:
        print("⚠️  El archivo está dañado o mal formado. Iniciando con lista vacía.")
        return []

    except ValueError as e:
        print(f"⚠️  Error de formato: {e}. Iniciando con lista vacía.")
        return []

    except Exception as e:
        print(f"⚠️  Error inesperado al leer archivo: {e}. Iniciando con lista vacía.")
        return []


def save_data(data: list[dict]) -> bool:
    """
    Guarda la lista de registros en el archivo JSON.
    - Crea la carpeta data/ si no existe.
    - Retorna True si guardó bien, False si hubo error.
    """
    try:
        carpeta = os.path.dirname(DATA_PATH)
        os.makedirs(carpeta, exist_ok=True)

        with open(DATA_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"💾 {len(data)} registro(s) guardado(s) correctamente.")
        return True

    except PermissionError:
        print("⚠️  Sin permisos para escribir en el archivo.")
        return False

    except OSError as e:
        print(f"⚠️  Error del sistema al guardar: {e}")
        return False

    except Exception as e:
        print(f"⚠️  Error inesperado al guardar: {e}")
        return False