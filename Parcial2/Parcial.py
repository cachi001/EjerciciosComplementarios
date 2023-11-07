import funcionesp

#PARCIAL 2

#Inicializo la matriz
dna = [""] * 6

#Llamo a la funcion para llenar la matriz
funcionesp.fill_matrix(dna)

#Muestro la matriz por medio de la funcion
print("\nMATRIZ DE ADN")
funcionesp.show_matrix(dna)

#Llamo a la funcion para verificar si la matriz de ADN es mutanto o no
if funcionesp.is_mutant(dna):
    print("\nEs mutante")
else:
    print("\nNo es mutante")

