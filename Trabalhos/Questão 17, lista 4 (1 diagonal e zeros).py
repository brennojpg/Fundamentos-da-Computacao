mat = []

for i in range (0, 5):
   mat.append(0)
   mat[i] = []
   for j in range (0, 5):
      mat[i].append(0)


for i in range (0, 5): #for i in range (0, 5): mat[i][i] = 1
   for j in range (0,5):
      if i == j:
         mat[i][j] = 1
         
for i in range (0, 5):
   for j in range (0, 5):
      print mat,
   print
         
      
