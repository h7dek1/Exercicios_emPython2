#EST.DEC_LT01.39
#CALCULE A QUANTIDADE DE GRAOS CONTIDOS EM UM TABULEIRO DE XADREZ
#CASA 1 | 2 | 3 | 4 ... 64
#QTDE 1 | 2 | 4 | 8 ... NN

#inicio
for casa in range (1, 65, 1):
    if casa ==1:
        qtde= casa*casa
        print(f"O número de grãos na casa {casa} é: {qtde}")
    else:
        qtde = 2**(casa-1)
        print(f"O número de grãos na casa {casa} é: {qtde}")
#fim