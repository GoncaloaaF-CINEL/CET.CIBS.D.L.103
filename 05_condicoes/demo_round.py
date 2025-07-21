nota = round(9.99, 0) # round(n, c) -> num decimal, c -> arredondar para c casas decimais
print(nota)


nota = 9.999999999999999
print(nota.__floor__())

print(int(nota)) # descarta a parte decimal

nota = 9.000000000000001
print(nota.__ceil__())

