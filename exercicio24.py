#EST.DEC_LT01.24
#declaracao de variaveis
# Receba um valor inteiro, verifique e mostre se é divisivel por 2 e 3
n1: int=0

#inicio
n1= int(input("receba o valor de n1: "))
dv2= False
if ((n1%2) ==0):
    dv2 = True
    
dv3=False
if ((n1%3) ==0):
    dv3 = True

if dv2 and dv3==True:
    print("n1 é divisível por 2 e 3")
else:
    print("n1 não é divisível por 2 e 3")
#fim