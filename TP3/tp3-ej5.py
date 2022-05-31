import shutil
abrir=open("ejercicio5.txt","w")
abrir.writelines("copiar y pegar en otro archivo")
abrir.close()
class Lectorn:
    def __init__(self,archivo,accion,archivo1,accion1):
        self.archivo=archivo
        self.accion=accion
        self.archivo1=archivo1
        self.accion1=accion1
    def copiarypegar(self):
        with open(self.archivo,self.accion) as abrir:
            with open(self.archivo1,self.accion1) as abrir1:
                shutil.copyfileobj(abrir,abrir1)
                print("Archivo copiado y pegado")
prueba=Lectorn("ejercicio5.txt","r","ejercicio5parte2","w")
prueba.copiarypegar()
