# Script de Python que crea una lista de saludos y una lista de nombres.
# Luego, elige un elemento aleatorio de cada lista y los imprime en un saludo personalizado.

import random


def generar_saludo(saludos, nombres):
    """Genera un saludo personalizado aleatorio."""
    # Esta función ahora asume que la lista 'nombres' no está vacía.
    # La responsabilidad de comprobarlo está en quien la llama (main).
    saludo_aleatorio = random.choice(saludos)
    nombre_aleatorio = random.choice(nombres)
    return f"{saludo_aleatorio} {nombre_aleatorio}!"

def main():
    """Función principal del programa."""
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
    # --- CAMBIO 1: La lista de nombres empieza vacía, como sugeriste ---
    nombres = []
    
    print("=== Generador de Saludos Personalizados ===")
    
    # --- El bloque para añadir nombres que ya tenías ---
    print("\n--- Añadir Nombres Personalizados ---")
    print("Introduce un nombre y pulsa Enter. Pulsa Enter sin escribir nada para terminar.")
    while True:
        nombre_introducido = input("Añadir nombre: ")
        if not nombre_introducido:
            print("¡Lista de nombres finalizada!")
            break
            
        nombre_limpio = nombre_introducido.strip()
        if nombre_limpio:
            nombres.append(nombre_limpio)
            print(f"-> ¡'{nombre_limpio}' ha sido añadido a la lista!")
        else:
            print("-> No se pueden añadir nombres vacíos.")
            
    print() # Un espacio para que se vea más limpio

    # --- CAMBIO 2: La comprobación de seguridad ---
    # Si después de todo, la lista de nombres está vacía, no podemos continuar.
    if not nombres:
        print("No se ha introducido ningún nombre. No se pueden generar saludos.")
        print("¡Hasta luego! 👋")
        return # Usamos 'return' para salir de la función main y terminar el programa.

    # --- El resto del programa solo se ejecuta si hay nombres en la lista ---
    
    # Generar y mostrar varios saludos
    print("¡Genial! Aquí tienes tus saludos personalizados:")
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