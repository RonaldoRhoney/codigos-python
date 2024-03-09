# Operações matemática

faturamento = 1000
custo = 700

novas_vendas = 300


faturamento = faturamento + novas_vendas # soma
imposto = faturamento * 0.1 # multiplicação
lucro = faturamento - custo - imposto # subtração


print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento # dividir
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)

# mode - resto da divisão
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print(tempo_em_meses, "anos")
print(tempo_em_meses % 12, "meses")

# dicas 

numero = 123.97
print(round(numero))

faturamento = 139_018_182 # _ aqui é qpenas um recurso visiual para facilitar a leitura
