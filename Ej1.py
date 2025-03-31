def calcular (peso,altura):
    imc = peso / (altura * altura)
    if imc < 18.5:
        print(f'Tu IMC es de {imc}, tu talla el S')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'Tu IMC es de {imc}, tu talla el M')
    elif imc >= 25 and imc <= 29.9:
        print(f'Tu IMC es de {imc}, tu talla el L')
    else:
        print(f'Tu IMC es de {imc}, tu talla el XL')

if __name__ == "__main__":
    print('Ingrese su peso en kg')
    peso = float(input())
    print('Ingrese su altura en metros')
    altura = float(input())

    calcular(peso,altura)