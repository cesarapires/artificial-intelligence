import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carregando os dados do arquivo CSV
file_path = "k-means/iris/Iris.csv"
dados = pd.read_csv(file_path)

# Selecionando as features (colunas) utilizadas para clustering
X = dados[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values

# Normalizando os dados para ter média zero e variância unitária
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Definindo o número de clusters (k=3 neste exemplo)
k = 3

# Criando o objeto KMeans
kmeans = KMeans(n_clusters=k, random_state=42)

# Aplicando o algoritmo KMeans aos dados normalizados
kmeans.fit(X_scaled)

# Obtendo os rótulos dos clusters e os centróides finais
clusters = kmeans.labels_
centroides = kmeans.cluster_centers_

# Exibindo os resultados
print("Clusters:")
print(clusters)
print("\nCentróides:")
print(centroides)
