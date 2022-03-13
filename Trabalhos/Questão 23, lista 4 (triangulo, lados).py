def criaM (mat):
   for i in range (0, 10):
      mat.append(0)
      mat[i] = []
      for j in range (0, 3):
         mat[i].append(input('Insira os elementos da matriz: '))

def printM (mat):
   for i in range (0, 10):
      for j in range (0, 3):
         print'%4d' % mat[i][j],
      print

def soma (mat):
   soma = 0
   vet = [0]*10
   for i in range (0, 10):
      for j in range (0, 3):
         soma = soma + mat[i][j]
         vet[i] = soma
   return soma, vet 

      
mat = []

criaM(mat)
printM(mat)
print
print soma(mat)
