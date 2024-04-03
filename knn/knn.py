import csv
import time
import random
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


def euclidean_distance(subj1, subj2):
    distance = sum((a - b) ** 2 for a, b in zip(subj1, subj2[:-1]))
    return distance ** 0.5


def predict_class(point, data_train, k):
    distances_and_classes = [(euclidean_distance(point, train_point), train_point[-1]) for train_point in data_train]
    distances_and_classes.sort(key=lambda x: x[0])
    nearest_classes = [cls for _, cls in distances_and_classes[:k]]

    class_counts = {}
    for cls in nearest_classes:
        class_counts[cls] = class_counts.get(cls, 0) + 1

    return max(class_counts, key=class_counts.get)


def calculate_accuracy(data_test, data_train, k):

    y_true = [point[-1] for point in data_test]
    y_pred = [predict_class(point, data_train, k) for point in data_test]

    accuracy = accuracy_score(y_true, y_pred) * 100
    recall = recall_score(y_true, y_pred, average='weighted') * 100
    precision = precision_score(y_true, y_pred, average='weighted') * 100

    return accuracy, recall, precision


def split_data(dataset, test_percentage):
    random.shuffle(dataset)
    test_size = int(len(dataset) * test_percentage)
    data_test = dataset[:test_size]
    data_train = dataset[test_size:]
    return data_train, data_test


def main():
    start_time = time.time()

    # Carrega o conjunto de dados
    file_path = "knn/iris/Iris.csv"
    dataset = read_dataset(file_path)

    # Divide o conjunto de dados em treinamento e teste
    test_percentage = 0.2
    data_train, data_test = split_data(dataset, test_percentage)

    k_values = [1, 3, 5, 7]
    max_accuracy = 0
    best_k = 1

    print("\nDataset lido")
    print("-------------------------------------------------------")
    print("Algoritmo do KNN para classificação com a IrisDatabase")
    print("-------------------------------------------------------")

    # Avalia o modelo para diferentes valores de k
    for k in k_values:
        accuracy, recall, precision = calculate_accuracy(data_test, data_train, k)
        print(f"k = {k} | Precisão: {accuracy:.2f}% | Revocação: {recall:.2f}% | Acurácia: {precision:.2f}%")
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            best_k = k

    print(f"\nMelhor valor de K: {best_k} \nPrecisão máxima: {max_accuracy:.2f}%")
    end_time = time.time()
    print(f"\nTempo de execução: {end_time - start_time:.3f} segundos")


if __name__ == "__main__":
    main()
