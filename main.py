import random
from messages import display_massages

print('say hello')
print('=====')


while True:
    resposta = input( "Deseja receber um conselho ? s/n:  ")
    if resposta == 's' or resposta =='S':
        menssagem = random.choice(display_massages)
        print(menssagem)
        print('===========')

