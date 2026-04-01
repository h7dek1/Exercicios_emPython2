#EST.DEC_LT01.27
#declaração de variaveis

n_voltas: int=0
e_circuito: int=0 #extensão em metros
tempo_dur: int=0 #tempo de duração em minutos

#inicio
n_voltas= int(input("numero de voltas: "))
e_circuito= int(input("extensão do circuito em metros: "))
tempo_dur= int(input("tempo de duração em minutos: "))

dist_total= (n_voltas*e_circuito)
temp_s= (tempo_dur*60)
v_media= (dist_total/temp_s)*3.6
print("velocidade média é: ", v_media)
#fim