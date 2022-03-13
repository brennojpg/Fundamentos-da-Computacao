mat = []

for i in range (0, 3):
   mat.append(0)
   mat[i] = []
   for j in range (0, 3):
      mat[i].append(input('digite um valor: '))

cont = 0
for i in range (0, 3):
   for j in range (0, 3):
      if mat[i][j] > 10:
         cont = cont +1

for i in range (0, 3):
   for j in range (0, 3):
      print mat[i][j],
   print

print cont
