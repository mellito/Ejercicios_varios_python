# Ejercicio 6
# Escribir un programa que lea un entero positivo,n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma= (n(n+1))/2



def main():
    try:
        
        number:int=int(input("type a number: "))

        if number>0:

            sum:int=(number*(number+1))/2
        else: 
            raise ("only positive number")

        print(f'the sum of the numbers from 1 to {number} is {sum} ')  

    except ValueError as ve:
        print(ve)           
    
       
        
        

if __name__ == '__main__':
    main()