N= int(input("Digite el limite de numeros a leer: "))

Num_Pares= 0
Num_Impares= 0

for i in range(N):
    num = int(input(f"Digite el valor {i+1}: "))
    if num % 2 ==0:
        Num_Pares= Num_Pares + 1
    else:
        Num_Impares = Num_Impares + 1
print(f"La cantidad de pares es :"+str(Num_Pares))
print(f"La cantidad de impares es: "+str(Num_Impares))