
import calendar

ano = int(input("Informe o ano: "))
mes = int(input("Informe o mês: "))

calendario = calendar.month(ano, mes)
print(calendario)