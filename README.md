# ProyectoPythonVideoConsolas

Prerequisitos:
-Tener instalado Python 3.11.6

sudo apt-get update
sudo apt-get install python(version)

-Tener instalado pip.

sudo apt-get install python3-pip

Mi aplicación Se basa en un programa que extrae los datos de un Json subido a una API web 
pública en la que se guardan los datos de todos los videojuegos pertenecientes a las videoconsolas PS4, XBOX ONE y Nintendo Switch
y a continuación los juegos con el género que le tendrá que dar el usuario.

El funcionamiento es así:
Lo primero el programa le preguntará al usuario qué videoconsola deseará mirar, Elegir entre 1, 2 o 3 y a continuación le dará a elegir entre los diferentes géneros que hay
(El programá te dirá los gérenos que hay y además tienes un archivo a parte con ellos llamado "generos.txt")

Para todo esto necesitarás instalar requests:

pip install requests

Después de elegir el género el programa te mostrará todos los videojuegos pertenecientes a ese género dentro de la videoconsola que elegiste anteriormente.
 
