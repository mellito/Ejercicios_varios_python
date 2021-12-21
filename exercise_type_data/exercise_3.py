# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.



def main():
    name:str=input("Cual es tu nombre: ")
    try:
        if name.isalpha():
            print(f'Hola {name}')
        else:    
            raise ValueError("solo se permiten caracteres ")    
        

    except ValueError as ve:
        print(ve)

if __name__=='__main__':
    main()