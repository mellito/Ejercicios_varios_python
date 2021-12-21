# Ejercicio 6
# Escribir un programa que lea un entero positivo,n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma= (n(n+1))/2



def main():
    number:int=int(input("type a number: "))
    sum:int=lambda number: (number*(number+1))/2
    total:int
    for i in range(1, number+ 1):
        total=sum(i)

    print(f'the sum of the numbers from 1 to {number} is {total} ')    
        
        

if __name__ == '__main__':
    main()