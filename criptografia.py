from string import ascii_lowercase
try:
    from unidecode import unidecode
except:
    from os import system
    system('pip install unidecode')
finally:
    from unidecode import unidecode

lista = ascii_lowercase

def crip(text='', letras='', base=3):
    text = unidecode(text.strip().lower())
    crip = str()

    for i in text:
        if not i in letras and i != ' ':
            continue
        try:
            crip += i if i == ' ' else letras[letras.index(i) + base]
        except:
            crip += letras[(letras.index(i) + base) - 26]

    return crip


def descrip(crip='', letras='', base=3):
    crip = crip.strip().lower()
    texto = str()

    for i in crip:
            texto += i if i == ' ' else letras[letras.index(i) - base]

    return texto

