#EST.DEC_LT01.23
#declaracao de variaveis
n1: int=0
n2: int=0
n3: int=0
n4: int=0

#inicio
n1= int(input("atribua o valor n1: "))
n2= int(input("atribua o valor n2: "))
n3= int(input("atribua o valor n3: "))
n4= int(input("atribua o valor n4: "))

if n1<n2<n3<n4:
    print("valores em ordem crescente: ",n1,n2,n3,n4)
elif n4<n1<n2<n3:
     print("valores em ordem crescente: ",n4,n1,n2,n3)
elif n1<n4<n2<n3:
    print("valores em ordem crescente: ",n1,n4,n2,n3)
else:
    print("valores em ordem crescente: ",n1,n2,n4,n3)
#fim