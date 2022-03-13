def criaV (vet):
     cont = 0
     cont2 = 0
     cont3 = 0
     for i in range (0, len(vet)):
          vet = raw_input ('Digite uma frase: ')
    
     for j in range (0, len(vet)):
          if vet[j] == 'a' or vet[j] == 'e' or vet[j] == 'i' or vet[j] == 'o' or vet[j] == 'u':
               cont = cont + 1
               
          elif vet[j] == ' ':
               cont2 = cont2 + 1
               
          else:
               cont3 = cont3 + 1
               
     print '\nQuantidade de vogais: ', cont
     print '\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
     print '\nQuantidade de espacos: ', cont2
     print '\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
     print '\nQuantidade de restos: ', cont3
     return cont, cont2, cont3

vet = [0]
criaV(vet)

