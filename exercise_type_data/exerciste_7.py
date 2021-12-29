# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

def imc_calcu(weight:float,height:float)->float:
    imc=weight/pow(height,2)
    return imc

def main():
    weight=float(input("Enter you weight (Kg): "))
    height=float(input("Enter your height (m): "))

    try:
        print(f'you imc is: {str(imc_calcu(weight,height))}')
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    main()