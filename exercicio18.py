#EST.DEC_LT01.18
#declaracao de variaveis
n1: int=0
n2: int=0

#inicio
n1= int(input("receba o valor de n1: "))
n2= int(input("receba o valor de n2: "))

if n1>n2:
    dif1= n1-n2
    print("diferença do maior pelo menor: ",dif1)
else:
    dif2= n2-n1
    print("diferença do maior pelo menor: ",dif2)
#fim