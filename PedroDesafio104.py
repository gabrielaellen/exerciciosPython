def leiaint(a):
    while True:
        a = int(input('Digite um número '))
        if type(a) != int:
            print('Apenas numeros inteiros!')
            continue
        

n = leiaint('Digite seu número')
print(n)