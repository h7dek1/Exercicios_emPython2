#EST.DEC_LT01.44
#Receba o número a base e do expoente.
#calcule e mostre o valor da potencia

#declaração de variaveis
base: int=0
exp: int=0

#inicio
base= int(input("Defina o valor da base: "))
exp= int(input("Defina o valor do expoente: "))
pot= base ** exp
print(f"O valor da potência {base}**{exp} é: {pot}")
#fim