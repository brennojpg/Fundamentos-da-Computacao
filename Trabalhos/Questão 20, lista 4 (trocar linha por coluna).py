mat = []

for i in range (0, 4):
   mat.append(0)
   mat[i] = []
   for j in range (0, 4):
      mat[i].append(input('Digite um valor: '))

for i in range (0, 4):
   for j in range (0, 4):
      print'%4d' % mat[i][j],
   print

for i in range (0, 4): #Aqui onde ocorre a troca
      aux = mat[1][i]
      mat[1][i] = mat[i][3]
      mat[i][3] = aux

for i in range (0, 4):
   for j in range (0, 4):
      print'%4d' % mat[i][j],
   print
                    
