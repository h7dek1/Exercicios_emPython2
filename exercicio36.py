#EST.DEC_LT01.36
#receba um numero n, calcule e mostre a serie 1+ 1/1! + 1/2! + ... 1/n!
#calculo de Euler

#declaração de variaveis
num_termos: int=0
euler=0
fat=1

#inicio
num_termos= int(input("Defina o valor de n: "))

for n in range (num_termos):
    if n == 0:
        fat = 1
    else: 
        fat *= n
    euler += 1/ fat
    print(f"A serie de {num_termos}: ",euler)
#fim