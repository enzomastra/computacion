abrir=open("ejercicio10.txt","w")
abrir.write("primera\n segunda o no se\n tercera\n cuarta\n quinta")
abrir.close()
class Lector:
    def __init__(self,archivo,accion,expresion):
        self.archivo=archivo
        self.accion=accion
        self.expresion=expresion
    def lectorexpresion(self):
        abrir=open(self.archivo,self.accion)
        self.expresion= input("Introduzca una expresion para buscar: ")
        contenido=abrir.read()
        lineas=contenido.split("\n")
        for i in lineas:
            if self.expresion in i:
                final=i
                print(final)

prueba = Lector("ejercicio10.txt","r"," ")
prueba.lectorexpresion()