from multi import NumMulti

while True:
    num = int(input('Digite um número natural: '))
    if num < 0:
        print('Por favor digite um número natural!')
        continue
    else:
        print(NumMulti(num))
        break
