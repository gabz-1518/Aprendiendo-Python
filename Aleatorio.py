#Titulo: Aleatorio.py:
#IMPORT, DEF, RANDOM.RANDRANGE()
#|*******************************************************************************************************************************************|"

#El lenguaje python tiene una diversidad de librerias que podemos usar.
#Las librerias que posee el lenguaje comunmente se les conoce como modules(MODULE) para poder usar esta funcion
#debemos colocar IN modulo en el programa, como primer paso se debe importar, utilizando IMPORT
import random

#Se redacta la variable FLOAT y se le dicta el valor
numero1=float(10.5)

#En este lenguaje, una FUNCION es una porción o bloque de código reutilizable que se encarga de realizar una determinada tarea.
#como una unidad de ejecucion.Para cada funcion se debe declarar con DEF con todo lo demas a la derecha esto forma parte de una DUNCION
def miFuncion():

    #El numero indicado se tranforma en FLOAT el número lanzado por RANDOM.RANDRANGE() (Este solo esta libre si se traslada al modulo Random).
    numero2=float(random.randrange(1,10))

    #Se ocupan meta sustituciones para los resultados.
    mensaje="la suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

#Se realiza el codigo determinado
miFuncion()


