vet1 = [0]3
vet2 = [0]3
vetU = [0]6
vetI = [0]6

for i in range (0, len(vet1)):
     vet1[i] = input('Digite os elementos do primeiro vetor: ')

for i in range (0, len(vet2)):
     vet2[i] = input('Digite os elementos do segundo vetor: ')

for i in range (0, len(vet1)):
     if vet1[i] not in vetU:
          vetU[i] = vet1[i]

indice = 3
for i in range (0, len(vet2)):
     if vet2[i] not in vetU:
          vetU[indice] = vet2[i]
          indice = indice + 1

indice = 0
for i in range (0, len(vet1)):
     for j in range (0, len(vet2)):
          if vet1[i] == vet2[j]:
               vetI[indice] = vet1[i]
               indice = indice + 1

print'\nVetor 1: ', vet1
print'\nVetor 2: ', vet2
print'\n Uniao: ', vetU
print'nIntercessao: ', vetI



     

     
