def criaF (vet):
     for i in range(0, len(vet)):
          vet[i] = input('Insira os elementos desse vetor: ')

     print'\n', vet



vet1 = [0]*5
vet2 = [0]*5
vet3 = [0]*10

criaF(vet1)
print
criaF(vet2)
print
vet3 = vet1 + vet2
print vet3
