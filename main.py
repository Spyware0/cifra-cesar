from criptografia import *
from colorama import Fore, Style

verde = Fore.GREEN + Style.BRIGHT
f = Style.RESET_ALL + Style.BRIGHT
n = Style.BRIGHT
estilo_resposta = Style.BRIGHT + '\033[4m'


banner = f'''{verde}   ______   _    ____
  / ____/  (_)  / __/  _____   ____ _
 / /      / /  / /_   / ___/  / __ `/
/ /___   / /  / __/  / /     / /_/ /
\____/  /_/  /_/    /_/      \__,_/{f}'''


continuar = 's'
while continuar == 's':
    print('\x1b[2J\x1b[1;1H')
    print(banner)

    try:
        opcao = input(f'\n{n}[ {verde}1{f} ] > {verde}Criptografar{f}\n[ {verde}2{f} ] > {verde}Descriptografar{f}\n\n[ {verde}0{f} ] {verde}Sair\n\n>>>{f} ').strip()[0]
    except:
        continue

    if opcao == '0':
        break

    if not opcao in '120':
        continue

    try:
        base = int(input(f"Digite a base: (\033[33;1menter para padrão{f}) "))
    except:
        base = 3

    match opcao:
        case '1':
            texto = input(f'Texto para criptografar: {estilo_resposta}').strip().lower()
            print(f'\033[m{f}Seu texto: {verde}{crip(texto, lista, base)}{f}')
        case '2':
            crip = input(f'Texto para descriptografar: {estilo_resposta}').strip().lower()
            print(f'\033[m{f}Seu texto: {verde}{descrip(crip, lista, base)}{f}')

    continuar = input('Deseja voltar? [s/n] ').strip().lower()[0]
