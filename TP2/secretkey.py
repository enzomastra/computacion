import os
import re
list = os.listdir("C:/Users/mastr/OneDrive/Escritorio/apuntes/computacion/SecretKey")
for i in range(len(list)):
    nom = list[i]
    nonumero = re.sub("[0-9]+","",nom)
    print(nonumero)