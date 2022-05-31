abrir=open("ejercicio9.txt","w")
abrir.write("primera segunda\n tercera cuarta\n quinta")
abrir.close()
class Lector:
    def __init__(self,archivo,accion):
        self.archivo=archivo
        self.accion=accion
    def lineaspalabrascaracteres(self):
        abrir=open(self.archivo,self.accion)
        lineas=0
        caracteres=0
        contenido=abrir.read()
        lista=contenido.split("\n")
        for i in lista:
            if i:
                lineas=lineas+1
        parapalabras=contenido.split()
        palabras=len(parapalabras)
        caracteres=len(contenido)
        print("el texto tiene ",lineas," lineas, ",palabras," palabras y ",caracteres," caracteres")

prueba = Lector("ejercicio9.txt","r")
prueba.lineaspalabrascaracteres()