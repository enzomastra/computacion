abrir = open("ejercicio1.txt","w")
abrir.write("Lo lograste")
abrir.close()
class Lector:
    def __init__(self,archivo,accion):
        self.archivo = archivo
        self.accion = accion
    def leer (self):
        abrir = open(self.archivo,self.accion)
        return abrir.readlines()
prueba = Lector("ejercicio1.txt","r")
print(prueba.leer())