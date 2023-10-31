import funciones

print("------------------BINGO------------------")
#Creo el carton de 5x5
bingo_card = [[] * 5 for _ in range(5)]
#Inicializo la lista de la posicion
position_list = 0
#Se llena el carton y se coloca en la posicion correspondiente
for i in range(0,25):
    if position_list < 5:
        card_value = funciones.validate_card(bingo_card)
        bingo_card[position_list].append(card_value)
    if len(bingo_card[position_list]) >= 5:
        position_list += 1

#Llamamos a la funcion para mostrar el carton del bingo
funciones.show_bingo_card(bingo_card)
#Llamamos a la funcions para validar si el numero de la bola esta en el carton 
funciones.validate_number_card(bingo_card)