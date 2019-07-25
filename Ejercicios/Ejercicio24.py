#Ejercicio 24
#Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. Muestra por pantalla en cuanto se habrá 
#convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
#Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años). Probar el programa 
#sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.

def calculo_prestamo(C, x, n):
    return C * (1 + x/100) ** n


print("$$$ Prestamos Chanchito $$$\n")
cantidad_de_dolares = float((input("Cuanto es la cantidad de dolares que necesitas?: ")))
interes = float(input("Que tasa de interes manejaras?: "))
años = int(input("A cuantos años vas a pagar?: "))

print(f"A {años} que seleccionaste, mas el interes aplicado, este seria costo total del prestamo: ${calculo_prestamo(cantidad_de_dolares, interes, años)}")
