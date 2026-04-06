#EST.DEC_LT01.38
import random

#inicio
cem_int = [random.randint(1,777) for _ in range (100)]
print("São os 100 inteiros aleatórios: ", cem_int)

#mostrando o maior e menor valor
print("O maior número é: ", max(cem_int))
print("O menor número é: ", min(cem_int))
#fim
