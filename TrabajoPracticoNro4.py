#Ejericicio1
print("------------------------------------------------------------------------------------------")
#Inicializamos la variable x con 0
x = 0

#Hacemos un while loop para escribir el valor de x incrementolo en 1 hasta que este tenga el valor de 30 como condicion de terminacion
while x < 30 or x != 30:
    #Incrementamos x en 1
    x += 1
    
    #Si x tiene un valor igual a 15, rompemos el loop
    if x == 15:
        break
    elif x == 4 or x == 6 or x == 10:
        #Escribimos ls numeros que se van a saltar si x toma los valores de 4,6 o 10 respectivamente
        print(f"Se salto el valor {x} de x")
        #Saltamos a la siguiente iteracion
        continue
    #Si no se cumple con ninguna de estas simplemente escribimos x
    else:
        print(x)

#Comprobamos si el bucle se rompio, o termino.
if x < 30:
    #Como x no llego al valor de 30, podemos asumir que no termino por completo por lo tanto se rompio
    print(f"\nSe rompio la ejecucion del bucle cuando x valia: {x}")

#Ejercicio2
print("------------------------------------------------------------------------------------------")
#Inicializamos la variable lines_str para almacenar todas las lineas que se van a ingresar, y line para almacenar la linea en cada iteracion
lines_str = []
line = ""

#Pedimos que se ingrese una linea de texto, y para salir break
print("Ingrese una secuencia de lineas (BREAK PARA SALIR)")
while True:
    #Se ingresa la linea
    line = input()
    #Se comprueba si se ingreso break para salir
    if line.upper() == "BREAK":
        break
    #Si no se ingresa break se almacena la linea en el arreglo lines_str
    else:
        lines_str.append(line)
#Separamos con un espacio en blanco
print("")
#Recorremos el arreglo para escribir cara linea con mayusculas
for str in lines_str:
    print(str.upper())

#Ejercicio3
print("------------------------------------------------------------------------------------------")
#Inicializamos las variables
operation = ""
operations_log = ""
amount = 0
bank_account = 0

#Pedimos que se ingrese la operacion y el monto separado con un espacio
print("Ingrese el tipo de operacion y el monto que desea realizar con un espacio para separar (D PARA DEPOSITO/R PARA RETIRO/ESPACIO VACIO PARA SALIR)")
#Hacemos un bucle while para repetir las operaciones hasta que se ingrese un espacio vacio
while True:
    #Recibimos la operacion con el monto a realizar
    operations_log = input()
    #Comprobamos si lo que se ingreso no es un espacio vacio,
    if operations_log == "":
        #En caso de que no se ingrese nada, se rompe el bucle
        break
    #Dividimos lo ingresado por el usuario para tener el tipo de operacion y el monto por separado
    operations_log = operations_log.split()
    #Se lo asignamos a sus variables correspondientes
    #Operation para la operacion
    operation = operations_log [0]
    operation = operation.upper()
    #Amount para el monto
    amount = int(operations_log[1])
    
    #Si la operacion ingresada es D, realizamos el deposito a la cuenta bancaria sumandole el monto
    if operation == "D":
        bank_account += amount
    #Si la operacion es R verificamos que bank_account sea mayor a cero
    #Porque no podemos retirar dinero, ya que el saldo es insuficiente
    elif bank_account > 0 and operation == "R":
        bank_account -= amount
    #Si la operacion ingresada no es D o R, continuamos con otra iteracion hasta que se ingrese bien la operacion
    else:
        continue
#Por ultimo mostramos por pantalla el saldo de la cuenta bancaria
print(bank_account)

#Ejericio4
print("------------------------------------------------------------------------------------------")
num=0
total_prime_number=0
while (True):
    num=int (input("Ingresa un numero (0 PARA TERMINAR)\n"))
    prime_number=0
    if num < 0:
        continue
    elif num == 0:
        break
    for i in range (1,num+1):
        if num%i ==0:
            prime_number+=1
    if prime_number==2:
        total_prime_number+=1

print(f"\nLa cantidad de numeros primos es {total_prime_number}")

#Ejercicio5
print("------------------------------------------------------------------------------------------")
year1 = 0
year2 = 0
while True:
    year1 = int(input("Ingrese el primer año: "))
    year2 = int(input("Ingrese un segundo año (MAYOR AL SEGUNDO): "))
    
    if year2 < year1:
        continue
    else:
        break

print("")
for i in range(year1, year2+1):
    
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0) and i % 10 == 0:
        print(f"El año {i} es un año bisiesto")

#Ejercicio6
print("------------------------------------------------------------------------------------------")
print("Numeros pares del 1 al 20")
for i in range(1,21):
    if i%2!=0:
        continue
    else:
        print(i)

#Ejercicio7
import random
print("------------------------------------------------------------------------------------------")
number_list=[random.randint(1,100) for i in range(10)]
print(number_list)
print("Intenta adivinar el numero")
for i in range(0,len(number_list)):
    num=int(input())
    if num in number_list:
        print("Se encontro")
        break
    else:
        print("Intenta otra vez")

#Ejercicio8
print("------------------------------------------------------------------------------------------")
option = 0
print("Ingrese el numero correspondiente a la opcion que desea seleccionar (0 TERMINAR)")
while True:
    print("")
    print("1.OPCION 1")
    print("2.OPCION 2")
    print("3.OPCION 3")
    
    print("")
    number = int(input())
    
    if number == 0:
        break
    elif number == 1:
        print("\nUsted selecciono la opcion 1")
    elif number == 2:
        print("\nUsted selecciono la opcion 2")
    elif number == 3:
        print("\nUsted selecciono la opcion 3")
    else:
        continue

print("\nBucle terminado")
