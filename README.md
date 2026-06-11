# 📧 Spam Email Classification using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-orange?style=for-the-badge&logo=scikit-learn)
![Keras](https://img.shields.io/badge/Keras-red?style=for-the-badge&logo=keras)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🖼️ Screenshots

### Main Application
![Main GUI](screenshots/1.png)

### Dataset & Preprocessing
![Dataset Upload](screenshots/2.png)
![Preprocessing](screenshots/3.png)

### Algorithm Results
![KNN, Naive Bayes & MLP](screenshots/4.png)
![SVM, Decision Tree & AdaBoost](screenshots/5.png)
![Random Forest & CNN](screenshots/6.png)

### Comparison Graphs
![Accuracy Graph](screenshots/Accuracy.png)
![Recall Graph](screenshots/Recall.png)
![Precision Graph](screenshots/precision.png)

---

## 📌 Project Overview

This project implements a Spam Email Classification System using multiple Machine Learning algorithms to classify emails as **Spam** or **Ham (Not Spam)**.

The system evaluates and compares different classifiers based on Accuracy, Precision, and Recall, and visualizes their performance using comparison graphs. The project is based on the SpamBase dataset and demonstrates how machine learning techniques can be applied to real-world email filtering problems.

---

## 🎯 Objective

- Detect and classify incoming emails as Spam or Ham using supervised learning techniques
- Compare the performance of multiple ML algorithms
- Identify the best performing classifier based on evaluation metrics

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| NumPy & Pandas | Data handling |
| Scikit-learn | ML algorithms |
| Keras | CNN / Deep learning |
| Matplotlib | Graphs & visualization |
| Tkinter | GUI application |

---

## 📂 Dataset

- **Name:** SpamBase
- **Source:** UCI Machine Learning Repository
- **Records:** 4,601 emails
- **Features:** 57 numerical attributes + 1 class label
- **Split:** 80% Training / 20% Testing

---

## ⚙️ Machine Learning Algorithms Implemented

| # | Algorithm |
|---|-----------|
| 1 | K-Nearest Neighbors (KNN) |
| 2 | Naive Bayes (BernoulliNB) |
| 3 | Multilayer Perceptron (MLP) |
| 4 | Support Vector Machine (SVM) |
| 5 | Decision Tree |
| 6 | AdaBoost |
| 7 | Random Forest |
| 8 | Convolutional Neural Network (CNN) |

---

## 📊 Evaluation Metrics

Each model is evaluated using:
- **Accuracy** — overall correct predictions
- **Precision** — how many predicted spams are actually spam
- **Recall** — how many actual spams were correctly caught

Graphs are generated to compare all algorithms side by side.

---

## 🖥️ Application Flow

1. Upload SpamBase Dataset
2. Preprocess dataset and split into train/test
3. Run KNN, Naive Bayes, and MLP algorithms
4. Run SVM, Decision Tree, and AdaBoost algorithms
5. Run Random Forest and CNN models
6. Generate Accuracy comparison graph
7. Generate Recall comparison graph
8. Generate Precision comparison graph

---

## ▶️ How to Run the Project

### Step 1 — Clone the repository
```bash
git clone https://github.com/sanjay-narra/Spam-Email-Classifier.git
cd Spam-Email-Classifier
```

### Step 2 — Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the application
```bash
python SpamFilter.py
```

### Step 5 — Use the GUI
- Click **Upload SpamBase Dataset** and select `spambase.data`
- Click **Preprocess Dataset**
- Run algorithms using respective buttons
- Generate comparison graphs

---

## 🏆 Results

**MLP (Multilayer Perceptron)** achieved the best performance with the highest Accuracy, Precision, and Recall among all classifiers tested.

---

## 🔮 Future Enhancements

- [ ] Implement advanced deep learning models (LSTM, BERT)
- [ ] Add real-time email classification
- [ ] Integrate with email clients
- [ ] Improve GUI design and visualization
- [ ] Deploy as a web application

---

## 👨‍💻 Author
**Narra Sanjay** — B.Tech Computer Science Engineering (2026)  
- 💻 GitHub: [github.com/sanjay-narra](https://github.com/sanjay-narra/Spam-Email-Classifier)  
- 📧 Email: narrasanjayigy7@gmail.com  
