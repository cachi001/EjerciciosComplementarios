import funciones

#Ejercicio 1
print("--------------------------------------------------------------------------")
while True:
    #Ingresa un numero mayor a 0
    print("Ingrese un numero")
    number = int(input("-> "))
    if number > 0:
        break
counter = 0
digit_amount = funciones.digit_number(number,counter)

print(f"\nLa cantidad de digitos que tiene el numero es {digit_amount}")

#Ejercicio 2
print("--------------------------------------------------------------------------")
while True:
    #Ingresa dos numeros positivos
    print("Ingrese un primer numero")
    number1 = int(input("-> "))
    print("Ingrese un segundo numero")
    number2 = int(input("-> "))
    if number1 > 0 and number2 > 0:
        break

#Validamos si el primer numero es potencia del segundo
validation = funciones.power_of_number(number1,number2)

#Si retorna True es potencia, sino no
if validation:
    print(f"\nEl numero {number1} es potencia del numero {number2}")
else:
    print(f"\nEl numero {number1} no es potencia del numero {number2}")

#Ejercicio 5
print("--------------------------------------------------------------------------")
#Creamos una lista de numeros
number_list = funciones.list_of_number()

#Mostramos la lista
for num in number_list:
    print(num, end= " ")

#Inicializamos el tamaño y el numero maximo
i = len(number_list)-1
max = 0
#Llamamos a la funcion para retornar el max de la lista
max_number = funciones.max_list(number_list, i,max)

#Mostramos el mensaje correspondiente
print(f"\nEl mayor numero de la lista es {max_number}")
