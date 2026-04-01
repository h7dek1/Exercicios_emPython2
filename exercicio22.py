#EST.SEQ_LT01.22
#declaracao de variaveis
n1: int=0
n2: int=0

#inicio
n1= int(input("receba o valor de n1: "))
n2= int(input("receba o valor de n2 diferente de n1: "))
if n1>n2:
    print("ordem crescente dos valores: ",n1,n2)
else:
    print("ordem crescente dos valores: ",n2,n1)
#fim