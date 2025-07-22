"""

var
op var

if-elif-else
match-case

range
for
while


    func
multi files
intro- intro Pandas


2f
intro Pandas (1h a 2h)

4f - trabalho

"""
from sqlalchemy.testing.suite.test_reflection import users


def ola_mundo():
    sum = 0
    for i in range(10):
        sum += i

    print(f"Ola Mundo: {sum}")

ola_mundo()

# range(n) -> todos os num int de 0 ate n-1
print("----"*10)

def ola_mundo2(max):
    sum = 0
    for i in range(max+1):
        sum += i

    print(f"Ola Mundo: {sum}")


ola_mundo2(10)
ola_mundo2(100)
ola_mundo2(1000)

print("----"*10)
def ola_mundo3(max):
    sum = 0
    for i in range(max+1):
        sum += i

    return f"Ola Mundo: {sum}"


res = ola_mundo3(10)
print(res)

print(ola_mundo3(15))



print("----"*10)

def ola_mundo4(nome):
    return f"Ola Mundo: {nome.upper()}"

print(ola_mundo4("Gonçalo"))


def ola_mundo5(nome):
    return f"Ola Mundo: {nome.upper()}"

print(ola_mundo5("gonçalo"))


# nome: str -> type hint
def ola_mundo6(nome: str):
    try:
        return f"Ola Mundo: {nome.upper()}"
    except:
        return f"Tipo de dados invalido"


print(ola_mundo6(" - Gonçalo - "))
print(ola_mundo6(123))


print(type("123"))
print(type(123))
print(type(12.12))
print(type(True))


def ola_mundo7(nome: str, ano:int):
    print(f"Ola Mundo: {nome} em {ano}")



ola_mundo7("Gonçalo", 2025)

ola_mundo7(nome="Gonçalo", ano=2025)

ola_mundo7(ano=2025, nome="Gonçalo")


def ola_mundo8(nome: str, ano:int, ano2:int):
    print(f"Ola Mundo: {nome} em {ano} - {ano2}")


ola_mundo8("Gonçalo", ano2=2000, ano=2025)
ola_mundo8("Gonçalo", ano=2000, ano2=2025)



def ola_mundo9(nome: str, ano:int, ano2:int=1998):
    print(f"Ola Mundo: {nome} em {ano} - {ano2}")

ola_mundo9("nome", 2013)

ola_mundo9("nome", 2013, 2000)
ola_mundo9("nome", 2013, ano2=1995)

ola_mundo9("nome",ano2=1995, ano=2013)


print("----"*10)
print("----"*10)


def soma(vals):
    return sum(vals)


print(soma([1,2,3,4,5]))



def soma2(*args):
    return sum(args)


print(soma2(1,2,3,4,5))


def foo(usr:str, *lista_ips):
    return f"o user {usr} acedeu dos ips: {lista_ips}"

print(foo("usr1", "123.123.122.122", "164.123.141.323"))



def registo(**usrInfo):
    print("username:", usrInfo["usr"])
    print("password:", usrInfo["pwd"])
    print("email:", usrInfo["email"])

    for elm in usrInfo.items():
        print(f"{elm}")


registo(usr="usr1", pwd="pass do usr 1", email="email do usr 1")



