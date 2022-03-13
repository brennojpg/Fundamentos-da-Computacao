def media(vet):
     soma = 0
     cont = 0
     meh = 0
     for i in range (0, 10):
          nota = float(input('Insira a nota: '))
          vet[i] = nota
          soma = soma + vet[i]
     media = soma/8
     print'\nA media eh: ', media
     cont = 0

     for j in range (0, 10):
          if vet[j] > media:
               cont = cont + 1
     print'\nAlunos acima da media: ', cont

     for k in range (0, 10):
          if vet[k] == media:
               meh = meh + 1
     print'\nAlunos na media: ', meh
     return soma, cont, meh


vet = [0]*10


media(vet)
