#Ejercicio 1
print("------------------------------------------------------------------------------------------")
word = input("Ingrese una palabra: ")

for i in range (10):
    print(f"{i+1} {word}")

#Ejercicio2
print("------------------------------------------------------------------------------------------")
age = int(input("Ingrese su edad: "))

for i in range (0,age):
    print(f"Años cumplidos {i+1}")

#Ejercicio3
print("------------------------------------------------------------------------------------------")
print("Ingrese un numero entero positivo")
number = -1
while number < 0:
    number = int(input())

for i in range(1,number+1):
    if i % 2 != 0:
        if i+1 == number:
            print(i, end= ".")
        else:
            print(i, end = ",")

#Ejercicio4
print("------------------------------------------------------------------------------------------")
print("Ingrese un numero entero positivo")
number = -1
while number < 0:
    number = int(input())

for i in range(number):
    if i + 1 == number:
        print(i+1, end = ".")
    else:
        print(i+1, end = ",") 

#Ejercicio5
print("\n------------------------------------------------------------------------------------------")
amount_invest = int(input("Ingrese la cantidad a invertir: "))
annual_interest = int(input("Ingrese el interes anual %: "))
year = int(input("Ingrese el numero de años: "))
time_per_year = 12

print("\n")
for i in range (year):
    
    time_per_year *= i+1
    earned_capital = (amount_invest * annual_interest * time_per_year) / 100
    print(f"El capital obtenido en el año {i+1} con una tasa de interes anual del {annual_interest}% fue de {earned_capital}$ ")

#Ejercicio6
print("------------------------------------------------------------------------------------------")
print("Ingrese un numero entero positivo")
number = -1
while number < 0:
    number = int(input())

print("\nTriangulo Rectangulo de asteriscos")
for i in range (number):
    for j in range (i+1):
        print(" * ", end= " ")
    print(" ")

#Ejercicio7
print("------------------------------------------------------------------------------------------")
print("Tablas de multiplicar del 1 al 10")
for i in range (10):
    for j in range (10):
        print(f"{i+1} x {j+1} = {(i+1)*(j+1)}")
    print("")

#Ejercicio8
print("------------------------------------------------------------------------------------------")
print("Ingrese un numero entero positivo")
number = -1
while number < 0:
    number = int(input())

current_num = 1
print("\nTriangulo Rectangulo de numeros")
for i in range (1,number+1):
    for j in range (current_num,0,-2):
        print(f" {j} ", end= " ")
    current_num += 2
    print(" ")

#Ejercicio9
print("------------------------------------------------------------------------------------------")
var = "contraseña"
password_user = ""
while password_user != var:
    password_user = input("Ingrese la contraseña: ")

#Ejercicio10
print("------------------------------------------------------------------------------------------")
print("Ingrese un numero entero positivo")
number = -1
while number < 0:
    number = int(input())

divider = 0

for i in range (1,number+1):
    
    if number % i == 0:
        divider += 1

if divider == 2:
    print(f"\nEl numero {number} es primo")
else:
    print(f"\nEl numero {number} no es primo")

#Ejercicio11
print("------------------------------------------------------------------------------------------")
word = input("Ingrese una palabra: ")

for i in range (len(word),0,-1):
    
    print(f" {word[i-1]}", end= " ")

#Ejercicio12
print("\n------------------------------------------------------------------------------------------")
phrase = input("Ingrese una frase: ")
letter = input("\nIngrese una letra: ")

counter = 0
for i in range (len(phrase)):
    
    if phrase[i] == letter:
        counter += 1

print(f"\nLa cantidad de veces que se encontro la letra en la frase fue {counter}")

#Ejercicio13
print("------------------------------------------------------------------------------------------")
var = ""
while True:
    var = input("Ingrese algo (INGRESE SALIR PARA SALIR): ")
    if var.lower() == "salir":
        break

    word_lenght = len(var)
    for i in range (len(var)):
        for j in range (word_lenght):
            print(f" {var[j]}", end="")
        word_lenght -= 1
        print("")

#Ejercicio14
print("------------------------------------------------------------------------------------------")
number1 = 1
number2 = 0
while number1 > number2:
    number1 = int(input("Ingrese el primer numero: "))
    number2 = int(input("Ingrese el segundo numero (MAYOR QUE EL PRIMERO): "))

