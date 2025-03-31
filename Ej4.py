import re

def verification(contraseña):
    special = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~±§€£¥₹©®™¶∞√∑∫πΩΔΦ♦♥♪♫☀★☂♣♂♀"""
    contador = 0
    for letra in contraseña:
        if letra in special:
            contador += 1

    if len(contraseña) < 8:
        print('Contraseña invalida, debe tener minimo 8 caracteres')
    elif not any(c.isdigit() for c in contraseña):
        print("Contraseña invalida, debe contener un numero")
    elif not any(c.islower() for c in contraseña):
        print("Contraseña invalida, debe contener una minuscula")
    elif not any(c.isupper() for c in contraseña):
        print("Contraseña invalida, debe contener un mayuscula")
    elif contador != 0:
        print('Contraseña invalida, debe contener algun caracter especial')
    else:
        print('Contraseña Valida')

if __name__ == "__main__":
    print('Cree una contraseña')
    contraseña = input()

    verification(contraseña)