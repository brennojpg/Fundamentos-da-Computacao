

def criaF (vet):
     for i in range (0, len(vet)):
          vet[i] = input('Insira os elementos do primeiro vetor: ')
     print vet
     print'\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='

def somaV (vet, vet1):
     soma = 0
     for i in range (0, len(vet)):
          soma = soma + vet[i] + vet1[i]              
     print'\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
     print'\nSoma dos vetores: ', soma
     return soma

vet1 = [0]*5
vet2 = [0]*5

criaF(vet1)
criaF(vet2)
somaV(vet1, vet2)

          
          
