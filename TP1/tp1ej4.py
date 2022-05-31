def diferencia(n):
    if n>21:
        resultado = (n - 21)*2
    else:
        resultado = 21-n
    print(resultado)
print("Diferencia con 21")
print("Escribe un numero")
n = int(input())
diferencia(n)