# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
import os 

def add_curso(list:list)->list:

    curso=input("ingresar un nuevo curso: ")
    list.append(curso)

    return list    

    
def opcion():
        
    option=int(input("""
    deseas agregar un curso
    1 - si
    2 - no
    """))

    return option 

  

def main():

    curso_list=[]
    counter = 0   
        
    while True:
        result=opcion() 

        try:
                       
            if result !=1 and result !=2:
                raise ValueError("  opion no valida")
                
            os.system("clear")

            print(f' se han ingresado {counter} cursos') 
                          
            if result ==1:
                add_curso(curso_list)
                counter+=1

            elif result ==2:
                break

        except ValueError as ve:
            print(ve)    
            

    os.system("clear")
    print(f' Lista de curos {curso_list}')       
              


   



if __name__ == '__main__':
    main()


