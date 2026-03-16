from arcP1 import arcP1

# Crear instancia
archivo = arcP1("archivo_demo.txt")
archivo.crear()

# Agregar contenido inicial
archivo.agregar("mundo juan")
archivo.agregar("hola Hola")
archivo.agregar("quien mundo")

# Mostrar contenido
print("Contenido del archivo:")
try:
    with open("archivo_demo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except Exception as e:
    print("Error al leer archivo:", e)

# Mostrar frecuencia de palabras
print("\nFrecuencia de palabras:")
for palabra, cant in archivo.frecuencia():
    print(f"{palabra}: {cant}")







