#Titulo:Multiplo.py
#%,AND, OR
#|************************************************************************************|


#Se coloca un numero para la conversion a int
#Se coloca un  valor booleano en la evaluacion de residuales.
#Si me lanza un numero sero este es multiplo.

numero=int(input("Dame un numero entero: "))
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)

if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("correco,")
else:
    print("incorrecto.")

#____________________________________________________#
#NOTAS
#El valor AND nos lanza por verdadero si todas son verdaderas
#El valor OR nos lanza por verdadero si 1 es verdadera.
#Los parentesis le dicen al lenguaje que los valores son juntos y la 3° esta sola.