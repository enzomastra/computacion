abrir = open("ejercicio3.txt","w")
abrir.write("texto inicial")
abrir.close()
class Lector:
    def __init__(self,archivo,accion,texto):
        self.archivo = archivo
        self.accion = accion
        self.texto = texto
    def añadir (self):
        abrir = open(self.archivo,self.accion)
        abrir.write(" ")
        abrir.write(self.texto)
        abrir.close()
    def leer (self):
        abrir = open(self.archivo,"r")
        return abrir.readlines()
print("Añadir una linea")
print("Ingresa el texto que quieres añadir")
texto=input()
prueba = Lector("ejercicio1.txt","a",texto)
prueba.añadir()
print(prueba.leer())
