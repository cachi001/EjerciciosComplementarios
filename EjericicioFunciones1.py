import funciones
digit_sum=0
number_sum=0
while (True):
    print("Ingrese un numero")
    num=int(input("->"))
    number_sum += num
    print("La suma del numero",num,"es",funciones.add_number(num))
    digit_sum += funciones.add_number(num)
    
    print("Ingrese 0 si desea salir")
    leave= int (input("->"))
    if (leave==0):
        break
print("La suma de los numeros ingresados es ",number_sum)
print("La suma total de cada digito es ",digit_sum)