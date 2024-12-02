from utils.csv_helper import get_list_from_csv

def montarListasOrdenadas(lista):
    l1 = []
    l2 = []
    for i in range (len(lista)):
        elementos = lista[i].split("   ")
        if len(l1) == 0 and len(l2) == 0:
            l1.append(int(elementos[0]))
            l2.append(int(elementos[1]))
        else:
            if int(elementos[0]) < l1[0]:
                l1.insert(0, int(elementos[0]))
            elif int(elementos[0]) > l1[len(l1) - 1]:
                l1.append(int(elementos[0]))
            else:
                for j in range(len(l1)):
                    if int(elementos[0]) < l1[j]:
                        l1.insert(j, int(elementos[0]))
                        break
            
            if int(elementos[1]) < l2[0]:
                l2.insert(0, int(elementos[1]))
            elif int(elementos[1]) > l2[len(l2) - 1]:
                l2.append(int(elementos[1]))
            else:
                for j in range(len(l2)):
                    if int(elementos[1]) < l2[j]:
                        l2.insert(j, int(elementos[1]))
                        break
    return l1, l2

lista = get_list_from_csv("../csv/day_1.csv")

soma = 0
soma2 = 0

l1, l2 = montarListasOrdenadas(lista)

for i in range(len(l1)):
    soma += abs(l2[i] - l1[i])
    soma2 += l1[i] * l2.count(l1[i])
print(soma)
print(soma2)
