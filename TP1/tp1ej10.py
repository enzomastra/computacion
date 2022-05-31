def caracter_perdido(str,n):
    if str[n] in str:
        for x in range(len(str[n])):
            str1 = str.replace(str[n],"")
            print(str1)
    else:
        print("La palabra no tiene ese numero representado en letra :(")
print("Introduce una palabra:")
str = str(input())
print("Introduce un numero que quitara la letra en esa posicion")
n = int(input())
caracter_perdido(str,n)