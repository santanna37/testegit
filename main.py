import random

display_massages = [
    "seja feliz",
    "fique bem",
    "fique zen "
]

while True:
    resposta = input( "Deseja receber um conselho ? s/n:  ")
    if resposta == 's' or resposta =='S':
        menssagem = random.choice(display_massages)
        print(menssagem)
        print('===========')

