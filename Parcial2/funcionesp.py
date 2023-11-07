#FUNCIONES PARCIAL 2

#Funcion que se encarga de llenar la matriz
def fill_matrix(dna):
    lenght = len(dna)
    
    for i in range(lenght):
        for j in range(lenght):
            letter = ""
            while True:
                #Se ingresa una letra
                print(f"Ingrese la letra de la fila {i + 1} y columna {j + 1} de ADN")
                letter = input("-> ").upper()
                #Se valida si la letra es solo una y si es (A/T/G/C)
                if len(letter) == 1 and check_letter (letter):
                    break
                else:
                    print("LETRA NO VALIDA (DEBE SER A, T, C, G)")
            #Se concatenan las letras en la matriz
            dna[i] = dna[i] + letter

#Funcion que comprueba si la letra ingresada es correcta
def check_letter(letter):
    return letter in "ATGC"

#Funcion que comprueba si la matriz de ADN es mutante o no
def is_mutant(dna):
    lenght = len(dna)
    counter = 0
    
    #Comprueba las filas
    for i in range(lenght):
        #Se valida si la fila tiene mas de una secuencia de cuatro letras iguales (Mutante)
        if check_sequence(dna[i]):
            counter += 1
            if counter > 1:
                return True
    
    #Comprueba las columnas
    for j in range(lenght):
        
        #Se guardan las letras de cada columna
        column = ''.join(dna[i][j] for i in range(lenght))
        #Se valida si la columna tiene mas de una secuencia de cuatro letras iguales (Mutante)
        if check_sequence(column):
            counter += 1
            if counter > 1:
                return True
    
    #Comprueba las diagonales de izquierda a derecha
    for i in range(lenght - 3):
        for j in range(lenght - 3):
            #Se guarda una secuencia diagonal de cuatro letras
            diagonal = ''.join(dna[i + k][j + k] for k in range(4))
            #Se valida si la diagonal tiene mas de una secuencia de cuatro letras iguales (Mutante)
            if check_sequence(diagonal):
                counter += 1
                if counter > 1:
                    return True
    
    #Comprueba las diagonales de derecha a izquierda
    for i in range(lenght - 3):
        for j in range(lenght - 3, lenght):
            #Se guarda una secuencia diagonal de cuatro letras
            diagonal = ''.join(dna[i + k][j - k] for k in range(4))
            #Se valida si la diagonal tiene mas de una secuencia de cuatro letras iguales (Mutante)
            if check_sequence(diagonal):
                counter += 1
                if counter > 1:
                    return True
    
    return False

#Funcion que verifica si hay una secuencia de cuatro letras iguales en la matriz ADN
def check_sequence(sequence):
    return any(subsequence in sequence for subsequence in ["AAAA", "TTTT", "CCCC", "GGGG"])

#Funcion que muestra la matriz
def show_matrix(dna):
    #Recorre las filas
    for row in dna:
        #Escribe cada letra de la fila y deja un espacio entre letra
        for letter in row:
            print(letter, end=" ")
        #Deja un salto de linea
        print()