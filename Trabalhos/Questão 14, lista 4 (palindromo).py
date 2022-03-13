
def palin (vet):
     for i in range (0, len(vet)):
          vet[i] = raw_input('Digite uma palavra: ')
          palindromo = True

     for i in range (0, len(vet)//2):
          if vet[i] != vet[len(vet) - i - 1]:
               palindromo = False
               break

     if palindromo == True:
          print 'A palavra escolhida EH um PALINDROMO!'

     else:
          print 'A palavra escolhida NAO EH um PALINDROMO'

def leen (vet):
       if palindromo == True:
          vet[i] = vet[i].replace ('a', '4')
          vet[i] = vet[i].replace ('b', '6')
          vet[i] = vet[i].replace ('e', '3')
          vet[i] = vet[i].replace ('i', '1')
          vet[i] = vet[i].replace ('o', '0')
          vet[i] = vet[i].replace ('s', '5')

vet = []

palin(vet)
print vet
leen(vet)
print vet

          
          
          
