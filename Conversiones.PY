#TITULO: Converciones.py
#TYPE(), INT Y STR.FORMAT()
#|********************************************************************************************|


#Se utiliza la variable "STR" para la cadena de digitos
numero="1234"

#se muestra el tipo de variable que se utilizó . La salida de TYPE() no el STR sino TYPE
print(type(numero))

#la cadena se convierte a INT
numero=int(numero)

#se muestra el cambio del datos, aunque usamos misma variable
print(type(numero))

#Pasamos un STR con el objetivo (posicion de valores indicados con str format)
salida= "El número utilizado es {}"

#Se obtiene un resultado.El objetivo producido en {} se colocara el valor del numero.
print(salida.format(numero))

