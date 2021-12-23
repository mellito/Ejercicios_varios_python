# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# this metod calculate the quotient of 2 numbers
def quotient(num1:int,num2:int):
    return num1//num2

# this metos calculate the rest of 2 numbers
def rest(num1:int,num2:int):
    return num1%num2


def main():
    number1=int(input("Digit the first number: "))
    number2=int(input("Digit the second number: "))

    print (f' number {number1} and {number2} have a quotient of {quotient(number1,number2)} and a rest of {rest(number1,number2)}')


if __name__ == '__main__':
    main()