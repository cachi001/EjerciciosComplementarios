import funciones

#Ejercicio 1

print("---------------------------------------------------------------------")

#Creamos una lista de numeros
number_list = funciones.list_of_number()

#Mostramos la lista de numeros
funciones.show_list(number_list)

#Ejercicio 2
print("\n---------------------------------------------------------------------")
while True:
    #Ingresa un numero mayor a 0
    print("Ingrese un numero")
    number = int(input("-> "))
    if number > 0:
        break

#Le pasamos a la funcion el numero para buscarlo en la lista y eliminarlo
funciones.search_number(number,number_list)
#Mostramos la lista
funciones.show_list(number_list)

#Ejercicio 3
print("\n---------------------------------------------------------------------")

#Llamamos a la funcion para sumar todos los numeros de la lista
funciones.list_sum(number_list)

#Ejercicio 4
print("---------------------------------------------------------------------")
while True:
    #Ingresa un numero mayor a 0
    print("Ingrese un numero")
    number = int(input("-> "))
    if number > 0:
        break

#Hacemos una lista nueva con los numeros de la lista anterior
#pero solo tomando los menor al numero ingresado y los ordenamos
minor_number_list = sorted(funciones.sort_list(number,number_list))

#Mostramos la lista nueva
funciones.show_list(minor_number_list)

