
print("Faturamento", 1000)
print("Custo", 500)
print("Lucro", 1000 - 500)

# melhorando o código com VARIÁVEIS 

faturamento = 1000 # número inteiro (int)
custo = 700

novas_vendas = 600
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1 # número decimal (float)
mensagem = "O faturamento foi de " # strig (testo)
teve_lucro = False # boolean (booleano)

imposto = taxa_imposto * faturamento
print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)