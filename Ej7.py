def calcular(precio,descuento):
    descuento = precio * (porcentaje / 100)
    total = precio - descuento
    print(f'El precio total es de {total}')

if __name__ == "__main__":
    print('Ingrese el precio')
    precio = float(input())
    print('Ingrese el de cuanto es el porcentaje deldescuento')
    porcentaje = float(input())

    calcular(precio, porcentaje)