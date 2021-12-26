# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

def calcinterest(money_invest:float,anual_interest:float,years:int)->float:

    result=money_invest*(anual_interest/100+1)**years
    return result




def main():
    money_invest=float(input("how much wana invest in our proyect: "))
    anual_interest=float(input("digit the anual interest of you money in porcentege: "))
    years=int(input("how many year want invest you money: "))

    print(f'The capital obtine for you invest is : {calcinterest(money_invest,anual_interest,years)}')




if __name__ == '__main__':
    main()