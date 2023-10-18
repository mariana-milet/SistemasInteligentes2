import pandas as pd

nomeAC = "treino_sinais_vitais_com_label.txt"
nomeAS = "treino_sinais_vitais_sem_label.txt"
df = pd.read_csv(nomeAS)
df = df.drop('i', axis=1)
print(df)


