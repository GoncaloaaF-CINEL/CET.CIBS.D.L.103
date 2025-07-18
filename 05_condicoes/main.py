
"""

int nota = 10;
if( nota > 10 ){
    console.WriteLine("aprovado");
}

"""


nota = 1

if nota >= 10:
    print("aprovado")
    print("nova linha")
else:
    print("não aprovado")

print("fora do if")


print("-----"*3, "if else", "-----"*3)


nota = 9

if nota >= 10:
    print("aprovado")
elif nota >= 8: # em c# -> else if (nota >= 8){
    print("prova oral")
else:
    print("não aprovado")


print("-----"*3, "and | or | not", "-----"*3)

print("--"*3, "and - c# -> &&", "--"*3)

nota = 21
if nota >= 0 and nota <=20:
    print("nota valida")
else:
    print("nota invalida")

print("--"*3, "or- c# -> ||", "--"*3)

nota_pratica = 8
nota_teorica = 20

if nota_pratica < 10 or nota_teorica < 10:
    print("nao aprovado")

elif nota_pratica >= 10 and nota_teorica >= 10:
    print("aprovado")


print("--"*3, "not - c# -> !", "--"*3)


nota = 21

if not (nota >= 10) and nota <=20:
    print("não aprovado")
else:
    print("aprovado")



print("-----"*3, "op trenario", "-----"*3)

# nota >= 10 ? "aprovado":"nao aporvado"

nota = 3

resp = "aprovado" if nota >= 10 else "nao aprovado"
print(resp)


print("aprovado") if nota >= 10 else print("nao aprovado")
