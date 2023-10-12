#Programa de un restaurante que nos deja acceder como clientes o dueños
#Cliente: Vamos a poder pedir comidas y bebidas del menu. Nos va a dar el total de la cuenta
#Dueño: Nos va a pedir un usuario y contraseña para validar que somos dueños y nos va a dejar aumentar los precios



#Diccionario que almacena el menu nombres y precios

menu = {
   "Hamburguesa": 2000,
   "Pizza" : 3500,
   "Lomo" : 3500,
   "Pancho" : 650,
   "Coca Cola" : 750,
   "Sprite" : 750,
   "Cerveza" : 750,
   "Pepsi" : 750
}

#Variable intentos de inicio sesion
counter = 0
#Variable cuenta total del cliente
receipt=0

#Se ingresa si queremos aceder como clientes o dueños
print("---------------BIENVENIDO A CRUTACEO CASCARUDO---------------")
print("Ingrese si es cilente o dueño")
print("1)Cliente")
print("2)Dueño")
client = int (input("-> "))

#If va a ejecutar la parte del cliente 
if client == 1:
   #Muestrael menu con sus precios
   print("***********INGRESE QUE COMIDA O BEBIDA DESEA***********")
   print("-------------------COMIDAS-------------------")
   print("1)Hamburguesa $", menu["Hamburguesa"])
   print("2)Pizza $", menu["Pizza"])
   print("3)Lomo $", menu["Lomo"])
   print("4)Pancho $", menu["Pancho"])
   print("-------------------BEBIDAS-------------------")
   print("5)Coca Cola $", menu["Coca Cola"])
   print("6)Sprite $", menu["Sprite"])
   print("7)Cerveza $",menu["Cerveza"])
   print("8)Pepsi $", menu["Pepsi"])
   print("---------------------------------------------")
   
   #Se ingresa la eleccion y se suma a la variable hasta que ingrese un numero que no esta en la lista
   while(True):
      print("PARA SALIR INGRESE OTRO NUMERO")
      food=int(input("Eleccion-> "))
      
      if food==1:
         receipt +=  menu["Hamburguesa"]
      elif food==2:
         receipt += menu["Pizza"]
      elif food==3:
         receipt += menu["Lomo"]
      elif food==4:
         receipt +=  menu["Pancho"]
      elif food==5:
         receipt +=  menu["Coca Cola"]
      elif food==6:
         receipt +=  menu["Sprite"]
      elif food==7:
         receipt +=  menu["Cerveza"]
      elif food==8:
         receipt +=  menu["Pepsi"]
      else:
         print("Saliendo...")
         break
   
   #If No compro nada else es para mostrar el total de la compra
   if receipt == 0:
      print("USTED ES UN TACAÑO")
   else:
      print("Su cuenta total es de $",receipt)
      
#Else va a ejecutar lo del dueño
else:
   #Se repite que ingrese el usuario y el producto para aumentar el precio hasta que se ingrese un numero para salir (que no este en venta)
   while(True):
      
      #If supera los intentos sale del programa
      if counter == 3:
         print("!!!!!!!!!DEMASIADOS INTENTOS!!!!!!!!!")
         break
      
      #El programa pide los datos
      print("************************************************")
      print("1)Ingrese el usuario")
      user = input("Usuario-> ")
      print("2)Ingrese la contraseña")
      password = input("Contraseña-> ")
      
      #If se equivoca aumenta el intento y continua a la siguente vuelta
      if user != "JuanEmiliano12" or password != "puredepapa":
         print("!)USUARIO O CONTRASEÑA INCORRECTA")
         counter += 1
         continue
      
      #Se ingresa los datos bien pide producto a cambiar precio hata que ingrese un valor invalido
      while (True):
         print("************************************************")
         print("Ingrese que comida desea cambiarle el precio")
         print("!)Ingrese otro valor para salir")
         print("-------------------COMIDAS-------------------")
         print("1)Hamburguesa $", menu["Hamburguesa"])
         print("2)Pizza $", menu["Pizza"])
         print("3)Lomo $", menu["Lomo"])
         print("4)Pancho $", menu["Pancho"])
         print("-------------------BEBIDAS-------------------")
         print("5)Coca Cola $", menu["Coca Cola"])
         print("6)Sprite $", menu["Sprite"])
         print("7)Cerveza $",menu["Cerveza"])
         print("8)Pepsi $", menu["Pepsi"])
         print("---------------------------------------------")
         food=int(input("-> "))
         if food==1:
            menu["Hamburguesa"] = int(input("Precio-> "))
         elif food==2:
            menu["Pizza"] = int(input("Precio-> "))
         elif food==3:
            menu["Lomo"] = int(input("Precio-> "))
         elif food==4:
            menu["Pancho"] = int(input("Precio-> "))
         elif food==5:
            menu["Coca Cola"] = int(input("Precio-> "))
         elif food==6:
            menu["Sprite"] = int(input("Precio-> "))
         elif food==7:
            menu["Cerveza"] = int(input("Precio-> "))
         elif food==8:
            menu["Pepsi"] = int(input("Precio-> "))
         else:
            print("Saliendo...")
            break
      break



