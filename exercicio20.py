#est.dec_LT.20
#declaração de variaveis
a: int=0
b: int=0
c: int=0

#inicio
a= int(input("receba o valor de a: "))
b= int(input("receba o valor de b: "))
c= int(input("receba o valor de c: "))

delta= (b**2-4*a*c)

if delta<0:
    print("Não existem raizes reais")
else:
    print("Existem raizes reais")
    x1= ((-(-b)+(delta**0.5))/2*a)
    x2= ((-(-b)-(delta**0.5))/2*a)
    print("raiz 1 é: ",x1)
    print("raiz 2 é: ",x2)
#fim