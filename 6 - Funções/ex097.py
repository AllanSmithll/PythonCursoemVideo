# 08/11/2022
'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''

def escreva(txt) -> str:
    if len(txt) == 0: return None
    else:
        if len(txt) == 1:
            print('~~~')
            print(txt)
            print('~~~'*len(txt))
        elif len(txt) > 1:
            print('~~~'*(len(txt) // 2))
            print(txt)
            print('~~~'*(len(txt) // 2))

# Programa principal
texto = input("Palavra para formatarmos bonitinho: ")
print(escreva(texto))
