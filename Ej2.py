def convertir(temp):
    tempF = (temp * 9/5) + 32
    print(f'La convercion de {temp} Celsius a Fahrenheit es {tempF} Fahrenheit')
if __name__ == "__main__":
    print('Ingrese una temperatura para pasar de Celsios a Fahrenheit')
    temp = float(input())
    convertir(temp)

