import csv
import numpy as np
import pandas as pd

def read_dataset(file_path):
    dataset = []
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row:
                if (row[0] == 'Id'): continue  # Ignora o cabeçalho do CSV
                datapoint = [float(value) for value in row[1:4]]  # Extrai as features como números
                datapoint.append(row[5])  # Adiciona a classe
                dataset.append(datapoint)
    return dataset

def initialize_centroids(data, k):
    # Utilizando o algoritmo k-means++ para inicializar os centróides
    centroides = data.copy()
    np.random.shuffle(centroides)
    return centroides[:k]

def assign_clusters(data, centroids):
    # Atribuindo cada ponto ao cluster mais próximo
    distancias = np.linalg.norm(data - centroids[:, np.newaxis], axis=2)
    return np.argmin(distancias, axis=0)

def update_centroids(data, clusters, k):
    # Atualizando os centróides com base na média dos pontos em cada cluster
    centroides = np.zeros((k, data.shape[1]))
    for cluster in range(k):
        pontos_cluster = data[clusters == cluster]
        if len(pontos_cluster) > 0:
            centroides[cluster] = np.mean(pontos_cluster, axis=0)
    return centroides

def k_means(data, k):
    # Inicialização dos centróides
    centroides = initialize_centroids(data, k)
    
    # Execução do algoritmo até a convergência
    while True:
        # Atribuição dos pontos aos clusters
        clusters = assign_clusters(data, centroides)
        
        # Atualização dos centróides
        novos_centroides = update_centroids(data, clusters, k)
        
        # Verificação de convergência
        if np.array_equal(novos_centroides, centroides):
            break
        
        centroides = novos_centroides
    
    return clusters, centroides

file_path = "k-means/iris/Iris.csv"

# Carregando os dados do arquivo CSV
dados = pd.read_csv(file_path)

X = dados[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values

# Definindo o número de clusters (k=3 neste exemplo)
k = 3

# Executando o algoritmo k-means
clusters, centroides = k_means(X, k)

# Exibindo os resultados
print("Clusters:")
print(clusters)
print("\nCentróides:")
print(centroides)
