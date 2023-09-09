print("****JUEGO PIEDRA , PAPEL O TIJERA VS CPU*****")
print()
import random

while True:
    cpu = random.randrange(0,3)
    maquina = ""
    print("1. papel ")
    print("2. piedra ")
    print("3. tijera ")

    usuario = int(input("Elige tu opción: "))

    if usuario == 1:
        usuario1 = "papel"
    elif usuario == 2:
        usuario1 = "piedra"
    elif usuario == 3:
        usuario1 = "tijera"
    
    print("Elejiste: ",usuario1)

    if cpu == 0:
        maquina = "papel"
    elif cpu == 1:
        maquina = "piedra"
    elif cpu == 2:
        maquina = "tijera"
    print("La maquina eligio: ",maquina)
    print("**..**")

    if maquina == "papel" and usuario1 == "tijera":
        print("Gana usuario1 ya que tijeras corta papel")
    elif maquina == "piedra" and usuario1 == "papel":
        print("Gana usuario1 ya que papel le gana a piedra")
    elif maquina == "tijera" and usuario1 == "piedra":
        print("Gana usuario1 ya que piedra le gana a tijera")

    elif maquina == "papel" and usuario1 == "piedra":
        print("Gana maquina ya que papel le gana a piedra")
    elif maquina == "piedra" and usuario1 == "tijera":
        print("Gana maquina ya que piedra le gana a tijera")
    elif maquina == "tijera" and usuario1 == "papel":
        print("Gana maquina ya que tijeras le gana a papel")
    
    elif maquina == usuario1:
        print("EMPATE")

    play_Again = input("Quieres jugar de nuevos y/n: ")
    if play_Again.lower() != "y":
        break

           





