import pandas as pd
import math

def calculate_entropy(values):
    total_values = len(values)
    value_counts = {}  # Dicionário para contar a frequência de cada valor

    for value in values:
        if value not in value_counts:
            value_counts[value] = 1
        else:
            value_counts[value] += 1

    entropy = 0
    print('value_counts: ')
    print(value_counts)
    print('value_counts.values(): ')
    print(value_counts.values())
    for count in value_counts.values():
        proportion = count / total_values
        entropy -= proportion * math.log2(proportion)

    return entropy

nomeAC = "treino_sinais_vitais_com_label.txt"
nomeAS = "treino_sinais_vitais_sem_label.txt"
df = pd.read_csv(nomeAS)
df = df.drop('i', axis=1)
#print(df.head())
coluna = df['pSist'].to_list()
#print(coluna)
print('---------------------------------------------------------------')

# Exemplo de valores float em uma coluna
column_values = [0.123456, 0.987654, 0.543210, 0.876543]
column_values2 = [0.1, 0.2, 0.3, 0.4]

# Calcula a entropia
entropy = calculate_entropy(column_values2)
print(f"A entropia da coluna e: {entropy:.6f}")

import numpy as np
from scipy.stats import entropy

# Seu vetor
vetor = np.array(column_values2)

# Normalizar o vetor para que a soma seja 1
vetor_norm = vetor / np.sum(vetor)

# Calcular a entropia
entropia = entropy(vetor_norm)

print(f'A entropia do vetor é: {entropia:.6f}')


