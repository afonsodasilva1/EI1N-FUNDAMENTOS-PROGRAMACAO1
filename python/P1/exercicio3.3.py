soma = 0
for i in range(0, 101):
    if i != 0:
        if  i % 2 != 0:
            soma = soma + 1

print(f'A soma dos números pares é igual a:  {soma}')