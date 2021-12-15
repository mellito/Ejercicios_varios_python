# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

#para usar los metodos matematicos para calcular seno coseno y todos los valores debemos importar math
import math

def calculator(value,option):
    
    if option == 1:
        for x in range(1,value+1):
            print(f'el resultado de aplicar seno a {x} es: {math.sin(x)}')

    elif option == 2:
        for  x in range(1,value+1):
            print(f'el resultado de aplicar coseno a {x} es: {math.cos(x)}')
            
    elif option == 3:
        for x in range(1,value+1):
            print(f'el resultado de aplicar tangente a {x} es: {math.tan(x)}')
            
    elif option == 4:
        for x in range(1,value+1):
            print(f'el resultado de aplicar tangente a {x} es: {math.exp(x)}')

    elif option == 5:

        for x in range(1,value+1):
            print(f'el resultado de aplicar tangente a {x} es: {math.log(x)}')                         




def main():
    value=int(input("ingresa el valor a calcular: "))

    option=int(input(f'ingresa la funcion que deseas aplicarle a {value} ' """
    1 - seno
    2 - coseno
    3 - tangente
    4 - exponencial
    5 - logaritmo

    
    """))
    calculator(value,option)


if __name__=='__main__':
    main()