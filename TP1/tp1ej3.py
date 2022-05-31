def suma(num1,num2):
    if num1 == num2:
        resultado = (num1+num2) * 2
    else:
        resultado = num1+num2
    print(resultado)
print("Introduce un numero")
num1 = int(input())
print("Introduce otro numero")
num2 = int(input())
suma(num1,num2)