#EST.DEC_LT01.40
#RECEBA 2 NUMEROS INTEIROS. VERIFIQUE E MOSTRE 
#TODOS OS NUMEROS PRIMOS EXISTENTES ENTRE ELES

#declaração de variáveis
n1: int=0
n2: int=0

#inicio
n1=int(input("Defina o valor de n1: "))
n2=int(input("Defina o valor de n2: "))
print(f"Números primos entre {n1} e {n2}:")

for primos in range(n1, n2 + 1):
    if primos > 1:
        primo = True
        i = 2
        while i * i <= primos:  # verifica até a raiz quadrada de primos
            if primos % i == 0:
                primo = False
                break
            i += 1
        if primo:
            print(primos, end=" ")
#fim