def secuence(number):
    list = [0,1]
    n1 = 0
    n2 = 1
    for i in range(number):
        value = n1 + n2
        list.append(value)
        n1 = list[n1 + 1]
        n2 = list[n2 + 1]
    print(list)



if __name__ == "__main__":
    print('Ingrese un numero entero positivo')
    number = int(input())

    secuence(number)