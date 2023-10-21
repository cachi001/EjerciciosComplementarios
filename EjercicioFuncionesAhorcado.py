
import funciones

#Llama a la funcion que retorna un jugador aleatorio

player = funciones.select_player()

#Llama a la funcion que retorna el jugador en "_"

word_original = funciones.secret_word(player)

#Los corazones son la cantidad de intentos
lives=["♥","♥","♥","♥","♥","♥"]
position_live = len(lives)-1  #tamaño de vidas para despues restarlas


print("\n!)Si se ingresa el jugador inocorrecto perdera todas sus vidas\n")
print("----------------------AHORCADO----------------------")
print()
while (True):
    #Muestra la palabra con "_" y las vidas actuales
    print(" ".join(word_original),"       "," ".join(lives))
    
    #Cuando todos los guiones se remplacen y la palabra este completa, el jugador gana
    if word_original == player :
        print("\n!!!Win!!!")
        break
    
    print("\nIngrese una letra o el nombre del jugador")
    letter=input("-> ").lower()
    position_letter = 0
    
    
    #Si letter es de un dígito y está en el player aleatorio se remplaza el "_" por la letra
    #Sino si letter es de un dígito y no está en player resta una vida / si vida son 0(-1) pierde
    #Sino / letter ingresado es de más de un dígito y es igual al player gana / sino es igual pierde y muestra el player aleatorio
    
    if len(letter)==1 and letter in player:
        for i in player:
            if i == letter :
                word_original = word_original[:position_letter]+letter+ word_original[position_letter+1:]
            position_letter += 1
    elif len(letter)==1 and letter not in player:
        lives[position_live]="♡"
        position_live-=1
        if position_live == -1 :
            print("\n!!!GAME OVER!!!        "," ".join(lives))
            print("\nEl jugador era", player)
            break
    else:
        if player == letter:
            print("\n!!!WIN!!!      "," ".join(lives))
            break
        else:
            print("\n!!!GAME OVER!!!")
            position_live=-1
            print("\nEl jugador era", player)
            break
