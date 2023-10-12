#EJercicio1 y Ejercicio2
print("--------------------------------------------------------------------")
computer_years = int(input("Ingrese lo años que tiene su computadora: "))

if computer_years < 0:
    print("\nERROR! NUMERO NO VALIDO")
elif computer_years > 2:
    print("\nSu computadora es vieja")
else:
    print("\nSu computadora es nueva")

#Ejercicio3
print("--------------------------------------------------------------------")
name_person1 = input("Ingrese el nombre de la primera persona: ")
name_person2 = input("Ingrese el nombre de la segunda persona: ")

first_letter_person1 = (name_person1 [0]).lower()
first_letter_person2 = (name_person2 [0]).lower()

if first_letter_person1 == first_letter_person2:
    print("\nCoincidencia")
else:
    print("\nNo hay coincidencia")

#Ejercicio4
print("--------------------------------------------------------------------")

candidate_color = {
    "A" : "ROJO",
    "B" : "VERDE",
    "C" : "AZUL"
}

print("-----------------INGRESE QUE CANDIDATO DESEA VOTAR--------------")
print("A. Candidato por el Partido Rojo")
print("B. Candidato por el Partido Verde")
print("C. Candidato por el Partido Azul")

candidate = input("\n").upper()

if candidate == "A":
    print("\nUsted ha votado por el partido",candidate_color["A"])
elif candidate == "B":
    print("\nUsted ha votado por el partido",candidate_color["B"])
elif candidate == "C":
    print("\nUsted ha votado por el partido",candidate_color["C"])
else:
    print("ERROR! CANDIDATO INVALIDO")