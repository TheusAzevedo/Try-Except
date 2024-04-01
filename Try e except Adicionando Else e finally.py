#Erros
#Excelente para teste
#Não realiza o 'Stop' no programa
#mensagens customizadas quando encontra um erro

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar somente numeros!')
finally:
    print('Codigo ok')

'''else:
    print('Usario digitou um valor correto')
    resultado = valor * 2
    print(resultado)'''

print('mais codigo abaixo')

