#!/usr/bin/python3

# Asegúrate de tener la version de python ###### y la biblioteca 'requests' instalada en tu entorno virtual
# Para instalarlo, puedes usar pip:
# ---------------------
#pip install python #######
# ---------------------
# pip install requests
#----------------------
# La libreria requests es una libreria que facilita el trabajo con peticiones http para en nuestro extrayendo el contenido de un json subido a una web

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
    url = "https://raw.githubusercontent.com/Elbriga14/EveryVideoGameEver/main/GamesDB/PS4Games.json"
elif eleccion == 2:
    url = "https://raw.githubusercontent.com/Elbriga14/EveryVideoGameEver/main/GamesDB/XboxOneGames.json"
elif eleccion == 3:
    url = "https://raw.githubusercontent.com/Elbriga14/EveryVideoGameEver/main/GamesDB/SwitchGames.json"
else:
    print("Opción incorrecta.")

respuesta = requests.get(url)

print("¿Qué género de videojuego deseas consultar?")
print("-------------------------------------------------------------------------")
print("(Shooter, Platform, Sports, Puzzle, Real_Time strategy") 
print("Arcade, Grafic Adventure, Interactive drama, Action")
print("Visual Novel, Horror, Point-and-click adventure, Abstraction Games")
print("Survival, Tactical, Role-playing, Dungeon crawl, Racing, Art, Simulator")
print("-------------------------------------------------------------------------")

generoDeseado = input("")

# Guardo el genero que quiera en la variable "generoDeseado" y luego usando un if dentro del for que compruebe cada uno de los generos con el generoDeseado
# y que imprima los que coincidan

if respuesta.status_code == 200:
    datos = respuesta.json() 
    for juegos in datos:
        nombre = juegos.get('Game')
        anioSalida = juegos.get('Year')
        genero = juegos.get('Genre')
        if genero == generoDeseado:
            print(f"Nombre: {nombre}, Año de salida: {anioSalida}, Género: {genero}")
            print("-----------------------------------------------------------------")
else:
    print(f"No se pudo obtener datos de la URL. Código de estado: {respuesta.status_code}")