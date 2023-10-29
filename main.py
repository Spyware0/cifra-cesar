from criptografia import *

verde = '\033[32;1m'
f = '\033[37;1m'
n = '\033[1m'


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
        if opcao == '0': break
        if not opcao in '120': continue
        try:
                base = int(input(f"Digite a base: (\033[33;1menter para padrão{f}) "))
        except:
                base = 3
        match opcao:
                case '1':
                        texto = input('Texto para criptografar: \033[4;1m').strip().lower()
                        print(f'\033[m{f}Seu texto: {verde}{crip(texto, lista, base)}{f}')
                case '2':
                        crip = input('Texto para descriptografar: \033[1;4m').strip().lower()
                        print(f'\033[m{f}Seu texto: {verde}{descrip(crip, lista, base)}{f}')
        continuar = input('Deseja voltar? [s/n] ').strip().lower()[0]
