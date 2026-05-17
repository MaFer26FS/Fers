import os
import random
import time

# --- CONFIGURACIÓN DE COLORES ANSI ---
# Nota: Las terminales móviles varían, usamos las mejores aproximaciones de la paleta solicitada.
PURPLE = "\033[0;35m"      # Morado
FUCHSIA = "\033[1;35m"     # Fucsia / Rosa brillante
GREEN = "\033[0;32m"       # Verde
LIGHT_GREEN = "\033[1;32m" # Verde brillante
RESET = "\033[0m"          # Resetear color

def limpiar_pantalla():
    """Limpia la pantalla de la consola según el sistema."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner_principal():
    """Muestra el banner de presentación con los colores requeridos."""
    limpiar_pantalla()
    print(GREEN + "==================================================" + RESET)
    print(PURPLE + "                 FRIENDS SCHOOL" + RESET)
    print(FUCHSIA + "                     MAFER" + RESET)
    print(GREEN + "==================================================" + RESET)
    print("")

def banner_ruleta():
    """Muestra el banner específico para la sección de la ruleta."""
    limpiar_pantalla()
    print(FUCHSIA + "==================================================" + RESET)
    print(FUCHSIA + "                      MAFER" + RESET)
    print(FUCHSIA + "==================================================" + RESET)
    print(GREEN + "               [ RULETA DE SORTEOS ]" + RESET)
    print("")

def simular_ruleta(participantes):
    """Simula el giro de una ruleta visualmente en la terminal."""
    banner_ruleta()
    print(GREEN + "¡Girando la ruleta!" + RESET)
    
    # Simulación de velocidad decreciente (efecto de frenado)
    retardo = 0.05
    for i in range(20):
        nombre_temporal = random.choice(participantes)
        # \r permite sobrescribir la misma línea en la terminal
        print(f"\r»» {FUCHSIA}{nombre_temporal}{RESET} ««", end="", flush=True)
        time.sleep(retardo)
        retardo += 0.02
    
    ganador = random.choice(participantes)
    print("\n")
    print(GREEN + "==================================================" + RESET)
    print(f" 🎉 ¡El ganador es: {FUCHSIA}{ganador}{RESET}! 🎉")
    print(GREEN + "==================================================" + RESET)
    print("")

def menu_ruleta():
    """Gestiona la lógica del sorteo y la ruleta."""
    participantes = []
    
    while True:
        banner_ruleta()
        if participantes:
            print(PURPLE + "Participantes actuales:" + RESET)
            print(", ".join(participantes))
            print("-" * 50)
        
        print(GREEN + "1." + RESET + " Añadir participante")
        print(GREEN + "2." + RESET + " ¡Girar Ruleta!")
        print(GREEN + "3." + RESET + " Limpiar lista")
        print(GREEN + "4." + RESET + " Volver al menú principal")
        print("")
        
        opcion = input(PURPLE + "Selecciona una opción: " + RESET).strip()
        
        if opcion == "1":
            nombre = input(PURPLE + "Ingresa el nombre del participante: " + RESET).strip()
            if nombre:
                participantes.append(nombre)
        elif opcion == "2":
            if len(participantes) < 2:
                print(FUCHSIA + "\n¡Necesitas al menos 2 participantes para sortear!" + RESET)
                time.sleep(2)
            else:
                simular_ruleta(participantes)
                input(PURPLE + "Presiona Enter para continuar..." + RESET)
        elif opcion == "3":
            participantes = []
            print(FUCHSIA + "\nLista vaciada." + RESET)
            time.sleep(1)
        elif opcion == "4":
            break
        else:
            print(FUCHSIA + "\nOpción no válida." + RESET)
            time.sleep(1)

def main():
    """Bucle principal de la aplicación."""
    while True:
        mostrar_banner_principal()
        print(LIGHT_GREEN + "1." + RESET + " Entrar a la Ruleta de Mafer")
        print(LIGHT_GREEN + "2." + RESET + " Salir")
        print("")
        
        opcion = input(PURPLE + "Selecciona una opción: " + RESET).strip()
        
        if opcion == "1":
            menu_ruleta()
        elif opcion == "2":
            limpiar_pantalla()
            print(FUCHSIA + "¡Gracias por usar el script de MAFER! Adiós." + RESET)
            break
        else:
            print(FUCHSIA + "\nOpción no válida." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main()
