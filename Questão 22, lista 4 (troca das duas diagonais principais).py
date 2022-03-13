#Funcao pra criar a matriz
def criaM (mat):
   for i in range (0, 4):
      mat.append(0)
      mat[i] = []
      for j in range (0, 4):
         mat[i].append(input('Digite os elementos da matriz: ')) 
#Funcao pra impimir a matriz
def printMat (mat): 
   for i in range (0, 4):
      for j in range (0, 4):
         print'%4d' % mat[i][j],
      print
#Funcao de
def trocaD (mat):
   for i in range (0, 4):
      aux = mat[i][i]
      mat[i][i] = mat[4 - i - 1][i]
      mat[4 - i - 1][i] = aux
  


            
mat = []
criaM(mat)
printMat(mat)
print'=-'*50
trocaD(mat)
printMat(mat)

