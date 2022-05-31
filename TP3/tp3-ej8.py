abrir=open("ejercicio8.txt","w")
abrir.write("primera segunda tercera cuarta quinta")
abrir.close()
class Lector:
    def __init__(self,archivo,accion,delimitador):
        self.archivo=archivo
        self.accion=accion
        self.delimitador=delimitador
    def leerdelimitar(self):
        abrir=open(self.archivo,self.accion)
        lector=abrir.readlines()
        string=" ".join(lector)
        dividir=string.split(" ")
        self.delimitador = input("Introduce un delimitador: ")
        dividido=self.delimitador.join(dividir)
        print(dividido)
prueba=Lector("ejercicio8.txt","r"," ")
prueba.leerdelimitar()