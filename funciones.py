import random


#1)FUNCION EJERCICIO FUNCIONES 1
def add_number(num):
    add = 0
    while num > 0:
        digit = num % 10
        add += digit
        num //= 10
    
    return add

#2)FUNCIONES AHORCADO

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

