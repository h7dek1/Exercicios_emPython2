#EST.DEC_LT01.28
#declaração de variaveis
p_atual: int=0
m_mensal: int=0

#inicio
p_atual= int(input("preço atual: "))
m_mensal= int(input("media mensal de um produto: "))


if (m_mensal <500) and (p_atual<30):
    novo_preço1= p_atual*1.1
    print("O novo preço é: ",novo_preço1)
elif (m_mensal >=500 and m_mensal <1000) and (p_atual >=30 and p_atual <80):
    novo_preço2= p_atual*1.15
    print("O novo preço é: ",novo_preço2)
elif m_mensal >=1000 and p_atual >=80:
    novo_preço3= p_atual*1.05
    print("O novo preço é: ",novo_preço3)
else:
    novo_preço4= p_atual
    print("O novo preço é: ",novo_preço4)
#fim