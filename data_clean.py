import pandas as pd


df=pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
del df["Stars_name"]
del df["distance"]
del df["mass"]
del df["radius"]

df.to_csv("final.csv")