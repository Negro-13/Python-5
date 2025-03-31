import random

def adivina(number):
    randomN = random.randrange(1, 100)
    while True:
        if number < randomN:
            print('El numero es mayor')
            number = int(input())
        elif number > randomN:
            print('El numero es menor')
            number = int(input())
        else:
            print('Adivinaste')
            break

if __name__ == "__main__":
    print('Intente adivinar el numero entre 1 y 100')
    number = int(input())
    adivina(number)
