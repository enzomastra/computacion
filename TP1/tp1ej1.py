dormir=["enero","febrero","sabado","domingo"]
def mes(vacacioneslower):
    final1= vacacioneslower in dormir
    if final1 == True:
        print("Dormir")
def dia(dia_semanalower):
    final2 = dia_semanalower in dormir
    if final2 == False:
        print("Laburar")
    else:
        print("Dormir")
print("¿En que mes estas?")
vacaciones = str(input())
vacacioneslower = vacaciones.lower()
mes(vacacioneslower)
final = vacacioneslower in dormir
if final == False:
    print("¿En que dia estas?")
    dia_semana = str(input())
    dia_semanalower = dia_semana.lower()
    dia(dia_semanalower)