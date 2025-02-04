'''2.2.	Escreva um programa para ler 2 valores reais e uma das seguintes operações a serem executadas (codificada da seguinte forma: 1.Adição, 2.Subtração, 3.Multiplicação , 4.Divisão). Calcular e escrever o resultado dessa operação sobre os dois valores lidos.
 Observação: Considere que só serão lidos os valores 1, 2, 3 ou 4.'''


num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
operacao = int(input('Digite a operação a ser realizada: '))


if operacao >=1 & operacao <= 4:
    if operacao == 1:
        print(num1 ,' + ', num2, ' = ', num1 + num2)
    elif operacao == 2:
        print(num1 ,' - ', num2, ' = ', num1 - num2)
    elif operacao == 3:
        print(num1 ,' * ', num2, ' = ', num1 * num2)
    elif operacao == 4:
        print(num1 ,' / ', num2, ' = ', num1 / num2)
else:
    print('Só podem ser digitados valores de 1 a 4')
