#Receba 2 números inteiros, verifique qual o maior entre eles.
#Calcule e mostre o resultado da somatória dos números ímpares entre esses valores. 

#EST.DEC_LT01.35
#declaracao de variaveis
n1: int=0
n2: int=0

#inicio
n1= int(input("defina o valor de n1: "))
n2= int(input("defina o valor de n2: "))
soma=0

for n in range(min(n1, n2), max(n1, n2) + 1):
    if n % 2 != 0:
        soma += n
print(f"A soma dos números ímpares entre {n1} e {n2} é: {soma}")
#fim