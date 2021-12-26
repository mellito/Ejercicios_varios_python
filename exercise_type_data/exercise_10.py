# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


def calc_weight(clows:int,dolls:int)->int:

    result = (clows*112) + (dolls*75)
    return result


def main():
    clows=int(input("how many clows you going to send: "))
    dolls=int(input("how many dolls you going to send: "))

    print(f'total weight to send is: {calc_weight(clows,dolls)} g')

if __name__ == '__main__':
    main()