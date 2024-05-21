import pandas as pd

df = pd.read_csv("C:/Users/Gerson/Downloads/Current_Pub_Meta.csv", encoding="utf-8")

numeric_cols = df.columns[:]  
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df_t = df

def calcularUlt(col):
    return col.quantile(0.75)

def calcular80(col):
    return col.quantile(0.80)

ult = df_t.apply(calcularUlt)
per = df_t.apply(calcular80)

for i, col in enumerate(df_t.columns):
    print(f"Columna {i+1}:")
    print(f"Último cuartil: {ult[col]}")
    print(f"Percentil 80: {per[col]}")
    print()
