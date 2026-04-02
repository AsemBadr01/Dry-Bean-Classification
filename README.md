# 🧠 Neural Network Feature Analysis: Perceptron vs Adaline

This project presents a comparative analysis between two fundamental neural network algorithms:

- Perceptron
- Adaline (Adaptive Linear Neuron)

The goal is to evaluate their performance on a binary classification task using different feature combinations.

---

## 📌 Problem Statement

Classify two classes:
- BOMBAY
- CALI

Using multiple combinations of extracted features such as:
- Area
- Perimeter
- Major Axis Length
- Minor Axis Length
- Roundness

---

## ⚙️ Algorithms Used

### 🔹 Perceptron
- A linear binary classifier
- Uses a step activation function
- Updated based on classification errors

### 🔹 Adaline
- Uses linear activation
- Optimizes weights using gradient descent
- More stable compared to Perceptron

---

## 📊 Experiments & Results

### 🔸 Perceptron Results

| Features Used                  | Accuracy |
|------------------------------|----------|
| Area + Perimeter             | 0.40     |
| Area + MajorAxisLength       | 0.525 ✅ |
| Area + MinorAxisLength       | 0.45     |
| Area + Roundness             | 0.425    |
| MinorAxisLength + Roundness  | 0.50     |

✔ **Best Perceptron Accuracy:**  
**0.525 using (Area + MajorAxisLength)**

---

### 🔸 Adaline Results

| Features Used                  | Accuracy |
|------------------------------|----------|
| Area + Perimeter             | 0.525    |
| Area + MajorAxisLength       | 0.475    |
| Area + MinorAxisLength       | 0.425    |
| Area + Roundness             | 0.55     |
| Perimeter + MajorAxisLength  | 0.60 ✅ |

✔ **Best Adaline Accuracy:**  
**0.60 using (Perimeter + MajorAxisLength)**

---

## 📈 Key Insights

- Adaline outperformed Perceptron in most feature combinations
- Feature selection has a significant impact on model performance
- Linear models can still provide meaningful results with proper features
- Perimeter + MajorAxisLength is the most informative feature pair

---

## 🛠️ Tech Stack

- Python (assumed)
- NumPy
- Basic Machine Learning concepts

---

## 🚀 Future Improvements

- Apply non-linear models (e.g., Neural Networks, SVM)
- Perform feature scaling and normalization
- Use larger dataset for better generalization
- Implement cross-validation

---

## 👨‍💻 Author

Assem Badr
  AI Engineer

---

## 📬 Contact

- LinkedIn: www.linkedin.com/in/assem-badr/
