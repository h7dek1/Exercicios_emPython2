#EST.DEC_LT01.42
#CALCULE E MOSTRE A SÉRIE 1 + 2/3 + 3/5 + ... 50/99

#declaração de variaveis
denominador = 1 #(1 = 1/1)
total= 0

#inicio
print("A série completa é: ") 

for numerador in range (1, 51):
    termo= numerador/denominador
    print(f"{numerador}/{denominador}")
    denominador += 2 #faz com que o denominador aumente de 2 em 2
    total += termo
print(f"Sua soma é: {total}")
#fim