# 🗂️ Sistema de Gestión de Usuarios

Sistema de consola desarrollado en Python que permite gestionar usuarios de forma local mediante un menú interactivo. Permite crear, consultar, actualizar y eliminar registros, con persistencia real en archivo JSON y generación de datos de prueba con Faker. Es útil para aprender buenas prácticas de modularización, manejo de archivos y estructuras de datos en Python.

---

## 📂 Estructura del proyecto

```
gestion-info/
├─ README.md                  # Documentación del proyecto
├─ requirements.txt           # Dependencias externas
├─ .gitignore                 # Archivos ignorados por Git
├─ data/
│  └─ records.json            # Base de datos local en formato JSON
├─ tests/
│  ├─ test_validate.py        # Pruebas de validaciones
│  └─ test_service.py         # Pruebas de lógica de negocio
└─ src/
   ├─ main.py                 # Punto de entrada del programa
   ├─ menu.py                 # Interfaz de consola (UI) con colorama
   ├─ service.py              # Lógica de negocio (CRUD)
   ├─ file.py                 # Persistencia: leer y guardar en archivo
   ├─ validate.py             # Validaciones y control de unicidad
   └─ integration.py          # Generación de datos falsos con Faker
```

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/santiago162/gestion-info.git
cd gestion-info
```

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```
colorama
faker
pytest
```

> **Nota:** Si tienes problemas de permisos de red en Windows (WinError 10013), ejecuta PowerShell como administrador o usa:
> ```bash
> pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
> ```

---

## 🚀 Uso

### Ejecutar el programa

```bash
python src/main.py
```

Al iniciar verás el menú principal:

```
=============================================
   SISTEMA DE GESTIÓN DE USUARIOS
=============================================
✅ Sistema listo

╔════════════════════════════════════╗
║      GESTIÓN DE USUARIOS           ║
╠════════════════════════════════════╣
║  1. Crear usuario                  ║
║  2. Listar usuarios                ║
║  3. Buscar usuario                 ║
║  4. Actualizar usuario             ║
║  5. Eliminar usuario               ║
║  6. Generar usuarios falsos        ║
║  0. Salir                          ║
╚════════════════════════════════════╝
```

### Opciones disponibles

| Opción | Descripción |
|--------|-------------|
| 1 | Crea un usuario ingresando nombre, email y estado |
| 2 | Lista todos los usuarios (con filtro y ordenamiento) |
| 3 | Busca un usuario por ID o por email |
| 4 | Actualiza nombre, email o estado de un usuario |
| 5 | Elimina un usuario con confirmación previa |
| 6 | Genera usuarios falsos automáticamente con Faker |
| 0 | Sale del programa |

### Campos de un usuario

| Campo  | Descripción                        | Ejemplo              |
|--------|------------------------------------|----------------------|
| id     | Generado automáticamente (8 chars) | `a3f9c21b`           |
| nombre | Solo letras y espacios             | `Ana Torres`         |
| email  | Formato válido, único en el sistema| `ana@mail.com`       |
| estado | Solo `activo` o `inactivo`         | `activo`             |

### Ejecutar las pruebas

```bash
pytest tests/ -v
```

Salida esperada:

```
tests/test_validate.py::test_nombre_valido           PASSED
tests/test_validate.py::test_email_valido            PASSED
tests/test_service.py::test_crear_usuario_retorna_dict  PASSED
...
======= 30 passed in 0.45s =======
```

---

## 👤 Créditos y autores

| Nombre | Rol |
|--------|-----|
| Santiago | Desarrollador principal |

Proyecto desarrollado como parte del taller de **Manejo de archivos y estructuras de datos avanzadas en Python** del SENA.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.

Esto significa que puedes usar, copiar, modificar y distribuir el código libremente, siempre que incluyas el aviso de copyright original.

```
MIT License

Copyright (c) 2026 Santiago

```