#Titulo:Compara.py
#NESTED IF
#|******************************************************************************************************|

#Para un valor "condicional"usamos un IF dentro del IF, si se diera el caso que no fueran iguales
#  #Selecciona si los valores son iguales
##Indica si el 1° es mayor que el 2° o si el 1°es menor que el 2°
numero1=int(input("Numero1:"))
numero2=int(input("Numero2:"))
salida="Numero proporcionados: {} y {}. {}."

if(numero1==numero2):
    print(salida.format(numero1,numero2,"Los numeros son iguales"))
else:
    if numero1>numero2:
        print(salida.format(numero1,numero2,"El mayor es el primero"))
    else:
        print(salida.format(numero1,numero2,"El mayor es el segundo"))

