import sys

# Para ejecutar el programa con argumentos, debe usarse el comando ctrl + ñ, añadir el caracter '&' + dirección del ejecutable de python + la dirección del archivo .py
#  y poner los argumentos en la misma línea separados por espacios
# Ejemplo:
# PS C:\Users\janus>      ## Esta es la línea predeterminada al presionar crtl + ñ
# & C:/Users/janus/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/janus/Downloads/Battleship2/src/Vista/a.py  1 2 3 ## Va en la misma linea
# En el ejemplo, el argumento ingresado es '1 2 3'

# Mostrar versión y plataforma
sys.stdout.write(f"Versión de Python: {sys.version}\n")
sys.stdout.write(f"Sistema operativo: {sys.platform}\n\n")

# Leer argumentos de línea de comandos
sys.stdout.write("Argumentos recibidos:\n")
for i, arg in enumerate(sys.argv):
    sys.stdout.write(f"  argv[{i}] = {arg}\n")

# Si no se pasan argumentos (aparte del script), terminar con error
if len(sys.argv) < 2:
    sys.stderr.write("No se pasaron argumentos. Finaliza con error.\n")
    sys.exit(1)  # Código de salida 1 = error

# Medir tamaño de un objeto
objeto = sys.argv[1]
sys.stdout.write(f"\nTamaño en memoria de '{objeto}': {sys.getsizeof(objeto)} bytes\n")

# Mostrar rutas de búsqueda de módulos
sys.stdout.write("\nRutas donde Python busca módulos:\n")
for ruta in sys.path:
    sys.stdout.write(f"  {ruta}\n")
