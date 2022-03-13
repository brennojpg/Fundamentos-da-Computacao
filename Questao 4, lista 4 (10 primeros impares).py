def criarV (vet):
     for i in range (0, len(vet)):
          vet[i] = input('insira os 10 primeiros numeros impares positivos aqui: ')

     if vet[i] % 2 == 0:
          print'\n ERRO! Algum numero nao eh impar!'

     else:          
          print'\nOs 10 primeiros numeros impares positivos sao: ', vet


vet = [0]*10
criarV(vet)

