# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.


def main():
    work_hour:int=int(input("how many hours you work: "))
    cost_hour:float=float(input("how much is the cost per hour: "))
    try:
        if isinstance(work_hour,int) and isinstance(cost_hour,float):
            print(f'you pay today for {work_hour} hours whit a cost of {cost_hour} is: {work_hour*cost_hour}')
         
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    main()