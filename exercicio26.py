#EST.DEC_LT01.26
#declaração de variaveis
n1: int=0
n2: int=0

#inicio
n1= int(input("receba o valor de n1: "))
n2= int(input("receba o valor de n2: "))

if ((n1%n2) ==0):
    print("n1 é multiplo de n2")
else: 
    print("n1 não é multiplo de n2")


if ((n2%n1) ==0):
    print("n2 é multiplo de n1")
else: 
    print("n2 não é multiplo de n1")
#fim
