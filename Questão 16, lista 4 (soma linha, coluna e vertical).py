mat = []

for i in range (0, 7):
   mat.append(0)
   mat[i] = []
   for j in range (0, 7):
      mat[i].append(input('Insira os valores da matriz :'))

soma = 0
soma2 = 0
soma3 = 0
par = 0
for i in range (0, 7):
   for j in range (0, 7):
      if i == 6:
        soma = soma + mat[i][j]

      if j == 2:
         soma2 = soma2 + mat[i][j]

      if i == j:
         soma3 = soma3 + mat[i][j]

      if mat[i][j] % 2 == 0:
         par = par + mat[i][j]

for i in range (0, 7):
   for k in range (0, 7):
      print mat[i][k],
   print

print'\nSoma linha 0: ', soma

print'\nSoma coluna 2: ', soma2

print'\nSoma da diagonal principal: ', soma3

print'\nElemento linha 1 coluna 2: ', mat[3][4]

print'\nElementos pares da matriz:', par
      
         
        
   
   
