#Titulo: Tabla.py
#FOR, RANGE()
#|*********************************************************************************************************************************************|
#se asigna una cierta cantidad de valores para obtener el resultado
numero=input("Dame un número del 1 al 9:")
numero=int(numero)

#Cuando nosotros ocupamos ejecutar varias veces un codigo debemos utilizar la funcion FOR, este se usa cuando nos piden categoria de valores
#en el ranfe no se incluye incluye otro rango, se realizaria otro por ejemplo 1 al 10
for i in range(1,11):
   salida="{} x {} = {}"
   #Se manda a imprimir el formato que el usuario quiere que aparezca
   print(salida.format(numero,i,i*numero))

 #La "i" va teniendo un cambio con cada repeticion que sea necesaria


