from Cliente import*
from Libro import*

def showclients():
    print("Lista de clientes")
    print(names)
def showbooks():
    print("Lista de libros:")
    print(books)
def assing():
    print("Ingrese el nombre del cliente al cual le asignara un libro:")
    client=input()
    print("Ingrese el nombre del libro:")
    book = input()
    print("A ",client," se le ha asignado el libro: ",book)