# o input recebe sempre uma str

nome = input("Digite seu nome: ")
print(nome)

idade = int(input("Digite seu idade: "))
print(idade)

ano_nasc = 2025 - idade

print(f"Olá {nome}, nasceste em {ano_nasc} e tens {idade} anos")