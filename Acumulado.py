#Titulo:Acumulado.py
#WHILE, BREAK, +=
#|************************************************************************************************************|

#La variables se usan explicitamente
acumulado=int(0)
numero=str("")

#La funcion de TRUE la podemos usar para varias cosas como en este caso para while que sirve para
#un ciclo infinito este no se rompera hasta que se use la instruccion break
#Si se llegara a dar el caso de un numero vacio, se debe de dar a conocer el problema para que salga.

while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        print("Vacio.Salida del programa.")
        break
    else:
        #Para este apartado se debe hace un calculo como (acumulado=acumulado + numero)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
