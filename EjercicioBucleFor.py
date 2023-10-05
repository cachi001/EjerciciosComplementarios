letters = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u", "v","w","x","y","z"]

messages = []

for i in range (5):
     messages.append(input(f'Ingrese el mensaje {i+1}: '))
        
number = int(input("Ingrese el numero de la ciffra de cesar: "))
j = 0
for n in messages:
    string_word = ""
    for i in range (len(n)):
        if n[i].lower() in letters:
            pos_letter = letters.index(n[i].lower())
            var = (pos_letter+number)%27
            string_word += letters[var]  
        else:
            string_word += n[i]
    messages [j] = string_word.upper()
    j +=1 

i = 0
for n in messages:
    print(f"La palabra {i+1} encriptada es: {n}")
    i += 1
                           