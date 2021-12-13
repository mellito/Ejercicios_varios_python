# Implementar un menú de aplicación con las siguientes opciones:
# [1] – Importar palabras clave
# [2] – Mostrar palabras clave
# [0] – Salir
# Implementar una función carga_keywords() que lea un fichero llamado keywords.txt:
# El fichero tendrá una(s) palabra(s) clave por línea.
# No hay que separar las palabras clave con ningún carácter, solo enter.
# El fichero se leerá línea a línea, guardando la palabra clave correspondiente como un nuevo elemento de una lista.
# La función devolverá una lista de palabras clave.
# Cuando se introduzca la opción de menú [1], se invocará a la función carga_keywords(). La lista resultante se asignará a una variable del programa llamada keywords.
# Cuando se introduzca la opción de menú [2], se mostrará el listado de palabras clave de 20 en 20, es decir, una vez mostradas 20 palabras clave, el usuario deberá pulsar la tecla enter para ver las siguientes.
# Cuando se introduzca la opción de menú [0], el programa finalizará.
from typing import Optional


def muestra_menu():
    print("""
    [1] importa palabra clave
    [2] motrar palabra clave
    [0] salir
    """)

def carga_keywords():
    keywords=[]

    try:
        with open("./menu_wranking/keywords.txt","r",encoding="utf-8") as f:
            for line in f:
                line=line.strip("\n")
                keywords.append(line)

    except FileNotFoundError:

        print("nose encuentra el fichero keywors.txt")    

    return keywords 

def mostrar_keyword(keywords):
    contador=0
    for kword in keywords:
        print(kword)
        contador +=1
        if contador ==20:
            contador=0
            input("mostrar mas")


def main():
    c_word=[]
    while True:
        muestra_menu()
        opcion=int(input("    selecciona una opcion: "))
        if opcion == 0:
            break
        elif opcion == 1:
            c_word=carga_keywords()
        elif opcion == 2:
            mostrar_keyword(c_word)    
        else: 
            print("opcion no valida")    

if __name__=='__main__':
    main()