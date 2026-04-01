#receba um n inteiro, calcule e mostre seu fatorial

#EST.DEC_LT01.32
#declaracao de variaveis
n: int=0

#inicio
n= int(input("defina o valor de n: "))

fat=1
for n in range (1, n+1):
    fat *= n 
int(f"O fatorial de {n}: ",fat)
#fim
