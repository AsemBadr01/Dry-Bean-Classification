from UI import DynamicFunctions as dyF


def adaline_algorithm(num_epochs, learning_rate, mse_threshold, bias_flag, feature1_value, feature2_value, classes_value):
    data = dyF.read_data('Dataset/Dry_Bean_Dataset.xlsx')

    X = data.columns[:5]
    # print(X)
    # print(y)
    # print(data.columns.shape)

    for column in X:
        data[column] = dyF.fill_null_column(data, column)
        dyF.normalization(data, column)

    column_names = ['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength', 'roundnes']
    feature1_index = feature1_value
    feature2_index = feature2_value

    if feature1_index > 0 and feature2_index > 0:
        chosen_features = [column_names[feature1_index - 1], column_names[feature2_index - 1]]
    else:
        raise ValueError('You must enter 2 features for the algorithm to work')

    # Class names: #BOMBAY  #CALI  #SIRA
    classes_index = classes_value
    class_mappings = {
        1: ['BOMBAY', 'CALI'],
        2: ['BOMBAY', 'SIRA'],
        3: ['CALI', 'SIRA']
    }
    chosen_classes = class_mappings.get(classes_index, ['BOMBAY', 'CALI'])

    X_train, y_train, X_test, y_test = dyF.train_test_split(data, 0.6,
                                                            features=chosen_features,
                                                            classes=chosen_classes,
                                                            prediction_class='Class')
    print(X_train)
    print(y_train)
    print(X_test)
    print(y_test)

    weights, bias = dyF.adaline_fit(X_train, y_train, learning_rate, num_epochs, mse_threshold, bias_flag)

    predicted_labels = dyF.predict_algorithm(X_test, weights, bias)
    confusion_matrix = dyF.confusion_matrix(y_test, predicted_labels)
    acc = dyF.accuracy(confusion_matrix)
    print("Confusion Matrix:\n",
          "true_positives =", confusion_matrix[0],
          "true_negatives =", confusion_matrix[1],
          "\nfalse_positives =", confusion_matrix[2],
          "false_negatives =", confusion_matrix[3])

    print("Accuracy:", acc)

    dyF.plot_algorithm(X_test, weights, bias)
