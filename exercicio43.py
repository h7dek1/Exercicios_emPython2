#EST.DEC_LT01.43
#CALCULE E MOSTRE QUANTOS ANOS SERÃO NECESSÁRIOAS PARA QUE
#ANA SEJA MAIOR QUE MARIA SABENDO QUE ELA TEM 1,10M E CRESCE 3CM AO ANO
#E MARIA TEM 1,5M E CRESCE 2CM AO ANO.

#declaração de variaveis
ana= 1.1
maria= 1.5

#inicio
while ana < maria:
    ana+= 0.03
    maria+= 0.02
    cresc_a= ana
    cresc_m= maria
    div_a= (cresc_a- 1.1) /0.03
    div_m= (cresc_m- 1.5) /0.02
print(f"A altura de Ana é: {round(ana, 2)} e de Maria {round(maria, 2)}")
print(f"Para Ana ser maior que Maria, serão necessários {round(div_a)} anos")
#fim