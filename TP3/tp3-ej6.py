from itertools import islice
abrir=open("ejercicio6.txt","w")
lines=["primera","segunda","tercera","cuarta","quinta"]
abrir.writelines("\n".join(lines))
abrir.close()
class Lectorn:
    def __init__(self,archivo,accion,n):
        self.archivo=archivo
        self.accion=accion
        self.n=n
    def lecturan(self):
        abrir = open(self.archivo,self.accion)
        for i in islice(abrir,self.n):
            print(i)

print("lector de n lineas")
print("El texto tiene 5 lineas, ¿hasta que linea queres leer?")
n=int(input())
prueba=Lectorn("ejercicio6.txt","r",n)
print(prueba.lecturan())