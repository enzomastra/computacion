def no_cadena(str):
    if str[0:2] == "no":
        print(str)
    else:
        print("no ", str)
print("Ingrese un str")
str = str(input())
no_cadena(str)