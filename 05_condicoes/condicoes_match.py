## swtich case

mes = "1"

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Marco")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case _: # caso pre-definido, se nenhum caso for valido c# -> default
        print("mes invalido")



"""

0 - 9 (F)
10-11 (E): Suficiente.
12-13 (D): Satisfaz.
14-15 (C): Bom.
16-17 (B): Muito Bom.
18-20 (A): Excelente. 

"""

nota = round(9.45, 2) # round(n, c) -> num decimal, c -> arredondar para c casas decimais
print(nota)


match nota:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
        print("F")
    case 10 | 11:
        print("E")
    case 12 | 13:
        print("D")
    case _:
        print("nota invalida")