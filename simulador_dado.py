from re import S
import pyautogui as pg
import random

print('-'*100)
print('Olá, bem vindo ao simulador de jogar dado\nBasta confirmar quando quiser jogar e o sistema mostrar o valor que o dado caiu\nEntão vamos jogar??')
parar = input('Então vamos jogar? [S] sim / [N] não:  ')
print('-'*100)
lista_numeros = ['1','2','3','4','5','6']

while (parar == 'S')|(parar == 'sim')|(parar == 's')|(parar == 'Sim'):
    print('Jogando o dado...')
    pg.sleep(1)
    
    dado = random.choice(lista_numeros)
    if dado == '1':
        print(f'O dado caiu com o valor {dado}')
        print('Hmmm que pena você tirou um valor muito baixo')
        
    elif dado == '2':
        print(f'O dado caiu com o valor {dado}')
        print('Hmmm que pena você tirou um valor muito baixo')
        
    elif dado == '3':
        print(f'O dado caiu com o valor {dado}')
        print('Hmmm que pena você tirou um valor muito baixo')
        
    elif dado == '4':
        print(f'O dado caiu com o valor {dado}')
        print('Nem tão bom nem tão ruim HAHAHA!')
        
    elif dado == '5':
        print(f'O dado caiu com o valor {dado}')
        print('Um bom valor!!')
        
    elif dado == '6':
        print(f'O dado caiu com o valor {dado}')
        print('Catapimbas você tirou o valor mais alto')
        
    parar = input('Deseja jogar novamente? [S] sim / [N] não:  ')

print('Obrigado por ter jogado até a próxima')