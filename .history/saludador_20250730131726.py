# Script de Python que crea una lista de saludos y una lista de nombres.
# Luego, elige un elemento aleatorio de cada lista y los imprime en un saludo personalizado.

import random


def generar_saludo(saludos, nombres):
    """Genera un saludo personalizado aleatorio."""
    saludo_aleatorio = random.choice(saludos)
    nombre_aleatorio = random.choice(nombres)
    return f"{saludo_aleatorio} {nombre_aleatorio}!"

def main():
    # Lista de saludos
    saludos = [
        "¡Hola",
        "¡Buenos días",
        "¡Buenas tardes",
        "¡Saludos",
        "¡Qué tal",
        "¡Hey",
        "¡Bienvenido"
    ]
    # Lista de nombres
    nombres = [
        "Ana",
        "Carlos",
        "María",
        "José",
        "Laura",
        "Pedro",
        "Carmen",
        "Miguel",
        "Sofía",
        "Diego"
    ]
    """Función principal del programa."""
    print("=== Generador de Saludos Personalizados ===")
    print()
    print("\n ---Añadir Nombres Personalizados ---")
    print("Introduce un nombre y pulsa Enter. Pulsa Enter sin escribir nada para terminar")
    while True:
        # Pedimos un nombre al usuario en cada vuelta del bucle
        nombre_introducido = input("Añadir nombre: ")
        # Condición de salida: si el usuario no escribe nada y pulsa "Enter"
        if not nombre_introducido:
            print("¡Lista de nombres finalizada")
            break # Rompe el bucle while
        # Limpiamos la entrada (quita espacios al inicio/final) y la añadimos a la lista
        nombre_limpio = nombre_introducido.strip()
        
        # Nos aseguramos de no añadir nombres vacíos si el usuario solo introduce espacios
        if nombre_limpio:
            nombres.append()
    # Generar y mostrar varios saludos
    for i in range(5):
        saludo = generar_saludo(saludos, nombres)
        print(f"Saludo {i + 1}: {saludo}")
    
    print()
    print("¿Quieres generar más saludos? (s/n)")
    
    while True:
        respuesta = input().lower().strip()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            print()
            print("¡Aquí tienes más saludos!")
            for i in range(3):
                saludo = generar_saludo(saludos, nombres)
                print(f"• {saludo}")
            print()
            print("¿Más saludos? (s/n)")
        elif respuesta in ['n', 'no']:
            print("¡Hasta luego! 👋")
            break
        else:
            print("Por favor, responde 's' para sí o 'n' para no:")

if __name__ == "__main__":
    main()
