numero = int (input('Digite um número: '))
fat = 1


fat = int(fat)

for i in range(1, numero +1): 
    fat *=   i

print(f' Fatorial de {numero} é igual a: {fat}')

'''def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Exemplo de uso
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")'''
