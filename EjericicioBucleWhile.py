
print("Ingrese numeros enteros positivos (0 PARA TERMINAR)")
even_counter = 0
odd_counter = 0
while True:
    number = int(input())
    if number == 0:
        break
    elif number % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

if even_counter == 0 and odd_counter == 0:
    print("No se han escrito numeros")
else:
    print(f"La cantidad de numeros pares es: {even_counter}")
    print(f"La cantidad de numeros impares es: {odd_counter}")