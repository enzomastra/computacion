abrir=open("ejercicio4.txt","w")
abrir.writelines("primera\n""segunda\n""tercera\n""cuarta\n")
abrir.close()
class Lector:
    def __init__(self,archivo,accion):
        self.archivo=archivo
        self.accion=accion
    def leer(self):
        abrir=open(self.archivo,self.accion)
        return abrir.readlines()
        abrir.close()
    def enlistar(self):
        abrir=open(self.archivo, self.accion)
        lista=[]
        lista.append(abrir.readlines())
        print(lista)

prueba=Lector("ejercicio4.txt","r")
prueba.leer()
prueba.enlistar()
