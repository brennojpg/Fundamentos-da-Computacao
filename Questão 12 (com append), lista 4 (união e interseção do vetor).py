vet = [0]*10
vet2 = [0]*10

vetU = []
vetI = []

for i in range(0,len(vet)):
    vet[i] =  input('insira um valor: ')

print

for i in range(0,len(vet2)):
    vet2[i] =  input('insira um valor: ')

for i in range(0,len(vet)):
    for j in range(0,len(vet2)):
        if vet[i] == vet2[j] and vet[i] not in vetI:
            vetI.append(vet[i])

for i in range(0,len(vet)):
    if vet[i] not in vetU:
            vetU.append(vet[i])

for i in range(0,len(vet2)):
    if vet2[i] not in vetU:
            vetU.append(vet2[i])
        
print vetU
print vetI
               



     

     
