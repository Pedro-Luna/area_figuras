import os
from areas_figuras import *


def menu():

    #os.system('cls')
    print("1. Area de Cuadraro")
    print("2. Area de Rectangulo")
    print("3. Area de Romboide")
    print("4. Area de Rombo")
    print("5. Area de Triangulo")
    print("6. Area de poligono regular")
    print("7. Area de Circulo")
    

while True:
    
    menu()
    opcionMenu = int(input("inserta el numero de la operecione >> "))
    if opcionMenu ==1:
        l1 = float(input("Lado uno >> "))
        l2 = float(input("Lado dos >> "))
        A_cuadrado(l1,l2)
        
    elif opcionMenu == 2:
        l1 = float(input("L: "))
        l2 = float(input("a:  "))
        A_Rectagulo(l1,l2)

    elif opcionMenu == 3:
        b = float(input("Base: "))
        a = float(input("Altura:  "))
        A_Romboide(b,a)

    elif opcionMenu == 4:
        D = float(input("Diagonal: "))
        d = float(input("diagonal:  "))
        A_rombo(D,d)    

    elif opcionMenu == 5:
        b = float(input("Base: "))
        a = float(input("Altura:  "))
        A_triangulo(b,a)

    elif opcionMenu == 6:
        lado = float(input("lado : "))
        a = float(input("Apotema:  "))
        cant = float(input("Cantidad de lados: "))
        A_poligono_Regular(lado,a,cant)

    elif opcionMenu == 7:
        r = float(input("Radio: "))
        A_Circulo(r)
        break
    else:
        print("El numero que usted selecione no es valido... \n Intente de nuevo")
	    