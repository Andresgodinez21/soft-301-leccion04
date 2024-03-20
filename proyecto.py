print("Bienvenido al sistema de pago de la POPS")

HV = float(600) #Helados de Vainilla
HC = float(700) #Helados de Chocolate
B = float(1200) #Batidos

c1=int(input("Ingrese cuantos Helados de Vainilla desea , costo de Helado 600 : "))
c2=int(input("Ingrese cuantos Helados de Chocolate desea, costo de Helado 700 : "))
c3=int(input("Ingrese cuantos Batidos desea,  costo de Batido 1200 : "))

HV = HV * c1 
HC = HC * c2
B = B * c3
SUM = float(HV + HC + B)
DESC = float(SUM*0.15) 

PVP = input("Tiene tarjeta Pops, digite S si la tiene ó N si no : ")
if PVP == "S":
    TOT = SUM - DESC
else:
    TOT = SUM

print("Helados Vainilla total : " + str(HV))
print("Helados Chocolate total : " + str(HC))
print("Batidos total : " + str(B))
if PVP == "S":
    print("Descuento tarjeta POPS 15% : " + str(DESC))
else:
    print("No tiene tarjeta Pops no aplica descuento ")
print("El total de su factura es  : " + str(TOT))
            