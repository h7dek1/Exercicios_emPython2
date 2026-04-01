#Receba um número. Calcule e mostre os resultados da tabuada desse número.

#EST.DEC_LT01.34
#declaracao de variaveis
n: int=0

#inicio
n = int(input("Defina 'n' para ver sua tabuada: "))
print(f"Tabuada do {n}:")

for variavel_tab in range(0, 11):
    print(f"{n} x {variavel_tab} = {n * variavel_tab}")
#fim