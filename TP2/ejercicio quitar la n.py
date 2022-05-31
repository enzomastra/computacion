import csv

file = open("prueba.txt","w")
file.write("computacion")
file.close()

file = open("prueba.txt","a")
file.write("\nalumno")
file.close()

file = open("prueba.txt","r")
leo = csv.reader(file, delimiter = " ")
print(list(leo))