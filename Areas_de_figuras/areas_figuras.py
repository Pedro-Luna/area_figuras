import math

def A_cuadrado( a=None, b=None):
    try:
        if a == None or b == None:
            print("Error, debes de dar los dos lados del cuadrado para el calculo")
        else:   
            area = a * b
            print("La area es: {} u^2" .format(area))
    except Exception as e:
        print(type(e).__name__)
       # print("error")

def A_Rectagulo( a=None, b=None):
    try:
        if a == None or b == None:
            print("Error, debes de dar los dos lados del rectugolo para el calculo")
        else:   
            area = a * b
            print("La area es: {} u^2" .format(area))
    except Exception as e:
        print(type(e).__name__)
       # print("error")

def A_Romboide(base=None,altura=None):
    try:
        if base == None or altura == None:
            print("Error, debes de dar los dos lados del Romboide para el calculo")
        else:   
            area = base * altura
            print("La area es: {} u^2" .format(area))
    except Exception as e:
        print(type(e).__name__)
       # print("error")

def A_rombo(D = None , d = None):
    try:
        if D== None or d == None :
            print("Las medidas de las diagonales debe ser posotivas")
        else:
            areaR = (D * d)/2
            print("La area es: {} u^2" .format(areaR))
    except Exception as e:
        print(type(e).__name__)

def A_triangulo(b = None, a = None):
    try:
        if b== None or a == None :
            print("Las medidas de los lados debe ser posotivas")
        else:
            areaT = (b * a)/2
            print("La area es: {} u^2" .format(areaT))
    except Exception as e:
        print(type(e).__name__)

def A_poligono_Regular(lado = None , a = None, cant_lados=None):
    try:
        if lado== None or a == None or cant_lados==None:
            print("Las medidas de los lados debe ser posotivas")
        else:
            perimetro = cant_lados * lado
            areaPR = (perimetro * a)/2
            print("La area es: {} u^2" .format(areaPR))
    except Exception as e:
        print(type(e).__name__)

def A_Circulo(r = None ):
    try:
        if r ==None :
            print("La medida del radio tiene que ser positiva")
        else:
            areaC = (math.pi* pow(r,2))
            print("La area es: {} u^2" .format(areaC))
    except Exception as e:
        print(type(e).__name__)      
