import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score

# Carregar a base de dados Iris
iris = load_iris()
X_iris, y_iris = iris.data, iris.target

# Carregar a base de dados Wine
wine = load_wine()
X_wine, y_wine = wine.data, wine.target

# Dividir a base de dados Iris
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)

# Dividir a base de dados Wine
X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine, y_wine, test_size=0.2, random_state=42)

# Padronizar os dados Iris
scaler_iris = StandardScaler()
X_train_iris = scaler_iris.fit_transform(X_train_iris)
X_test_iris = scaler_iris.transform(X_test_iris)

# Padronizar os dados Wine
scaler_wine = StandardScaler()
X_train_wine = scaler_wine.fit_transform(X_train_wine)
X_test_wine = scaler_wine.transform(X_test_wine)

# Treinar o modelo MLPClassifier na base de dados Iris
mlp_iris = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
mlp_iris.fit(X_train_iris, y_train_iris)

# Treinar o modelo MLPClassifier na base de dados Wine
mlp_wine = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
mlp_wine.fit(X_train_wine, y_train_wine)

# Avaliar o modelo na base de dados Iris
y_pred_iris = mlp_iris.predict(X_test_iris)
accuracy_iris = accuracy_score(y_test_iris, y_pred_iris)
precision_iris = precision_score(y_test_iris, y_pred_iris, average='weighted')
recall_iris = recall_score(y_test_iris, y_pred_iris, average='weighted')

# Avaliar o modelo na base de dados Wine
y_pred_wine = mlp_wine.predict(X_test_wine)
accuracy_wine = accuracy_score(y_test_wine, y_pred_wine)
precision_wine = precision_score(y_test_wine, y_pred_wine, average='weighted')
recall_wine = recall_score(y_test_wine, y_pred_wine, average='weighted')

# Funções para plotar a matriz de confusão
def plot_confusion_matrix(y_true, y_pred, title, labels):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title(title)
    plt.show()

# Imprimir as métricas formatadas
def print_metrics(algorithm_name, dataset_name, accuracy, precision, recall):
    print(f"Algoritmo do {algorithm_name} para classificação com a {dataset_name}")
    print("-" * 55)
    print(f"Precisão: {precision * 100:.2f}% | Revocação: {recall * 100:.2f}% | Acurácia: {accuracy * 100:.2f}%")
    print("-" * 55)

# Plotar e calcular as métricas para a base de dados Iris
print_metrics("MLPClassifier", "IrisDatabase", accuracy_iris, precision_iris, recall_iris)
plot_confusion_matrix(y_test_iris, y_pred_iris, "Confusion Matrix for Iris Dataset", iris.target_names)

# Plotar e calcular as métricas para a base de dados Wine
print_metrics("MLPClassifier", "WineDatabase", accuracy_wine, precision_wine, recall_wine)
plot_confusion_matrix(y_test_wine, y_pred_wine, "Confusion Matrix for Wine Dataset", wine.target_names)
