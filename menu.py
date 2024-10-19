import subprocess
import os

# Funciones para mostrar diferentes proyectos
def mostrar_algoritmos():
    print("Proyectos de Algoritmos:")
    print("1. Ordenamiento de listas")
    print("2. Búsqueda binaria")

def mostrar_algebra_lineal():
    print("Proyectos de Álgebra Lineal:")
    print("1. Resolución de sistemas de ecuaciones")
    print("2. Transformaciones lineales")

# Opción 1: Ejecutar el script `algebralineal.py`
def ejecutar_algebra_lineal():
    print("Abriendo el proyecto de Álgebra Lineal...")
    subprocess.run(["python", "algebralineal.py"])  # Asegúrate de que el archivo esté en la misma carpeta

# Opción 2: Ejecutar el script `matematica_discreta.py`
def ejecutar_matematica_discreta():
    print("Abriendo el proyecto de Matemática Discreta...")
    subprocess.run(["python", "matematica_discreta.py"])  # Asegúrate de que el archivo esté en la misma carpeta

# Menú principal
def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Algoritmos")
        print("2. Ejecutar matematica_discreta.py")  # Ejecutar `matematica_discreta.py`
        print("3. Ejecutar algebralineal.py")  # Ejecutar `algebralineal.py`
        print("4. Salir")
        
        eleccion = input("Elige un proyecto (1-3 y 4 para salir): ")
        
        if eleccion == '1':
            mostrar_algoritmos()
        elif eleccion == '2':
            ejecutar_matematica_discreta()  # Ejecuta `matematica_discreta.py`
        elif eleccion == '3':
            ejecutar_algebra_lineal()  # Ejecuta `algebralineal.py`
        elif eleccion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    while True:
        menu_principal()
        reiniciar = input("¿Quieres volver a entrar al programa? (s/n): ").lower()
        if reiniciar != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
