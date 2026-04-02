import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_data(fill_name):
    data = pd.read_excel(fill_name)
    return data


def fill_null_column(df, column):
    not_null_values = df[column].fillna(df[column].mean())
    return not_null_values


def normalization(df, column, new_min=0, new_max=1):
    if column not in df:
        raise ValueError(f"Column '{column}' not found in the DataFrame.")

    max_value = df[column].max()
    min_value = df[column].min()

    # Perform Min-Max scaling
    df[column] = ((df[column] - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min

    return df


def train_test_split(df, train_percent, features, classes, prediction_class):
    df = df[df['Class'].isin(classes)]
    print(df)

    class_mapping = {class_name: label for label, class_name in enumerate(classes)}

    df.loc[:, prediction_class] = df[prediction_class].map(class_mapping)

    # print('--------------------------------------------------------')
    # print(df)
    # print('--------------------------------------------------------')

    train_size = int(df.shape[0] * train_percent)
    print(train_size)

    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    print(shuffled_df)

    X = shuffled_df[features]
    y = shuffled_df[prediction_class]
    # print(X)
    # print('--------------------------------------------------------')
    # print(y)
    # print('--------------------------------------------------------')
    train_data_x = X.iloc[:train_size]
    train_data_y = y.iloc[:train_size]
    test_data_x = X.iloc[train_size:]
    test_data_y = y.iloc[train_size:]

    return train_data_x, train_data_y, test_data_x, test_data_y


def signum(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def mean_squared_error(y_actual, y_predicted):
    if len(y_actual) != len(y_predicted):
        raise ValueError("Input lists must have the same length")
    squared_errors = [(y_actual[i] - y_predicted[i]) ** 2 for i in range(len(y_actual))]
    mse = sum(squared_errors) / len(y_actual)
    return mse


def perceptron_fit(features, label, learning_rate, num_epochs, add_bias):
    num_samples, num_features = features.shape
    weights = np.zeros(num_features)
    bias = 0

    names = label.unique()
    label = label.replace(names[0], 1)
    label = label.replace(names[1], -1)

    for epoch in range(num_epochs):
        for i in range(num_samples):
            if add_bias:
                linear_output = np.dot(features.iloc[i], weights) + bias
            else:
                linear_output = np.dot(features.iloc[i], weights)

            y_predicted = signum(linear_output)

            if y_predicted != label.iloc[i]:
                loss = label.iloc[i] - y_predicted
                update_value = learning_rate * loss
                weights += update_value * features.iloc[i]

                if add_bias:
                    bias += update_value  # X0 = 1

    return weights, bias


def adaline_fit(features, label, learning_rate, num_epochs, mse_threshold, add_bias):
    print(features)
    num_samples, num_features = features.shape
    weights = np.zeros(num_features)
    bias = 0

    names = label.unique()
    label = label.replace(names[0], -1)
    label = label.replace(names[1], 1)
    print(features.shape)

    for epoch in range(num_epochs):
        mse = 0
        for i in range(num_samples):
            if add_bias:
                print(weights[0])
                print(weights[1])
                linear_output = np.dot(features.iloc[i], weights) + bias
            else:
                print(weights[0])
                print(weights[1])
                linear_output = np.dot(features.iloc[i], weights)

            # print('----------------')
            # print(type(linear_output))
            # print(linear_output)

            # print('----------------')
            # print('----------------')
            # print(type(linear_output))
            # print(linear_output)
            # print(label.iloc[i])

            error = label.iloc[i] - linear_output
            update_value = learning_rate * error
            weights += update_value * features.iloc[i]

            if add_bias:
                bias += update_value  # X0 = 1

            mse += error ** 2
        # add for loop to multiply the final weights with the features and calc the final mse
        mse /= (2 * num_samples)
        print(f'Epoch {epoch + 1}: MSE = {mse}')

        if mse <= mse_threshold:
            break
    print("bias : ", bias)
    print(features.shape)
    print(weights)
    return weights, bias


def predict_algorithm(X_test, weights, bias):
    num_samples = X_test.shape[0]
    predicted_labels = []

    for i in range(num_samples):
        if bias > 0:
            linear_output = np.dot(X_test.iloc[i], weights) + bias
        else:
            linear_output = np.dot(X_test.iloc[i], weights)

        predicted_label = signum(linear_output)
        predicted_labels.append(predicted_label)

    return predicted_labels


def confusion_matrix(actual_labels, predicted_labels):
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    names = actual_labels.unique()
    actual_labels = actual_labels.replace(names[0], -1)
    actual_labels = actual_labels.replace(names[1], 1)
    actual_labels = actual_labels.tolist()

    for i in range(len(actual_labels)):
        if (actual_labels[i] == 1) & (predicted_labels[i]) == 1:
            true_positives += 1
        if (actual_labels[i] == -1) & (predicted_labels[i]) == -1:
            true_negatives += 1
        if (actual_labels[i] == -1) & (predicted_labels[i]) == 1:
            false_positives += 1
        if (actual_labels[i] == 1) & (predicted_labels[i]) == -1:
            false_negatives += 1

    return true_positives, true_negatives, false_positives, false_negatives


def accuracy(confusion_matrix):
    true_positives, true_negatives, false_positives, false_negatives = confusion_matrix
    total = true_positives + true_negatives + false_positives + false_negatives

    if total == 0:
        accuracy = 0.0
    else:
        accuracy = (true_positives + true_negatives) / total

    return accuracy


def plot_algorithm(features, weights, bias):
    # X1class1 = features.iloc[0:20, 0:1]
    # X1class2 = features.iloc[20:, 0:1]
    # X2class1 = features.iloc[0:20, 1:]
    # X2class2 = features.iloc[20:, 1:]
    # w1 = weights[0]
    # w2 = weights[1]
    # b = bias
    #
    # max_value1 = features.iloc[:, 0].max().item()
    # max_value2 = features.iloc[:, 1].max().item()
    # max_value = max(max_value1, max_value2)
    #
    # x1 = np.linspace(0, max_value, 2)
    # x2 = (-w1 * x1 - b) / w2
    # plt.figure()
    # plt.plot(x1, x2, label='x1w1 + x2w2 + b = 0', color='red')
    # plt.scatter(X1class1, X2class1, color='blue', label='Class1')
    # plt.scatter(X1class2, X2class2, color='red', label='Class2')
    # plt.xlabel('x1')
    # plt.ylabel('x2')
    # plt.legend()
    # plt.title('Line Equation: w1x1 + w2x2 + b = 0')
    # plt.grid(True)
    # plt.axhline(0, color='black', lw=0.5)
    # plt.axvline(0, color='black', lw=0.5)
    # plt.show()

    feature1 = features.iloc[:, 0]
    print(feature1.shape)
    feature2 = features.iloc[:, 1]
    print(feature2.shape)

    print(weights[0])
    print(weights[1])
    print(weights)

    plt.scatter(feature1[0:20], feature2[0:20], label='Class 1', c='b', marker='o')

    plt.scatter(feature1[20:], feature2[20:], label='Class -1', c='r', marker='o')

    x_values = np.linspace(0, feature1.max(), 100)

    y_values = (-weights[0] * x_values - bias) / weights[1]

    plt.plot(x_values, y_values, 'g--', label='Decision Boundary')

    plt.xlabel(f'Feature {0}')
    plt.ylabel(f'Feature {1}')
    plt.legend(loc='best')

    plt.title('Line Equation: w1x1 + w2x2 + b = 0')
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)

    plt.show()
