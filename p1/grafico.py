import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("C:/Users/Gerson/Downloads/Current_Pub_Meta.csv", encoding="utf-8")
df_numeric = df.select_dtypes(include=['number'])
print(df.columns)

plt.figure(figsize=(10, 10))
plt.bar(df['Name'],df["Primary Attribute"] )
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de la columna')
plt.show()


