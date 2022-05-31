from Library import*

import os

def menu():
    print("Biblioteca")
    print("Selecciona una opcion mediante un numero:")
    os.system("cls")
    print("1. Ingresar Libro")
    print("2. Ingresar Cliente")
    print("3. Mostrar libros")
    print("4. Mostrar informacion de los libros")
    print("5. Mostrar clientes")
    print("6. Mostrar informacion de los clientes")
    print("7. Asignar un libro a un cliente")
    print("8. Salir")

while True:
    menu()
    choice=int(input())

    if choice>8:
        print("Esa opcion no existe")

    else:
        if choice==1:
            answer=""
            while answer!="no":
                print("Ingrese el nombre del libro")
                bookname=input()
                print("Ingrese el autor del libro")
                author=input()
                print("Ingrese el precio del libro")
                price=input()
                book=Book(bookname,author,price)
                book.add()
                answer=input("¿Quieres añadir otro libro? Si/No:")

        elif choice==2:
            answer=""
            while answer!="no":
                print("Ingrese el nombre del cliente")
                name=input()
                print("Ingrese la edad del cliente")
                age=input()
                print("Ingrese la direccion del cliente")
                direction=input()
                client=Client(name,age,direction)
                client.add()
                answer=input("¿Quieres añadir otro cliente? Si/No:")

        elif choice==3:
            showbooks()

        elif choice==4:
            book.view()

        elif choice==5:
            showclients()

        elif choice==6:
            client.view()

        elif choice==7:
            assing()

        elif choice==8:
            break