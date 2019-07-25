#Ejercicio 22
#Escribe un programa que te permita jugar a una versión simplificada del juego Master Mind. El juego consistirá en adivinar una cadena de números distintos. 
#Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la cadena de números. 
#En cada intento, el programa informará de cuántos números han sido acertados (el programa considerará que se ha acertado un número si coincide el valor y la posición).

#Dime la longitud de la cadena: 4
#Intenta adivinar la cadena: 1234
#Con 1234 has adivinado 1 valores. Intenta adivinar la cadena: 1243
#Con 1243 has adivinado 0 valores. Intenta adivinar la cadena: 1432
#Con 1432 has adivinado 2 valores. Intenta adivinar la cadena: 2431
#Con 2431 has adivinado 4 valores. Felicidades

import random
import time

def intro():
    print("""
                            Mastermind!

    Bienvenido al juego de Mastermind, un juego que pondra a prueba tu
logica y capacidades de raciocinio!

El objetivo es simple: descifrar el código de numeros que generara 
Python. Para hacerlo necesitarás ir descartando posibilidades según las 
pistas que te proporcionará nuestro oponente Python.

El juego constara de 3 partidas, tu seras el decodificador, y tendras
10 oportunidades para descifrar el codigo secreto. Entre mas rapido
descifres el codigo, mayor sera la cantidad de puntos que ganaras!
Cada error sera un punto para Python!

El jugador que acumule mas puntos en las 3 partidas, sera el vencedor!


Preparado?
""")
    print("Cargando...")
    time.sleep(5)

def generador_numeros(codigo_secreto, dificultad):
    for numero in range(dificultad):
        codigo_secreto.append(random.randint(0,9))

    return codigo_secreto

def codigo_a_lista(codigo_descodificador):
    lista = list()

    for valor in codigo_descodificador:
        lista.append(int(valor))

    return lista

def valida_codigo(codigo_secreto, codigo_descodificador):
    copia_codigo_secreto = codigo_secreto.copy()
    copia_codigo_descodificador = codigo_descodificador.copy()
    acierto_rojo = 0
    acierto_blanco = 0
    posicion_usuario = 0
    posicion_oponente = 0

    print(codigo_descodificador)

    #Calcula solo puntos rojos (Toma como parametro tanto el valor como donde esta ubicado)
    for valor_usuario in copia_codigo_descodificador:
        for valor_oponente in copia_codigo_secreto:
            if valor_usuario == valor_oponente and posicion_usuario == posicion_oponente:
                acierto_rojo += 1
                copia_codigo_secreto[posicion_oponente] = '+'
                copia_codigo_descodificador[posicion_usuario] = '-'
                break

            posicion_oponente += 1
        
        posicion_usuario += 1
        posicion_oponente = 0

    #Calcula solo puntos blancos (Busca sin importar la posicion. Los puntos rojos ya fueron removidos)
    for valor_usuario in copia_codigo_descodificador:
        for valor_oponente in copia_codigo_secreto:
            if valor_usuario == valor_oponente:
                acierto_blanco += 1
                break

    return acierto_rojo, acierto_blanco


def fin_partida(num_partida, puntos_codificador, puntos_descodificador):
    print(f"\nFin de la partida {num_partida}")
    print("\nPuntuacion al momento:")
    print(f"Codificador: {puntos_codificador}")
    print(f"Descodificador: {puntos_descodificador}\n\n")
    time.sleep(5)


codigo_secreto = list()
puntos_codificador = 0
puntos_descodificador = 0
filas = 1
num_partida = 1

intro()
print("Selecciona la dificultad del juego:")
print("3. Facil (Codigo 3 numeros)")
print("4. Normal (Codigo 4 numeros)")
print("6. Experto (Codigo 6 numeros)")
print("9. Mastermind (Codigo 9 numeros)")

while True:
    try:
        dificultad = int(input("> "))
        assert dificultad == 3 or dificultad == 4 or dificultad == 6 or dificultad == 9
        break
    except (ValueError, AssertionError):
        print("Escribe una opcion valida!")

while num_partida <= 3:
    print(f"\nIniciando partida {num_partida}...")
    time.sleep(5)
    print("El codificador esta creando el codigo...")
    codigo_secreto = generador_numeros(codigo_secreto, dificultad)
    time.sleep(5)
    print("Codigo creado!")
    print("\nComencemos!")
    print(codigo_secreto)

    while filas < 11:

        while True:
            try:
                codigo_descodificador = input(f"Turno {filas}. Adivina el codigo de tu oponente > ")
                assert len(codigo_descodificador) == dificultad and codigo_descodificador.isdigit()
                break
            except AssertionError:
                print("El codigo ingresado es invalido. Debe ser numerico y del tamaño correcto!\n")
        
        print("Validando codigo...")
        acierto_rojo, acierto_blanco = valida_codigo(codigo_secreto, codigo_a_lista(codigo_descodificador))
        time.sleep(5)

        if acierto_rojo == dificultad:
            print("\nHaz descifrado el codigo!!")
            puntos_descodificador += 11 - filas
            break
        else:
            print(f"\nTienes {acierto_rojo} numeros en la posicion correcta, {acierto_blanco} en posicion incorrecta.\n")

        filas += 1
        puntos_codificador += 1
        

    fin_partida(num_partida, puntos_codificador, puntos_descodificador)
    num_partida += 1
    filas = 1
    codigo_secreto.clear()

    

print("Fin del juego!")
print("Resultados finales: ")
print(f"Codificador: {puntos_codificador}")
print(f"Descodificador: {puntos_descodificador}")

if puntos_descodificador > puntos_codificador :
    print("\nFELICIDADES ERES EL GANADOR!!\n")
else:
    print("\nPython the ha derrotado...")

print("\nEsperamos verte de nuevo pronto!")