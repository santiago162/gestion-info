import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from colorama import Fore, Style, init
from service import inicializar
from menu import ejecutar_menu

init(autoreset=True)


def main():
    print(Fore.YELLOW + Style.BRIGHT + "=" * 45)
    print(Fore.YELLOW + Style.BRIGHT + "   SISTEMA DE GESTIÓN DE USUARIOS")
    print(Fore.YELLOW + Style.BRIGHT + "=" * 45)
    print(Fore.GREEN  + "✅ Sistema listo\n")

    inicializar()
    ejecutar_menu()


if __name__ == "__main__":
    main()