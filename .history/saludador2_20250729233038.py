# Script de Python que crea una lista de saludos y una lista de nombres.
# Luego, elige un elemento aleatorio de cada lista y los imprime en un saludo personalizado.

import random



# Lista de nombres


def generar_saludo():
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
    """Genera un saludo personalizado aleatorio."""
    saludo_aleatorio = random.choice(saludos)
    nombre_aleatorio = random.choice(nombres)
    return f"{saludo_aleatorio} {nombre_aleatorio}!"

def main():
    """Función principal del programa."""
    print("=== Generador de Saludos Personalizados ===")
    print()
    
    # Generar y mostrar varios saludos
    for i in range(5):
        saludo = generar_saludo()
        print(f"Saludo {i + 1}: {saludo}")
    
    print()
    print("¿Quieres generar más saludos? (s/n)")
    
    while True:
        respuesta = input().lower().strip()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            print()
            print("¡Aquí tienes más saludos!")
            for i in range(3):
                saludo = generar_saludo()
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
