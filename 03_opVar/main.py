val1 = 10
val2 = 20

# op com var

print(val1 + val2)

soma = val1 + val2
print(soma)

sub = -val1 + -val2
print(sub)

mult = val1 * val2
print(mult)

divi = val1 / val2
print(divi)

val3 = 8
val4 = 3

# modulo -> resto
"""

0 1 2 3 4 5 6 7 8 9
0 1 2 0 1 2 0 1 2 0

9 Mod 3 = 0

"""
modulo = val3 % val4
print(modulo)

# div inteira
div_int = val3 // val4
print(div_int)

mod_v2 = 8 % -3
print(mod_v2)

div_v2 = 8 / 3.5
print(div_v2)

mod_v3 = 8 % 3.5
print(mod_v3)

val3 = 5
val4 = 2.5

div_int2 = val3 // val4
print(div_int2)

## op com str

str1 = "Ola"
str2 = "Mundo"

print(str1 + str2)
print(str1, str2)

ano = 2025

print(str1 + " " + str2 + " " + str(ano))

# str(ano)

# type -> ver o tipo de uma var

ano_s = "2025"
print(type(ano_s))

ano_i = int(ano_s)
print(type(ano_i))


print("------")

print(str1 + " " + str2 + " no ano " + str(ano))

print(f"{str1} {str2} no ano {ano}")

"""
\n - new line
\t - tab
"""
print("Ola\n" * 5)



## print("Ola" - "Ol") <- Erro
## print("Ola" - 4)  <- Erro

## print("Olaa" / "a") <- Erro

## print("Ola\n" * 5.5) <- Erro