print("\nPARES")
for i in range (number1,number2+1):
    if i % 2 == 0:
        print(i, end=" ")
print("\nIMPARES")
for i in range (number1,number2+1):
    if i % 2 != 0:
        print(i, end=" ")

#Ejercicio15
print("\n------------------------------------------------------------------------------------------")
print("Ingrese un numero entero positivo")
number = -1
while number < 0:
    number = int(input())

print("\nDivisores")
for i in range(1,number+1):
    if number % i == 0:
        print(i, end=" ")

#Ejercicio16
print("\n------------------------------------------------------------------------------------------")
num_count = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
number = 0
counter_negative_number = 0
i = 0

while i < num_count:
    number = int(input("Ingrese un numero: "))
    
    if number < 0:
        counter_negative_number += 1
    i += 1

print(f"\nLa cantidad de negativos fue de {counter_negative_number}")

#Ejercicio17
print("------------------------------------------------------------------------------------------")
word = input("Ingrese una palabra: ")
vocals = ("a","e","i","o","u")
vocals_word = []

for letter in word:
    if letter in vocals and letter not in vocals_word:
        vocals_word += letter
print("\nVocales de la palabra")
for n in vocals_word:
    print(n, end=" ")

#Ejercicio18
print("\n------------------------------------------------------------------------------------------")
fibonacci = []
for i in range(11):
    if i == 0 or i == 1:
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("Fibonacci")
for n in fibonacci:
    print(n, end=" ")

#Ejercicio19
print("\n------------------------------------------------------------------------------------------")
amount_to_save = int(input("Ingrese la cantidad de dinero que desea ahorrar $"))
amount_saved = 0
while amount_saved <= amount_to_save or amount_saved < 0:
    
    amount_saved += int(input("Cantidad a ahorrar: "))

print(f"\nTotal ahorrado ${amount_saved}")

#Ejercicio20
print("------------------------------------------------------------------------------------------")
total_amount = 0
while True:
    
    number = int(input("Ingrese un numero (0 PARA TERMINAR): "))
    if number == 0:
        break
    else:
        total_amount += number

print(f"\nLa suma de todos los numeros ingreseados es {total_amount}")

#Ejercicio21
print("------------------------------------------------------------------------------------------")
big_num = 0
while True:
    
    number = int(input("Ingrese un numero (0 PARA TERMINAR): "))
    if number == 0:
        break
    elif number > big_num:
        big_num = number

print(f"\nEl mayor de los numeros fue {big_num}")

#Ejercicio22
print("------------------------------------------------------------------------------------------")
sum_num = 0
counter_even = 0
number_int = 0
while True:
    
    number_str = input("Ingrese un numero (-1 PARA TERMINAR): ")
    number_int = int(number_str)
    sum_num = 0
    if number_int == -1:
        break
    elif number_int % 2 == 0:
        counter_even += 1
    for n in number_str:
        sum_num += int(n)
    print(f"La suma de los digitos del numero {number_int} es {sum_num}")

print(f"\nLa cantidad de numeros pares fue de {counter_even} ")

#Ejercicio23 y Ejercicio24
print("------------------------------------------------------------------------------------------")
purchase_amount = -1
total_to_pay = 0
while True:
    
    purchase_amount = int(input("Ingrese los montos de las compras (0 PARA TERMINAR) $"))
    if purchase_amount == 0:
        break
    elif purchase_amount == -1:
        continue
    total_to_pay += purchase_amount

if total_to_pay > 1000:
    total_to_pay -= (total_to_pay * 0.10)
    print(f"\nEl total total a pagar con un 10% de descuento es ${total_to_pay}")
else:
    print(f"\nEl total total a pagar es ${total_to_pay}")

#Ejericicio25
print("------------------------------------------------------------------------------------------")
number = -1
while number < 0:
    number = int(input("Ingrese un numero entero positivo: "))

var = number
factorial = 1
print("\nFactorial")
for i in range(number,0,-1):
    if i == 0:
        print("0 = 1")
    elif var == number:
        print(number, end=" x ")
    elif i == 1:
        print(f"{var} = {factorial}")
    else:
        print(var,end=" x ")
    var -= 1
    factorial *= i

print("------------------------------------------------------------------------------------------")

