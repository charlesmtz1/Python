#Los paquetes son una coleccion de modulos dentro de una carpeta. Esto permite una mejor organizacion de modulos cuando estos son demasiados o se quieren
#almacenar por categorias o funcionalidad.

#Se tiene que crear una carpeta y se le pondra un nombre(este sera el nombre del paquete)
#Dentro de la carpeta crearemos un archivo __init__.py , este archivo indicara a Python que se trata de un paquete de modulos.
#Posteriormente guardaremos todos los archivos .py que son considerados modulos dentro de nuestro paquete.

#Para importar un paquete, utilizaremos import, seguido del modulo que queremos utilizar (Para fines practicos, nuestro paquete se llama Tools)
import Tools.Saludo

#Para utilizar una funcion de un modulo dentro de un paquete, realizaremos lo siguiente:
Tools.Saludo.buenos_dias("Carlos")

#Si se ocupa mas de un modulo, podemos declarar mas imports o utilizar comas.
import Tools.Saludo
import Tools.Despedida
import Tools.Saludo, Tools.Despedida

#Al mandar llamar una funcion de un paquete de forma simple, genera mucha escritura de codigo y a veces se torna engorroso. Podemos acortar el codigo importando
#detalladamente cada funcion de las siguientes formas:

from Tools import Saludo
from Tools.Despedida import adios

Saludo.buenos_dias("Carlos")
adios("Carlos")

#Tambien se pueden utilizar alias para utilizar funciones o modulos completos
from Tools import Saludo as bienvenida
from Tools.Despedida import adios as salida

bienvenida.buenos_dias("Carlos")
salida("Carlos")
