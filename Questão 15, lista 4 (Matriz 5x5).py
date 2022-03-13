mat = []

for i in range (0, 5):
   mat.append(0)
   mat[i] = []
   for j in range (0, 5):
      mat[i].append(input('insira os valores da matriz: '))

aux = 0
for i in range (0, len(mat)):
   for j in range (0, len(mat)):
      if mat[i][j] > aux:
         aux = mat[i][j]
         linha = i
         coluna = j

for i in range (0, len(mat)):
   for j in range (0, len(mat)):
      print mat[i][j],
   print

print'\nMaior elemento: ', aux

print linha, coluna
      
      
                    
