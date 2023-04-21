
#¿Cuantos multiplos por 7 y por 9 hay en el rango de (1000,5000)

Mult_7=0
Mult_9=0

for i in range (1000,5000):
    if i % 7 ==0:
        Mult_7= Mult_7+1
    if i % 9 == 0:
        Mult_9= Mult_9+1
print("Hay: "+str(Mult_7), "Multiplos de 7")
print("Hay: "+str(Mult_9), "Multiplos de 9")