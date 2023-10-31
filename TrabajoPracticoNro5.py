import funciones

#TP 5 FUNCIONES

#Ejercicio 1
print("--------------------VALIDAR ID--------------------")
#Ingresa el DNI
print("Ingresa un numero de DNI")
real_id = input("-> ")

#Llamamos a la fucnion para validar el ID
validate_id = funciones.validate_ID(real_id)

#Si la funcion retorna verdadero es valido, sino no.
if validate_id :
    print("El documento es valido")
else:
    print("El documenro NO es valido")

#Ejercicio 2
print("--------------------LONGITUD ULTIMA PALABRA--------------------")
#Ingresa una cadena
print("Ingresa una cadena")
str = input("-> ")

#Llamo a la funcion para que retorne la longitud de la ultima palabra
print("La longitud de la ultima palabra es",funciones.str_length(str))

#Ejercicio 3
print("--------------------CREAR ID--------------------")
while True:
    #Ingresa el nombre completo
    print("\n1)Ingrese su nombre completo(INGRESE UN VALOR VACIO PARA SALIR)")
    name = input("-> ")
    
    #Si esta vacio sale del bucle
    if not name:
        print("\nSaliendo...")
        break
    #Ingresa el apellido
    print("\n2)Ingrese su apellido")
    last_name = input("-> ")
    
    while True:
        #Ingresa el DNI
        print("\n3)Ingrese su numero de DNI")
        real_id = input("-> ")
        #Llamamos a la funcion para validar el ID
        if funciones.validate_ID(real_id):
            break
        #Si es invalido, volvemos a pedirlo
        else :
            print ("\n!)Ingrese un documento valido")
    #Llamamos a la funcion para crear el ID, y asignarlo a la variable.
    id = funciones.return_id(name,last_name,real_id)
    #Mostrams el id
    print(f"\nEl ID es {id}")

#Ejercicio 4
print("--------------------MULTIPLOS--------------------")
#Ingresan dos numeros
print("1)Ingrese el primer numero")
number1 = int(input("-> "))

print("\n2)Ingrese el segundo numero")
number2 = int(input("-> "))

#Llamamos a la funcion con el primero como parametro y vemos si es multiplo del segundo
if funciones.multiple_numbers(number1,number2):
    print(f"\nEl numero {number1} es multiplo de {number2}")
else:
    print(f"\nEl numero {number1} NO es multiplo de {number2}")
#Llamamos a la funcion con el segundo como parametro y vemos si es multiplo del primero
if funciones.multiple_numbers(number2,number1):
    print(f"\nEl numero {number2} es multiplo de {number1}")
else:
    print(f"\nEl numero {number2} NO es multiplo de {number1}")

#Ejercicio 5
print("--------------------TEMPERATURA--------------------")
#Ingresa la cantidad de dias para calcular el promedio de temperatura
print("1)Ingrese la cantidad de dias que desea calcular su temperatura")
number_of_days = int(input("-> "))
#Recorremos los dias y se ingresa la minima y maxima
for i in range (1,number_of_days+1):
    print(f"\n*******DIA {i}*******")
    print("\n2)Ingresa la temperatura minima")
    min_temperature = int(input("->"))
    print("\n3)Ingresa la temperatura Maxima")
    max_temperature = int(input("->"))
    #Llamamos a la funcion que obtiene el promedio y lo muestra
    funciones.average_temperature(max_temperature,min_temperature)

#Ejercicio 6
print("--------------------TEXTO--------------------")
#Ingresa una cadena de texto
print("1)Ingrese una cadena de texto")
text = input("-> ")

print("\nTEXTO CON ESPACIO:\n")
#Llamamos a la funcion para poner un espaciado por caracter y mostrarlo
funciones.spaced_text(text)

#Ejercicio 7
print("--------------------LISTA DE NUMEROS--------------------")
#Inicializamos una lista de numeros
number_list = []

while True:
    #Se ingrean numeros
    print("Ingrese un numero (0 PARA TERMINAR)")
    number = int(input("-> "))
    #Su es 0 sale
    if number == 0 :
        break
    #Se agregan a la lista
    number_list.append(number)
#Llamamos a la funcion que calcula el max y min de la lista, para mostrarlos
funciones.max_min_number(number_list)

#Ejericio 8
print("--------------------AREA Y PERIMETRO--------------------")
#Ingresa el radio de la circunferencia
print("Ingrese el radio de la circunferencia")
radius = int(input("-> "))

#Llamamos a la funcion para calcular el area y el perimetro, para mostrarlas
funciones.circumference(radius)

#Ejercicio 9
print("--------------------LOGIN--------------------")

#Inicialo variables
attempts = 3
leave = True

#Se repite el login hasta que sea correcto o intentos sean 0
while leave and attempts>0:
    #Se ingresa usuario y contraseña
    print(f"\nINTENTOS RESTANTES {attempts}")
    print("Ingrese el nombre de usuario")
    user = input("-> ").lower()
    print("Ingrese la contraseña de usuario")
    password = input("-> ").lower()
    #Llamamos a la funcion para verificar si el login es correcto
    leave = not funciones.login(attempts,user,password)
    
    #Si leave es verdadero, se resta un intento
    if leave:
        attempts -= 1

#Ejerciocio 10

print("--------------------DESCUENTO--------------------")
#Inicializo un diccionario con productos y precios
price_and_product = {
    "coca cola":900,
    "sanguche":500,
    "cerveza":700,
    "alfajor":200,
    "chocolate":180,
    "chicle": 150,
    }

print("-----------PRODUCTOS-----------")
#Muestra los productos y sus precios
for i in price_and_product:
    print(i,":",price_and_product.get(i))

total_price = 0 
while (True):
    #Se ingresa el producto que quiere con su descuento
    print("\n)Ingrese el nombre del producto que desea")
    product_name = (input("-> ")).lower()
    print(")Ingrese el decuento en porcentaje")
    discount = int(input("-> "))
    #Llamamos a la funcion para aplicar el descuento al precio y sumarlo al precio total
    total_price += funciones.product_discount(price_and_product,discount,product_name)
    #Condicion de salida
    print("\n!)Ingresa 1 para ingresar otro producto")
    finalize_purchase = int(input("-> ")) 
    if finalize_purchase != 1 :
        break
#Mostramos el precio total de la compra
print(f"\nEl precio total de la compra es con el descuento aplicado {total_price}")

#Ejercicio 11
print("--------------------FUNCION DE OTRA FUNCION--------------------")
#Inicializo una lista
names_list = []
#Llamo a una funcion y le paso como parametro una funcion que retorna el tamaño, y la lista
#Y retorna la lista anterios en mayusculas
names_list_upper = funciones.list_in_upper(funciones.list_size(),names_list)

#Muestra la lista
print("NOMBRES")
for name in names_list_upper:
    print(f"{name}",end=" ")

#Ejercicio 12
print("--------------------DICCIONARIO DE PALABRAS Y LONGITUD--------------------")
while True:
    #Ingresa una frase
    print("Ingrese una frase")
    phrase = input("-> ")
    #Si la frase esta vacia sigue
    if not phrase:
        continue
    else:
        break
#Llamamos a una funcion para dividir las palabras de la frase y colocarlas con su longitud en un
#diccionario
dictionary = funciones.word_lenght_dictionary(phrase)

#Mostramos el diccionario
print("PALABRA DE LA FRASE CON SU LONGITUD")
for word in dictionary:
    print(f"{word}: {dictionary[word]}")
