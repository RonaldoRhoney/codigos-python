faturamento = 1000
custo = 700

lucro = faturamento - custo

print("f Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email = "EMAIL_falso@gmail.com"

print(email.lower())
print(email.find("@"))

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

tamanho = len(email)
print(tamanho)

email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "Ronaldo Rhoney"
print(nome.capitalize())
print(nome.title())

margem = lucro / faturamento
print(f"Faturamento: R$ {faturamento:.2f}\n Custo: R$ {custo:.2f}\n Lucro: R$ {lucro:.0%}")