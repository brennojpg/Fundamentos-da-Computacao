def InvertVet (vet):
      for i in range(0, len(vet)):
            vet[i] =input('Numero: ')

      print'\nVetor original: ',vet
      print'\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='

      for j in range(0, len(vet)//2):
           aux = vet[j]
           vet[j] = vet[j+len(vet)//2]
           vet[j+len(vet)//2] = aux

      print'\nVetor trocado: ',vet


vet = [0]*16
InvertVet(vet)



