#Tutulo: Tablas.py
#FOR ELSE, NESTED FOR
#|********************************************************************************************************************|

#Aqui usamos la funcion FOR y despues ocuparemos un FOR dentro de este
for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))

    #Para poder saltar una linea en el codigo poder usar la funcion PRINT()(los parentesis quiere decir sin argumentos)
    print()
    for j in range(1,11):
        #En esta seccion fue necesario usar la letra "i" para el numero base y la "j" para indicar el elemento en la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al concluir volvemos a usar PRINT(), para poder realizar otr tabla y que estas no permanezcan juntas
        print()

