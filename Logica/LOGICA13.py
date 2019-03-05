def funcao(string):
    string = string.replace(',','.').replace(" ","")
    if len(string) == 0:
        return 0

    return int(float(string))

def main():
    a = raw_input()
    a = funcao(a)
    print a


if __name__ == "__main__":
    main()