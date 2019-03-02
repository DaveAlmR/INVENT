def min(lista):
    if len(lista) == 0:
        return 0
    lista = lista.replace("[","").replace("]","").replace(" ","").split(',')
    while '' in lista:
        lista.remove("")

    ret = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] < ret:
            ret = lista[i]
        i += 1

    return int(ret)

def main():

    path = []
    a = raw_input()
    while len(a) != 0 and a[len(a) - 1] == ',':
        path.append(min(a))
        a = raw_input()
    path.append(min(a))

    dst = 0
    flag = False
    for i in path:
        if flag:
            print '+',i,
        else:
            print i,
            flag = True
        
        dst += i

    print '=',dst
    
    


if __name__ == "__main__":
    main()