def achar(string):
    lista = [')','}',']']
    lista2 = ['(','{','[']
    dicionario = {'(':')', '{':'}', '[':']'}

    flag = any( i in string for i in lista+lista2)
    while flag:
        menor = len(string) - 1
        for i in lista:
            aux = string.find(i)
            if aux == -1:
                aux = len(string) - 1
            
            menor = min(aux,menor)
        i = menor
        while i >= 0:
            if string[i] in lista2:
                if dicionario[string[i]] != string[menor]:
                    return False
                break
            i -= 1
        string = string[:i] + string[i+1:menor] + string[menor+1:]
        flag = any( i in string for i in lista+lista2)

    return True


def main():
    a = raw_input()
    if achar(a):
        print 'Valido'
    else:
        print 'Invalido'




if __name__ == "__main__":
    main()