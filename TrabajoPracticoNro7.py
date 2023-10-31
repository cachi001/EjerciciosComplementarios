import funciones

#Ejercicio 1

print("---------------------------------------------------------------------")

#Creamos una lista de numeros
number_list = funciones.list_of_number()

#Ordenamos la lista de manera ascendente mediante una funcion usando el metodo burbuja
ordered_list = funciones.bubble_sort(number_list)

#Mostramos la lista
funciones.show_list(ordered_list)

#Ejercicio 2

print("\n---------------------------------------------------------------------")

#Creamos una lista de palabras
word_list = funciones.list_of_word()

#Mostramos la lista no ordenada
print("LISTA NO ORDENADA")
funciones.show_list(word_list)

#Llamamos a la funcion para ordenar la lista
ordered_list = funciones.selection_sort(word_list)

#Mostramos la lista ordenada
print("\nLISTA ORDENADA DE MANERA ASCENDENTE")
funciones.show_list(ordered_list)

#Ejercicio 5

print("\n---------------------------------------------------------------------")

#Creamos una lista de numeros
number_list = funciones.list_of_number()

#Ordenamos la lista de manera descendente
ordered_list = funciones.bubble_sort_descendet(number_list)

#Mostramos la lista
funciones.show_list(ordered_list)