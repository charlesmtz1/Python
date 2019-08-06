import os
#Python puede trabajar con archivos, ya sea leerlos, escribirlos o crearlos.

#Para abrir un archivo se necesita el comando open(). Si el archivo no existe, open() lo creara.
f = open("Prueba.txt","w")

#Existen 4 metodos para abrir un archivo:
f = open("Prueba.txt", "r")     #Solo lectura. Por defecto abre asi los archivos si no se especifica este parametro.
#f = open("Prueba.txt", "w")         #Escritura. Borra el contenido del archivo y esta listo para contenido nuevo.
#f = open("Prueba.txt", "a")         #Append. Escribe en el archivo a partir de la ultima linea que tiene creada el archivo.
#f = open("Prueba.txt", "x")         #Validador. Si el archivo ya existe, no crea nada y finaliza la ejecucion, a menos que se pueda controlar el error.

#Tambien se puede especificar si el archivo se abrira en modo texto o binario(para imagenes)
#f = open("Prueba.txt", "rb")
#f = open("Prueba.txt", "wt")

#Cuando se abre un archivo en modo escritura, pero este no existe, se creara automaticamente. El modo x lanzara un error si dicho archivo ya esta creado.


#Para mostrar en pantalla el contenido de un archivo, usaremos la funcion read()
print(f.read())     #Para que esta funcion trabaje, necesita abrirse el archivo primero con la propiedad r

print(f.readline())    #Readline permite la lectura del archivo linea por linea. Se puede colocar un parametro para indicar que linea leer.

#Para cerrar un archivo, usaremos close()
f.close()   

#Si queremos escribir dentro de un archivo, usaremos la funcion write. Recuerda abrir el archivo primero en modo w o a
f = open("Prueba.txt", "w")

f.write("Hola Mundo")

f.close()
###########################################################################################
#Para borrar archivos en Python, necesitaremos importar el modulo OS
import os

#Usaremos la funcion remove del modulo os para borrar el archivo que especifiquemos.
os.remove("Prueba.txt")

#Si queremos validar que el archivo este disponible antes de eliminarlo, podemos usar la funcion exists
if os.path.exists("Prueba.txt"):
    os.remove("Prueba.txt")
else:
    print("El archivo no existe")


#Si queremos borrar una carpeta, usaremos la funcion rmdir(). Solo se podra borrar si la carpeta no tiene archivos dentro.
try:
    os.rmdir("Carpeta")
except FileNotFoundError:
    print("La carpeta no existe!")
