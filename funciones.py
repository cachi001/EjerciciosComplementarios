import random
import math

#FUNCION EJERCICIO FUNCIONES 1
def add_number(num):
    add = 0
    while num > 0:
        digit = num % 10
        add += digit
        num //= 10
    
    return add

#FUNCIONES AHORCADO

#Esta funcion devuelve un jugador aleatorio de la lista
def select_player ():
    list_fotball_player=[
    "gvardiol",
    "musiala",
    "onana",
    "karim benzema",
    "mohamed salah",
    "kevin de bruyne",
    "bellingham",
    "kolo muani",
    "bernardo silva",
    "emiliano martinez",
    "ruben dias",
    "erling haaland",
    "julian alvarez",
    "vinicius",
    "rodri",
    "griezmann",
    "lionel messi",
    "lautaro martinez",
    "lewandowski",
    "luka modric",
    "mbappe"]
    player=random.choice(list_fotball_player)
    
    return player

#Esta funcion devuelve el nombre del jugador en "_"
def secret_word (player):
    word_original=""
    
    for i in player:
        if i != " " :
            word_original += "_"
        else:
            word_original += " "
    
    return word_original

#FUNCIONES BINGO

#Validar Numero del carton

def validate_card (bingo_card):
    while True:
        found = False
        print("Ingrese el valor del carton (1 A 75)")
        number = int(input("-> "))
        if number > 0 and number < 76:
            for card in bingo_card:
                for element in card:
                    if element == number :
                        found = True
                        break
            if found:
                print("ERROR: NUMERO YA INGRESADO")
            else:
                return number
        else:
            print("ERROR: NUMERO FUERA DE RANGO")

#Muestra el carton del bingo
def show_bingo_card(bingo_card):
    for i in range(5):
        row = sorted(map(str, bingo_card[i]))
        for j in range(5):
            if row[j] == 'x':
                cell_formatted = f"{row[j]:4}"
                print("\033[94m" + cell_formatted + "\033[0m", end=" ")
            else:
                cell_formatted = f"{row[j]:4}"
                print(cell_formatted, end=" ")
        print()

#Genera una bola y valida si ya salio antes, si no esta lo agrega a la lista y devuelve la bola
def validate_bingo_ball(bingo_balls):
    while True:
        ball = random.randint(1, 75)
        if ball not in bingo_balls:
            bingo_balls.append(ball)
            return ball

#Valida si el numero esta en el carton y lo remplaza por una 'x' de ser asi
def validate_number_card(bingo_card):
    bingo_balls = []
    game_won = False
    
    while not game_won:
        bingo_ball = validate_bingo_ball(bingo_balls)
        
        print("------------------------------------------------------------")
        print(f"BOLA NUMERO {bingo_ball}")
        found = False
        
        for i in range(5):
            for j in range(5):
                if bingo_card[i][j] == bingo_ball:
                    bingo_card[i][j] = 'x'
                    found = True
        
        show_bingo_card(bingo_card)
        
        if found:
            if check_for_winning_line(bingo_card):
                if not game_won:
                    message_win()
                    game_won = True
            else:
                print("\nNúmero en el cartón. Continuamos...")
        else:
            print("\nNúmero no encontrado en el cartón. Continuamos...")

#Verifica si se completo una linea
def check_for_winning_line(bingo_card):
    # Verificar líneas horizontales y verticales
    for i in range(5):
        if all(cell == 'x' for cell in bingo_card[i]) or all(bingo_card[j][i] == 'x' for j in range(5)):
            return True
    
    # Verificar diagonales
    if all(bingo_card[i][i] == 'x' for i in range(5)) or all(bingo_card[i][4 - i] == 'x' for i in range(5)):
        return True
    return False

#Si gana muestra el mensaje de win
def message_win ():
    print("BINGO!!!!!!")

#3)FUNCIONES TP5

#Ejercicio 1 (Funcion que valide un documento)

def validate_ID (id):
    
    if len(id)>6 and len(id)<9 :
        return True
    
    return False

#Ejercicio 2 (Longitud de la ultima palabra)

def str_length (cadena):
    cadena = cadena.split()
    
    if cadena :
        return len(cadena[-1])
    else:
        return 0

#Ejercicio 3 (Crea el id y lo retorna)
def return_id(name,long_last_name,digit_id):
    name = ((name.capitalize()).split())[:2]
    long_last_name = (long_last_name.split())[0]
    id = name[0] + str(len(long_last_name)) + str(digit_id[:3])
    return id

#Ejercicio 4 (Verifica si los numeros son multiplos)

def multiple_numbers (number1,number2):
    
    if number1 % number2 == 0 :
        return True
    else:
        return False

#Ejercicio 5 (Calcula el promedio de la temperatura y lo muestra)

def average_temperature (max,min):
    average = (max+min)/2

    print(f"\nEl promedio de la temperatura es {average}")

#Ejercicio 6 (Inserta un espacio por caracter y lo muestra)

def spaced_text(text):
    text = " ".join(text)
    print(text)

#Ejercicio 7 (Guarda y muestra el valor maximo y minimo de una lista)

def max_min_number (number_list):
    max_number = max(number_list)
    min_number = min(number_list)

    print(f"\nEl maximo valor de la lista es {max_number}")
    print(f"El minimo valor de la lista es {min_number}")

