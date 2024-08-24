# ejercicios de repaso
#1
tupla1 = 1, 2, 3, 4, 5
print (tupla1)
tupla2 = ('Bioingenieros', 'Udea', '2024', 0, 1, 2)
print (tupla2)

#2
print(f'{tupla2[1]} ciudad universitaria')
#3
print(f'El resultado de elevar {tupla2[4]} al cuedrado es {tupla2[4]**2}')
#4
print(tupla1)
print(tupla2)

tupla3 = tupla1 , tupla2
print(tupla3)
#5
print(tupla3[1][0])
print('\nCONCATENANDO.....\n')
print(f'Programa de {tupla3[1][0]} de la UdeA')
#6
tupla1 = 1, 5, 2, 3 ,4, 5
tupla2 = ('Bioingenieros', 'Udea', '2023', 9, 'Udea', 8, 7, 'Udea')
print("Número de vez que aparece el 5 en la tupla1: ",tupla1.count(5))
print("Número de vez que aparece 'Udea' en la tupla2: ",tupla2.count('Udea'))
print("Posición del número 5 en la tupla1: ", tupla1.index(5))
tupla2.append('Bio')
print(tupla2)

#7
while True:
    numero = int(input("Ingrese un numero entre 0 y 255: "))
    
    if numero >=0 and numero <= 255:
        break
    elif numero < 0:
        print("El valor del numero es menor al rango requerido. ")
    elif numero >255:
        print("El valor del numero excede el rango requerido. ")
  



print(f"{numero}, en valor binario  ")
print(format(numero,'08b'))
print(" ")

print(f"{numero}, en valor hexadecimal")


hexadecimal = format(numero,'0x')
print(hexadecimal)


def decimal_a_octal(numero):
    octal = ""
    while numero > 0:
        residuo = numero % 8
        octal = str(residuo) + octal
        numero = int(numero / 8)
    print(octal)    
    return octal
    

print(" ")
print(f"{numero}, en valor octal")
decimal_a_octal(numero)

#8
f = [1,2,3,4,5,6] 
g = [4,5,6,7,8,9]

n = 0
j = 0
for x in range(len(f)):
   g.pop(n)
   g.insert(n, f[j])
   n +=2
   j +=2
   if n == 6 or j == 6:
     break

print(g)    



lista_f = [1,2,3,4,5,6] 
lista_g = [4,5,6,7,8,9]
lista_h = []

n = 0

for x in range(len(lista_f)):
    lista_h.append(lista_f[n])
    n +=1
    lista_h.append(lista_g[n])
    n +=1
    if n == 6:
        break
   

print(lista_h)    


    