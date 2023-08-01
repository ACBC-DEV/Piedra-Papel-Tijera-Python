

import random
print('-.'*50)
opcions = ["piedra", "papel", "tijera"]

# winUsar = 0
# winPc = 0
wins = {
    'Usar': 0,
    'Pc': 0
}


def obtener_jugada_usuario():
    while True:
        jugada = input("Elige piedra, papel o tijera: ").lower()
        if jugada in opcions:
            return jugada
        else:
            print("¡Jugada inválida! Inténtalo nuevamente.")


def obtener_jugada_computadora():
    return random.choice(opcions)


def determinar_ganador(jugada_usuario, jugada_computadora):
    if jugada_usuario == jugada_computadora:
        return "Empate"
    elif (jugada_usuario == "piedra" and jugada_computadora == "tijera") or \
        (jugada_usuario == "papel" and jugada_computadora == "piedra") or \
            (jugada_usuario == "tijera" and jugada_computadora == "papel"):
        wins["Usar"] += 1
        return "¡Ganaste!"
    else:
        wins["Pc"] += 1
        return "Perdiste :("


def jugar_piedra_papel_tijera():
    print("Bienvenido a Piedra, Papel o Tijera")

    while wins["Pc"] < 3 and wins["Usar"] < 3:
        jugada_usuario = obtener_jugada_usuario()
        jugada_computadora = obtener_jugada_computadora()

        print(f"Tú elegiste: {jugada_usuario}")
        print(f"La computadora eligió: {jugada_computadora}")

        resultado = determinar_ganador(jugada_usuario, jugada_computadora)
        print(
            f'la partida van computador: {wins["Pc"]} vs usuario: {wins["Usar"]}')
        print(resultado)
        if wins["Pc"] == 3 or wins["Usar"] == 3:
            jugar_nuevamente = input(
                "¿Quieres jugar de nuevo? (sí/no): ").lower()
            if jugar_nuevamente == "si":
                wins["Pc"] = 0
                wins["Usar"] = 0


if __name__ == "__main__":
    jugar_piedra_papel_tijera()
