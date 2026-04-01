#EST.DEC_LT01.37
#receba um numero N, calcule e mostre a serie de 
#fibonacci até o seu n'nésimo termo

#declaração de variaveis
num_termos: int=0
n1= 1
n2= 2

#inicio
num_termos= int(input("defina o número de termos da série: "))
if (num_termos==1) or (num_termos==2):
    print("1")
else:
    for count in range(2,num_termos):
        termo= n1 + n2
        n2 = n1
        n1= termo
        count += 1
    print(f"A série de {num_termos} vai até: {termo}")
#fim
