def pos_negativa(a,b,negativa):
    if negativa==False:
        num1=a>0
        num2=b>0
        final=num1!=num2
        print(final)
    else:
        num1=a<0
        num2=b<0
        final=num1==True and num2==True
        print(final)
print("Ingresa 2 valores")
a=int(input())
b=int(input())
print("¿Quieres activar el parametro ´negativa´? - Si/No")
rta=str(input())
rtalow=rta.lower()
negativa=rtalow=="si"
pos_negativa(a,b,negativa)