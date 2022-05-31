sonrie = ["si"]
def problemas_monos(a_sonriendo, b_sonriendo):
    if a_sonriendo == b_sonriendo:
        final= True
    else:
        final = False
    print(final)
print("¿El mono A esta sonriendo?")
print("Si/No")
eleccion = str(input())
eleccionlower= eleccion.lower()
a_sonriendo = eleccionlower in sonrie
print("¿El mono B esta sonriendo?")
print("Si/No")
eleccion1 = str(input())
eleccion1lower= eleccion1.lower()
b_sonriendo = eleccion1lower in sonrie
problemas_monos(a_sonriendo,b_sonriendo)