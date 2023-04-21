

N=int(input("Ingrese un valor entero positivo: "))

Fact = 1

for i in range(1,N+1):
    Fact = Fact*i
print("El factorial de "+str(N),"es "+str(Fact))