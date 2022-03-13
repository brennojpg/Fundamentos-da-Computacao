vetC = [0]*5
vetF = [0]*5
mediaC = 0
mediaF = 0
acima = 0
for i in range (0, len(vetC)):
     vetC[i] = float(input('Digite a temperatura em Celsius: '))
     vetF[i] = ((vetC[i]*9)/5)+32

for i in range (0, len(vetC)):
     mediaC = mediaC + vetC[i]
     mediaF = mediaF + vetF[i]

mediaC = mediaC/len(vetC)
mediaF = mediaF/len(vetF)

for i in range (0, len(vetF)):
     if vetF[i] > mediaF:
          acima = acima + 1
          

print'\nTemperaturas em Celsius: ', vetC

print'\nTemperaturas em Farenheit: ', vetF

print'\nA media em C: ', mediaC

print'\nA media em F: ', mediaF

print'\nA cima da media em F: ', acima
          
          
          
     
     

     
     
