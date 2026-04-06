#EST.DEC_LT.01.41
#Mostre todas as possibilidades de 2 dados de forma
#que a soma tenha como resultado 7

#Declaração de variaveis
contador=0
#inicio
for dado1 in range (1, 7):
    for dado2 in range(1 , 7):
        if dado1 + dado2 ==7:
            print((dado1, dado2))
            contador +=1
print(f"São {contador} possibilidades de 2 dados apresentarem o resultado 7.")
#fim