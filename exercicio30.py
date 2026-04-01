#EST.DEC_LT01.30
from datetime import datetime
from dateutil.relativedelta import relativedelta

#inicio
def idade(d_nasc_str):
    try:
    #convertendo string para um objeto date
        d_nasc= datetime.strptime(d_nasc_str, "%d/%m/%Y").date()
    except ValueError:
        raise ValueError("Data inválida. Atribua novamente.")

    #usando biblioteca datetime para obter a data atual
    d_atual = datetime.today().date()

    #validando a condicional: data de nascimento não pode ser no futuro
    if d_nasc > d_atual:
        raise ValueError("A data de nascimento não pode ser maior que a data atual.")

    #calculando a diferença 
    diferenca = relativedelta(d_atual, d_nasc)

    return diferenca.years, diferenca.months, diferenca.days, d_atual

if __name__ == "__main__":
    try:
        nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
        anos, meses, dias, d_atual = idade(nasc)

        print(f"Data atual: {d_atual.strftime('%d/%m/%Y')}")
        print(f"Você tem {anos} anos, {meses} meses e {dias} dias de vida.")
    except ValueError as e:
        print(f"Erro: {e}")
#fim