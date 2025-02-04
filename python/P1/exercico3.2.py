qtd = 0
for i in range(1, 11):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        qtd = qtd + 1

print(f'Foram digitados {qtd} números pares')