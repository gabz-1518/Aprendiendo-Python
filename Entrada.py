#Titulo:Entrada.py
#INPUT(), STR-ISDIGIT(), STR.FIND()
#|******************************************************************************************************************|
entrada=input()
print(type(entrada))

#Se obtiene el resultado a verificar  con la variable booleana, si es digito y se no se localiza en lo capturado,
#lo que nos diria que es un numero decimla (FLOAT)

#Si FIND retorna -1, quiere decir que el anterior numero no se encontró.
#Si llega a ser entero es verdadero (TRUE), quiere decir que lo capturado es numero entero.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #Aqui se ejecutara las condiciones si llegaran hacer verdaderas (TRUE)
    print("Dato entero. ¡Muy bien!")
else:
    #Aqui se ejecutaran las condiciones si llegaran hacer falsa (FALSE)
    print("Dato no es entero. Intentar nuevamente.")

