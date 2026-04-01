#EST.DEC_LT.01.25
#declaracao de variaveis
h_i: int=0
m_i: int=0
h_f: int=0
m_f: int=0

#inicio
h_i= int(input("defina hora de inicio: "))
m_i= int(input("defina minuto de inicio: "))
h_f= int(input("defina hora de fim: "))
m_f= int(input("defina minuto de fim: "))

convs_hi= ((h_i*60) + m_i) #conversão para minutos
convs_hf= ((h_f*60) + m_f) #conversão para minutos

from datetime import time, timedelta, datetime

print(timedelta(minutes= convs_hi))
print(timedelta(minutes= convs_hf))

temp_j = timedelta(minutes= convs_hf) - timedelta(minutes= convs_hi)
print("tempo de jogo foi: ",temp_j)
#fim
