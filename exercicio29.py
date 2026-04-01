#EST.DEC_LT.01.29
#declaracao de variaveis
vlr: int=0

#inicio
vlr= int(input("receba o valor investido: "))

vlr_p= (vlr+(vlr*3/100))
vlr_rf= (vlr+(vlr*5/100))
print("O valor investido em poupança em 30 dias será de: ",vlr_p)
print("O valor investido em renda fixa em 30 dias será de: ",vlr_rf)
#fim