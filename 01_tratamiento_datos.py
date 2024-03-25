import pandas as pd
import numpy as np

# https://www.youtube.com/watch?v=XcmCwJCNR7Q&list=PL5C9QKu8AsmUDmAZNFiPEHxYTbZtliZZl
df = pd.read_csv("dataset_1.csv", index_col=0,encoding='latin-1')


print("dataset--->")
# print(df)
print("descripcion->")
# print(df.describe())
print(df.info())


# ? tenemos que saber los datos categoricos
