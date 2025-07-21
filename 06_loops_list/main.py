# range

range(10) # todos os val int de 0 a 9, range(m) -> todos os val de 0 a m-1
range(5, 10) # todos os val int de 5 a 9, range(n, m) -> todos os val de n a m-1
range(5, 10, 2)  # todos os val de 5 a 9 com step de 2, range(n, m, s) -> todos os val de n a m-1
                 # com step de s
                 # 5 7 2
                 # 5 9
                 # range(4, 10, 2) -> 4 6 8
#for loop

for elm in range(3, 10, 3):
    print(f"{elm:2}", end=' ')

print("")

for elm in range(15, 10, -1):
    print(f"{elm:2}", end=' ')

print("")
print("---------" * 5)

for elm in range(10, 100):
    if elm == 20:
        break

    print(f"{elm:2}", end=' ')

print("")
for elm in range(10, 100):
    if elm == 30:
        break

    if elm % 2 == 0:
        continue

    print(f"{elm:2}", end=' ')


print("")

"""
int 
float 
double
char


char nome[10];
"""

nome = "Gonçalo"

for elm in nome:
    print(f"{elm:2}", end=' ')


# loop while
print("")




cond = True








# cond inicialmete é True

num = 10
while num > 0: # data > 10/12/2026
    print(f"{num:2}", end=' ')
    num -= 1


"""
while data < 10/12/2026:
    print(f"{data:2}", end=' ')
"""
print("")
print("----------")

num = 100
count = 0
while num > 0: # data > 10/12/2026

    if num == 30:
        break

    if num % 2 == 0:
        # print(f"Par: {num:2}", end=' ')
        # count += 1
        # print(f"count: {count}")
        num -= 1
        continue

    print(f"{num:2}", end=' ')
    num -= 1

print("")
print("--"*10,"Listas", "--"*10)
# listas ("array")
# c# ArrayList

lst = [1,2,4,5,6,7,8,9,10]

print(lst)
print(lst[0])
print(lst[1])
print(lst[8])

lst.append(99) # add no fim
print(lst)

# lst.append("Foo") <- EVITAR
# print(lst)


lst.insert(4, -1)
print(lst)


lst.pop() # ## remove por pos ->  sem parm -> ultimo
print(lst)


lst.pop(0) # ## remove por pos -> com parm -> pos indicada
print(lst)



lst.remove(-1) ## remove por valor
print(lst)

lst.append(5)
print(lst)

lst.remove(5) ## remove por valor -> remove a 1 vez q elm aparece, o val tem que existir
print(lst)


print(lst.pop())
print(lst.remove(2))

lst.append(5)
print(lst)
lst.append(5)
print(lst)
lst.append(5)
print(lst)


print(lst.count(5))

print(lst.__len__())
print(len(lst))

print(lst.index(5))

print(4 in lst)
print(42 in lst)

print(lst.__contains__(4))
print(lst.__contains__(42))


print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst.reverse()
print(lst)


nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fábio", "Gabriela", "Henrique", "Inês", "João",
    "Kátia", "Luís", "Marta", "Nuno", "Olívia", "Pedro", "Quitéria", "Rafael", "Sofia", "Tiago",
    "Úrsula", "Vítor", "Wanda", "Xavier", "Yara", "Zé", "Alice", "Bernardo", "Clara", "Diogo",
    "Eva", "Fernando", "Graça", "Hugo", "Irene", "Jorge", "Kelly", "Leonor", "Manuel", "Natália",
    "Orlando", "Paula", "Quintino", "Rita", "Sandra", "Telmo", "Vanessa", "Walter", "Ximena", "Yuri"
]


print(nomes[0])
print(nomes[-1])

print(nomes[0:10])
print(nomes[:10])

print(nomes[10:20])

print(nomes[0:20:2])

print(nomes[10:0:-1])

print(nomes[::-1])

print("-----"*10)


lst = [1,2,4,5,6,7,8,9,10]
print(lst)
lst.insert(3, 99)
print(lst)

lst.insert(-1, 99)
print(lst)

lst.insert(-2, 919)
print(lst)

lst.insert(15, 88)
print(lst)

lst.insert(-115, 88)
print(lst)

#lst.pop(-115)
#print(lst)

print("-----------")
nome = "Gonçalo"
print(nome[0])
print(nome[0:3])

print(nome[0].lower())


print(nome)