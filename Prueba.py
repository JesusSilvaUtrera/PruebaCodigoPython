import os

path = "C:/Users/jsilv/Documents/PruebaCodigoPython"
if os.path.isdir(path):
    print(f"Directorio reconocido: {path}")
else:
    print("Directorio no reconocido")