def poten(numero):
    if numero == 1:
        return 1
    else:
        if(numero%2==0):
            return numero+poten(numero/2)
        else:
            return -1
        
if __name__ == "__main__":
    x=int(input("Digite um numero: "))
    if ((poten(x)+1)/2==x):
        print("O numero {} pode ser escrito como potencia de 2.".format(x))
    else:
        print("O numero {} nao pode ser escrito como potencia de 2".format(x))