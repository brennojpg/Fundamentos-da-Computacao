def criaV (vet):
     for i in range (0, len(vet)):
          vet[i] = input('Insira numeros aqui: ')

def par (vet):
     cont = 0
     for i in range (0, len(vet)):
          if vet[i] % 2 == 0:
               cont = cont + 1
     print'\nAquantidade de numeros pares no vetor eh de: ', cont
     return cont

vet  = [0]*10
criaV(vet)
par(vet)
