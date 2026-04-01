#EST.DEC_LT01.21
#declaracao de variaveis
n1: int=0
n2: int=0
n3: int=0
n4: int=0

#inicio
n1= int(input("receba nota1: "))
n2= int(input("receba nota2: "))
n3= int(input("receba nota3: "))
n4= int(input("receba nota4: "))

media_a= (n1+n2+n3+n4)/4
print("media aritmética é: ",media_a)

if media_a>=6:
        print("Aprovado")
elif media_a >=3 and media_a <6:
        print("Exame")
else:
        print("Retido")
#fim