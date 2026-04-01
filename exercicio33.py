#EST.DEC_LT01.33
#declaracao de variaveis
n: int=0

#inicio
n= int(input("defina o valor de n: "))
inteiro =1
serie= 0

while inteiro <= n:
    serie += 1/inteiro
    inteiro +=1
print(f"a serie de {n}: ",serie)
#fim