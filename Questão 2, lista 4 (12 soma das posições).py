def lerVet (vet):
    soma = 0
    for i in range (0, len(vet)):
        vet[i] = input('Insira um numero: ')

    a = input('Insira um numero de 1 a 12: ')
    b = input('Insira um numero de 1 a 12: ')

    for i in range (0, len(vet)):
        if i == a:
            aux = vet[i]

    for j in range (0, len(vet)):
        if j == b:
            aux2 = vet[j]

    soma = aux + aux2
    print'\n', soma
    return soma


vet = [0]*12
lerVet(vet)
     


