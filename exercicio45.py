#EST.DEC_LT01.45
#Calcule e mostre a série 
#1 - 2/4 + 3/9 - 4/16 + 5/25 - ... + 15/225 

#série baseada em potencia do numerador com 
#denominador sendo o produto do numerador

#declaração de variaveis
total= 0
denominador = 1

#inicio
for numerador in range(1,16):
    denominador= numerador**2
    div= numerador/denominador
    if numerador % 2 == 0:
        div= -div
    print(f"{numerador} / {denominador}")
    total+= div

print(f"A soma da série é: {total}")
#fim