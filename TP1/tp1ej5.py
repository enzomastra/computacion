def problema_loro(hora):
    if hora<7 or hora>20:
        problema = True
    else:
        problema = False
    print(problema)
print("El loro esta hablando??")
print("Si//No")
hablando = str(input())
hablando = hablando.lower()
print("Que hora es??")
hora = int(input())
if hablando == "si":
    problema_loro(hora)
if hablando == "no":
    problema = False
    print(problema)