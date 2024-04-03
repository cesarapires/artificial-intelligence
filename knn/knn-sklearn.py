import csv
import time
import random

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score


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


def main():
    start_time = time.time()  # Marca o início da execução

    # Lê o conjunto de dados do arquivo CSV
    file_path = "knn/iris/Iris.csv"
    dataset = read_dataset(file_path)
    random.shuffle(dataset)  # Embaralha os dados

    # Separa as features (X) e os rótulos (y)
    X = [row[:-1] for row in dataset]
    y = [row[-1] for row in dataset]

    # Divide os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Padroniza as features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    k_values = [1, 3, 5, 7]
    max_accuracy = 0
    best_k = 1

    print("\nDataset lido")
    print("-------------------------------------------------------")
    print("Algoritmo do KNN para classificação com a IrisDatabase")
    print("-------------------------------------------------------")

    # Para cada valor de k, treina o classificador KNN e avalia a precisão, revocação e acurácia
    for k in k_values:
        # Inicializa o classificador KNN com o valor de k atual
        knn_classifier = KNeighborsClassifier(n_neighbors=k)

        # Treina o classificador KNN com os dados de treinamento
        knn_classifier.fit(X_train, y_train)
        
        # Faz previsões com os dados de teste
        y_pred = knn_classifier.predict(X_test)

        # Calcula a precisão do classificador
        accuracy = accuracy_score(y_test, y_pred) * 100

        # Calcula a revocação do classificador
        recall = recall_score(y_test, y_pred, average='weighted') * 100

        # Calcula a precisão do classificador
        precision = precision_score(y_test, y_pred, average='weighted') * 100

        # Imprime a precisão, revocação e acurácia para o valor de k atual
        print(f"k = {k} | Precisão: {accuracy:.2f}% | Revocação: {recall:.2f}% | Acurácia: {precision:.2f}%")

        # Atualiza o melhor valor de k se a precisão atual for maior que a máxima anterior
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            best_k = k

    # Imprime o melhor valor de k e sua precisão correspondente
    print(f"\nMelhor valor de k: {best_k} \nPrecisão máxima: {max_accuracy:.2f}%")

    end_time = time.time()  # Marca o fim da execução
    print(f"\nTempo de execução: {end_time - start_time:.3f} segundos")


if __name__ == "__main__":
    main()
