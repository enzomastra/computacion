c1=100
c2=200
rango=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
def cerca_cien(num,rango):
    final=num-c1 in rango
    print(final)
def cerca_doscientos(num,rango):
    final=num-c2 in rango
    print(final)
print("Numero dentro de un rango")
print("Ingrese un numero:")
num=int(input())
print("Quieres averiguarlo en:")
print("¿Rango de 100 o 200?")
print("Introduce el numero elegido")
eleccion= int(input())
if eleccion == 100:
    cerca_cien(num,rango)
if eleccion == 200:
    cerca_doscientos(num,rango)