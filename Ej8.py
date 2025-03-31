import random

def pasword(large):
    special = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~±§€£¥₹©®™¶∞√∑∫πΩΔΦ♦♥♪♫☀★☂♣♂♀"
    mayus = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    minus = 'abcdefghijklmnñopqrstuvwxyz'
    number = '0123456789'
    pasword = []
    index = 0
    while (index < large):
        randomValue  = random.randrange(1, 5)
        if (randomValue == 1):
            indexRandom = random.randrange(0, 26)
            pasword.append(mayus[indexRandom])
            index += 1
        elif (randomValue == 2):
            indexRandom = random.randrange(0, 26)
            pasword.append(minus[indexRandom])
            index += 1
        elif (randomValue == 3):
            indexRandom = random.randrange(0, 60)
            pasword.append(special[indexRandom])
            index += 1
        else:
            indexRandom = random.randrange(0, 10)
            pasword.append(number[indexRandom])
            index += 1
    resultado = ''.join(pasword)
    print(resultado)
if __name__ == "__main__":
    print('Creador de contraseñas')
    print('Ingrese el numero de caracteres de la contraseña')
    large = int(input())
    
    pasword(large)