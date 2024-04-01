#Erros
#Excelente para teste
#Não realiza o 'Stop' no programa
#mensagens customizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existente')