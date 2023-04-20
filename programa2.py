#Caso 1
rta = "Salida = l"
for i in [1, 2, 3, 4,5 , 6, 7, 8, 9, 10]:
    rta=rta +str(i)+", "
rta=rta + "l"
print(rta)

#Caso 2
for i in [1, 2, 3, 4,5 , 6, 7, 8, 9, 10]:
    print("UIS NO ES UNA....")
    
#Caso 3
rta = "Salida = l"
for numero in [1, 2, 3, 4,5 , 6, 7, 8, 9, 10]:
    rta=rta +str(numero)+", "
rta=rta + "l"
print(rta)

#Caso 4 
rta = "Salida = l"
for numero in range (1, 11):
    rta=rta +str(numero)+ ", "
rta = rta + "i"
print(rta)

#caso 5
rta = "salida = l"
for numero in "UIS NO ES UNO":
    rta = rta +str (numero + ", ")
rta=rta + "l"
print(rta)

#caso 6
suma=0
for numero in range (1, 11):
    suma=suma+1
print(f"la suma es {suma}")

#Caso 7
frase=input("digite una frase: ")
vocales= "aeiouAEIOU"
numero_vocales=0
for i in frase:
    if i in vocales:
        numero_vocales=numero_vocales+1
print(f"en la frase hay  {numero_vocales}vocales")
