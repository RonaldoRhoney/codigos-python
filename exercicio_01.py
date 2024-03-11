#Exercícios:
nome = "Ronaldo Rhoney Martins"
email = "rhoney_falso@gmail.com"

# Descubra o servidor do email:

posicao = email.find("@")
servidor = email[posicao:]
print(servidor) 

# Pegue o 1º nome do usuário:
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# Construa uma mensagem: Usuário primeiro_nome cadastrado com sucesso com o em-al tal..:
mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o email: {email}" 
print(mensagem)

# Construa uma mensagem: Enviamos um link de confirmação para o email r***@gmail.com
primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um link de confirmação para o email {primeira_letra}***{servidor}"
print(mensagem2)