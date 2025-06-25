
# cmt 1 linha
"""
cmt
multi
linha

"""

nome = "Gonçalo" # String nome = "Gonaçlo";
ano = 2025 # int nome = 2025;

print(nome)
print(ano)

# tudo na mesma linha

#v1
print(nome, ano)

print("Ola", nome, "no ano", ano)


#v2
# str(ano) - Cria uma str com o valor de ano, em c# -> ano.ToString()
print("Ola" + nome + "no ano" + str(ano))


# v2.2
print("Ola " + nome + " no ano " + str(ano))


#v3
print(f"Ola {nome} no ano {ano}")