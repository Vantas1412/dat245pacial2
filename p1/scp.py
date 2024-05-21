import csv
dat = []
with open("C:/Users/Gerson/Downloads/Current_Pub_Meta.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        dat.append(row)
dat_t = list(zip(*dat))

def calcularUlt(col):
    col_or = sorted(col)
    ind = int(len(col_or) * 0.75)
    return col_or[ind]

def calcular80(col):
    col_or = sorted(col)
    ind = int(len(col_or) * 0.80)
    return col_or[ind]

ult = [calcularUlt(col) for col in dat_t]
per = [calcular80(col) for col in dat_t]

for i, col in enumerate(dat_t):
    print(f"Columna {i+1}:")
    print(f"Último cuartil: {ult[i]}")
    print(f"Percentil 80: {per[i]}")
    print()
