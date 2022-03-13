def letra():
    x = raw_input('Informe: ')
    y = raw_input('Informe: ')
    if len(x) > len(y):
        aux = x
    else:
        aux = y

    if aux == x:
         for i in range(0,len(x)):
              ind = 0
              aux2 = ''
              if x[i] == y[0]:
                   ind = i
                   aux3 = i
                   for j in range(0,len(y)):
                        if y[j] != x[ind]:
                              break
                    else:
                         aux2 += x[ind]
                         ind += 1
                    if aux2 == y:
                         print y, ' eh um segmento de ', x
                         print 'indice ', aux3
                         exit()


     else:
          for i in range(0,len(y)):
               ind = 0
               aux2 = ''

            if y[i] == x[0]:
                ind = i
                aux3 = i

                for j in range(0,len(x)):
                    if x[j] != y[ind]:
                        break
                    else:
                        aux2 += y[ind]
                        ind += 1
                if aux2 == x:
                    print y,' eh um segmento de ', x
                    print 'indice ', aux3
                    exit()
     if aux2 != x and aux2 != y:
            print 'segmento inexistente'
            print 'indice: -1'

letra()
