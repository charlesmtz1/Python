from time import sleep

#El modulo pathlib nos permite interactuar con archivos y carpetas a partir que indiquemos una ruta y/o nombre de archivo.
#Esta herramienta se usa principalmente para automatizacion de procesos.

#Importaremos la clase Path del modulo pathlib
from pathlib import Path

#Como importamos una clase, para poder utilizarla necesitamos crear los objetos.
path = Path("..\\Mosh")     #La clase Path necesita de argumentos para trabajar. En este caso es una ruta.
path2 = Path("Carpeta Dummy")   #Aqui se paso como argumento un nombre de carpeta.

#Si queremos validar que una ruta o archivo existe, usaremos la funcion exists().
print(path.exists())

#Para crear carpetas en el directorio especificado, usaremos mkdir()
path2.mkdir()
sleep(5)

#De igual forma, para remover un directorio, usaremos rmdir()
path2.rmdir()

#glob() funciona como un parser de archivos. Permite buscar un archivo o archivos, directorios, etc dentro de una ruta especificada.
#Se requiere de un loop for para poder imprimir los resultados de la busqueda en pantalla.
for file in path.glob("*.py"):
    print(file)
