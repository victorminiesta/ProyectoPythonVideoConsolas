#!/usr/bin/python3

# Asegúrate de que tienes la biblioteca 'requests' instalada en tu entorno virtual
# Para instalarlo, puedes usar pip:
# pip install requests

import json
import requests

# Creo un formulario en el que el usuario tenga que elegir entre qué consola para 
# a continuación ver los videojuegos que contiene


print("¿Qué consola quieres mirar?")
print("1. PS4")
print("2. XBOXONE")
print("3. SWITCH")
print("Introduzca el número según lo que desees:")
print("-----------------------------------------")
eleccion = int(input(""))

if eleccion == 1:
    url = 'https://raw.githubusercontent.com/Elbriga14/EveryVideoGameEver/main/GamesDB/PS4Games.json'
elif eleccion == 2:
    url = 'https://raw.githubusercontent.com/Elbriga14/EveryVideoGameEver/main/GamesDB/XboxOneGames.json'
elif eleccion == 3:
    url = 'https://raw.githubusercontent.com/Elbriga14/EveryVideoGameEver/main/GamesDB/SwitchGames.json'
else:
    print("Opción no válida.")

respuesta = requests.get(url)

print("¿Qué género deseas ver?")
print("--------------------------------------------------------")
print("(Shooter, Platform, Sports, Puzzle, Real_Time strategy") 
print("Arcade, Grafic Adventure, Interactive drama, Action")
print("Visual Novel, Horror, Point-and-click adventure, Abstraction Games")
print("Survival, Role-playing, Dungeon crawl, Racing, Art, Simulator, Tactical")

generoDeseado = input("")

if respuesta.status_code == 200:
    datos = respuesta.json()  
    for juegos in datos:
        nombre = juegos.get('Game')
        anioSalida = juegos.get('Year')
        genero = juegos.get('Genre')
        print(f"Nombre: {nombre}, Año de salida: {anioSalida}, Género: {genero}")
else:
    print(f"No se pudo obtener datos de la URL. Código de estado: {respuesta.status_code}")


'''print("¿Qué género deseas ver?")
    print("-----------------------")
    print("Shooter")
    print("Platform")
    print("Sports")
    print("Puzzle")
    print("Real-time strategy")
    print("Arcade")
    print("Grafic Adventure")
    print("Interactive drama")
    print("Action")
    print("Visual Novel")
    print("Visual Novel")
    print("Horror")
    print("Point-and-click adventure")
    print("Abstraction Games")
    print("Survival")
    print("Role-playing")
    print("Dungeon crawl")
    print("Racing")
    print("Art")
    print("Simulator")
    print("Tactical")'''