#Ejercicio 8 (Calcula el area y el perimetro,y los muestra)

def circumference (radius):
    perimeter = 2 *math.pi*radius
    area = math.pi*(radius**2)
    
    print(f"\nEl area de la circunferencia es {area}")
    print(f"El perimetro de la circunferencia es {perimeter}")

#Ejercicio 9 (Verifica si son correctas la contraseña y el usuario)

def login(attempts,user,password):
    if attempts == 1 :
        print("INTENTOS TERMINADOS")
    elif password == "asdasd" and user == "usuario1":
        print("Usuario y contraseña correcta")
        return True
    else:
        print("!Contraseña o usuario incorrecto")
        return False

#Ejercicio 10 (Guarda la seleccion del producto y aplica el descuento correspondiente)

def product_discount(product,discount,selection_product):
    value_prod = product[selection_product]
    aplicated_discount = value_prod - (value_prod * (discount / 100))
    return aplicated_discount

#Ejercicio 11 

#Retorna el tamaño de la lista
def list_size():
    while True:
        print("Ingrese el tamaño de la lista (1-5)")
        size = int(input("-> "))
        
        if size > 0 and size < 6:
            return size

#Recibe una funcion
def list_in_upper (size,name_list):
    name_list_upper = []
    counter = 0
    while counter < size:
        print("Ingrese nombres en la lista")
        name = input("-> ")
        
        if not name:
            continue
        else:
            name_list.append(name)
        counter += 1
    name_list_upper = name_list[:]
    name_list_upper = [name.upper() for name in name_list_upper]
    return name_list_upper

#Ejercicio 12

#Recibe una frase, separa las palabras y las agrega al diccionario con su longitud
def word_lenght_dictionary(phrase):
    
    phrase_split = phrase.split(" ")
    dictionary = {}
    for word in phrase_split:
        dictionary[word] = len(word)
    return dictionary

#FUNCIONES TP6

#Ejercicio 1
#Se agregan numeros a la lista y la retorna
def list_of_number ():
    number_list = []
    while True:
        print("Ingrese un numero para agregar a la lista (0 PARA SALIR)")
        num = int(input("-> "))
        
        if num == 0:
            break
        else:
            number_list.append(num)
    return number_list

#Ejercicio 2

#Buscamos el numero en la lista y si se encuentra se elimina
def search_number(number,number_list):
    if number in number_list:
        print(len(number_list))
        for i in range (len(number_list)-1):
            if number == number_list[i]:
                number_list.pop(i)
        print("\nSe elimino el numero de la lista")
    else:
        print("\nEl numero no se encontro en la lista")

#Muestra la lista de numeros
def show_list (number_list):
    for num in number_list:
        print(num, end=" ")

#Ejercicio 3

#Muestra la suma de los numeros de la lista
def list_sum(number_list):
    add = 0
    print("SUMATORIA DE LOS NUMEROS DE LA LISTA")
    for i in number_list:
        add += i
    print(add)

#Ejercicio 4

#Agrega a la lista los numeros menos al ingresado
def sort_list(number,number_list):
    minor_number_list = []
    for i in range(len(number_list)-1):
        if number_list[i] < number or number_list[i] == number:
            minor_number_list.append(number_list[i])
    return minor_number_list

#FUNCIONES TP7

#Ejercicio 1

#Ordenamos la lista con el metodo de burbuja
def bubble_sort(number_list):
    long_list = len(number_list)
    for i in range(long_list):
        for j in range(long_list-i-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list [j+1], number_list[j]
    return number_list

#Ejercicio 2

#Creamos una lista de palabras
def list_of_word():
    
    word_list = []
    while True:
        print("Ingrese una palabra (ESCRIBIR 'SALIR' PARA TERMINAR)")
        word = input("-> ")
        
        if not word:
            continue
        elif word.upper() == "SALIR":
            break
        else:
            word_list.append(word)
    return word_list

#Ordenamos la lista con el metodo de seleccion
def selection_sort(word_list):
    long = len(word_list)
    
    for i in range(long):
        min_index = i
        for j in range(i+1,long):
            if word_list[j] < word_list[min_index]:
                min_index = j
        word_list[i], word_list[min_index] = word_list[min_index], word_list[i]
    return word_list

#Ejercicio 5

#Ordenamos la lista de manera descendete con el metodo burbuja
def bubble_sort_descendet(number_list):
    long_list = len(number_list)
    for i in range(long_list):
        for j in range(long_list-i-1):
            if number_list[j] < number_list[j+1]:
                number_list[j], number_list[j+1] = number_list [j+1], number_list[j]
    return number_list

#FUNCIONES TP8

#Ejercicio 1

#Llamamos a la funcion de manera recursiva para sumar la cantidad de digitos
def digit_number(number,counter):
    if number > 0:
        return digit_number(number//10,counter+1)
    return counter

#Ejercicio 2

#Llamamos a la funcion de manera recursiva para verificar si a es potencia de b
def power_of_number (a,b):
    if a == 1:
        return True
    if a < b or a % b != 0:
        return False
    return power_of_number(a // b,b)

#Ejercicio 3

#Llamamos a la funciond de manera recursiva para obtener el mayor valor de una lista
def max_list(number_list,i,max):
    if i == 0:
        return max
    elif number_list[i] > max:
        max = number_list[i]
    return max_list(number_list,i-1,max)
