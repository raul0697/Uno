import random

colores = ["Rojo", "Amarillo", "Azul", "Verde"]
numeros = [str(i) for i in range(0,10)] + ["Salto","Reversa","Más dos"]

def crear_baraja():
    baraja = []
    for color in colores:
        for numero in numeros:
            baraja.append(f"{numero} de {color}")
    random.shuffle(baraja)
    return baraja

def repartir_cartas(baraja, num_jugadores):
    manos = {f"Jugador {i + 1}": [] for i in range(num_jugadores)}
    for _ in range(7):  # Cada jugador recibe 7 cartas
        for jugador in manos:
            manos[jugador].append(baraja.pop())
    return manos, baraja

def mostrar_mano(jugador, mano):
    print(f"{jugador}: {', '.join(mano)}")


def jugar_uno(num_jugadores):
    baraja = crear_baraja()
    manos, baraja = repartir_cartas(baraja, num_jugadores)

    turno = 0
    while True:
        jugador = f"Jugador {turno + 1}"
        mostrar_mano(jugador, manos[jugador])

        carta_jugada = baraja.pop() if baraja else None
        if carta_jugada:
            print(f"Carta en juego: {carta_jugada}")


        carta_a_jugar = input(f"{jugador}, elige una carta para jugar o escribe 'robar': ")

        if carta_a_jugar.lower() == 'robar':
            if baraja:
                manos[jugador].append(baraja.pop())
                print(f"{jugador} robó una carta.")
            else:
                print("No quedan cartas en la baraja.")
        elif carta_a_jugar in manos[jugador]:
            manos[jugador].remove(carta_a_jugar)
            print(f"{jugador} jugó: {carta_a_jugar}")
        else:
            print("No tienes esa carta. Pierdes el turno.")


        if not manos[jugador]:
            print(f"{jugador} ha ganado!")
            break

        turno = (turno + 1) % num_jugadores

if __name__ == "__main__":
    num_jugadores = int(input("¿Cuántos jugadores (2-4)? "))
    jugar_uno(num_jugadores)
