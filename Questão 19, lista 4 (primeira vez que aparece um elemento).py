mat = []

for i in range (0, 3):
   mat.append(0)
   mat[i] = []
   for j in range (0, 3):
      mat[i].append(input('digite um valor: '))

x = input('Insira um numero para procurar na matriz: ')

teste = False
for i in range (0, 3):
   for j in range (0, 3):
      if x == mat[i][j]:
         first = mat[i][j]   
         linha =  i           #Apenas a linha
         coluna = j        #Apenas a coluna
         teste = True

if teste == False:
   print'\nERRO'

else:        
   for i in range (0, 3):
      for j in range (0, 3):
         print'%3d'%mat[i][j],
         
      print


   print'\n elemento: ',first,'linha: ', linha,'coluna: ',coluna






         
      
