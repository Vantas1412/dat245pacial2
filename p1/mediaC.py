import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("C:/Users/Gerson/Downloads/Current_Pub_Meta.csv", encoding="utf-8")
df_numeric = df.select_dtypes(include=['number'])

media = df_numeric.mean()
mediana = df_numeric.median()
moda = df_numeric.mode().iloc[0] 
media_geometrica = stats.gmean(df_numeric.values.flatten()) 

print("Media:")
print(media)
print("\nMediana:")
print(mediana)
print("\nModa:")
print(moda)
print("\nMedia geométrica:")
print(media_geometrica)
