# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

def product_discount(price,discount):
    return price - price * discount/100

def product_iva(price,iva):
    return price + price * iva/100

def shop_car_calculation(diccionary,function):
    
    total=0
    for price,discount in diccionary.items():
        total += function(price,discount)
    return total


def main():
    
    print('El precio de la compra tras aplicar los descuentos es: ', shop_car_calculation({1000:20, 500:10, 100:1}, product_discount))
    print('El precio de la compra tras aplicar el IVA es: ', shop_car_calculation({1000:20, 500:10, 100:1}, product_iva))

    


if __name__=='__main__':
    main()