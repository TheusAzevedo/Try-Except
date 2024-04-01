#Erros
#Excelente para teste
#Não realiza o 'Stop' no programa
#mensagens customizadas quando encontra um erro

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar somente numeros!')


print('mais codigo abaixo')
