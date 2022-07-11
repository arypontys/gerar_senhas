# Gerador de senhas
from random import choices, shuffle
from string import ascii_letters, digits, punctuation


def gerar_senha(quant_letras, quant_numeros, quant_simbolos):
    '''
    Gerar senhas aleatórias com a quantidade de caracteres passada.

    quant_letras: argumento com quantidades de letras para ser randomizadas
    quant_numeros: argumento com quantidades de números para ser randomizados
    quant_simbolos: argumento com quantidades de símbolos para ser randomizados
    lista senha: variável que recebe os caracteres ramdomizados na sequencia das variáveis dispostas
    senha: variável que recebe os caracteres já tratados e aleatorios.
    '''

    lista_senha =[]
    senha = []
        
    for caracter in range(0, quant_letras):
        lista_senha.append(choices(ascii_letters))
    for caracter in range(0, quant_numeros):
        lista_senha.append(choices(digits))
    for caracter in range(0, quant_simbolos):
        lista_senha.append(choices(punctuation))
    
    shuffle(lista_senha)
    for caracter in lista_senha:
        for i in caracter:
            senha.append(i)
        
        a  = ''.join(senha)

    print(a)


quant_letras = int(input('Quantidade de caracteres: '))
quant_numeros = int(input('Quantidade de números: '))
quant_simbolos = int(input('Quantidade de símbolos: '))

gerar_senha(quant_letras,quant_numeros,quant_simbolos)