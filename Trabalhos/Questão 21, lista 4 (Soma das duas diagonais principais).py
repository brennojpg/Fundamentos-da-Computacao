#Funcao para criar matriz
def criaM (mat):
   for i in range (0, 3):
      mat.append(0)
      mat[i] = []
      for j in range (0, 3):
         mat[i].append(input('Insira os elementos da matriz: '))

#Funcao para printar        
def printM (mat):
   for i in range (0, 3):
      for j in range (0, 3):
         print'%4d' % mat[i][j],
      print

#Funcao para somar a diagonal principal
def somaDP (mat):
   soma = 0
   for i in range (0, 3):
      for j in range (0, 3):
         if i == j:
            soma = soma + mat[i][j]
   return soma

#Funcao para somar a diagonal secundaria
def somaDS (mat):
   soma1 = 0
   for i in range (0, 3):
      for j in range (0, 3):
         if i == j:
            soma1 = soma1 + mat[3 - i - 1][j]
   return soma1



mat = []
criaM(mat)
printM(mat)
print
resultDP= somaDP(mat)
resultDS = somaDS(mat)
print'\nA soma das diagonal pricipal eh:',resultDP,'e da secundaria eh:',resultDS,', respectivamente.'




         
