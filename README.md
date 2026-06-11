<div align="center">

<h1>📧 Spam Email Classification</h1>

<p><em>Benchmarking 8 machine learning algorithms on real-world email filtering — with a full desktop GUI and visual performance comparison.</em></p>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

</div>

---

## 🚀 What This Project Does

This system takes the [SpamBase dataset](https://archive.ics.uci.edu/ml/datasets/spambase) (4,601 real emails, 57 features) and runs it through **8 different classifiers** — from classic KNN to a full CNN — then compares every model's Accuracy, Precision, and Recall side by side on a bar chart. Everything is packaged into a **Tkinter desktop app** so you can upload data, trigger training, and generate graphs without writing a single line of code.

**Best result:** MLP achieved the highest score across all three metrics.

---

## 🖥️ Application Preview

<div align="center">

**Main Interface**

<img src="screenshots/1.png" width="75%" alt="Main Application UI"/>

</div>

<br>

<div align="center">

| Dataset Upload | Preprocessing |
|:---:|:---:|
| <img src="screenshots/2.png" width="100%" alt="Dataset Upload"/> | <img src="screenshots/3.png" width="100%" alt="Preprocessing"/> |

</div>

<br>

<div align="center">

**Algorithm Results**

| KNN · Naive Bayes · MLP | SVM · Decision Tree · AdaBoost |
|:---:|:---:|
| <img src="screenshots/4.png" width="100%" alt="KNN Naive Bayes MLP Results"/> | <img src="screenshots/5.png" width="100%" alt="SVM Decision Tree AdaBoost Results"/> |

<img src="screenshots/6.png" width="49%" alt="Random Forest and CNN Results"/>

</div>

<br>

<div align="center">

**Model Comparison Graphs**

| Accuracy | Recall | Precision |
|:---:|:---:|:---:|
| <img src="screenshots/Accuracy.png" width="100%" alt="Accuracy Comparison"/> | <img src="screenshots/Recall.png" width="100%" alt="Recall Comparison"/> | <img src="screenshots/precision.png" width="100%" alt="Precision Comparison"/> |

</div>

---

## ⚙️ Algorithms Implemented

| # | Algorithm | Type |
|:-:|-----------|------|
| 1 | K-Nearest Neighbors | Instance-based |
| 2 | Naive Bayes (BernoulliNB) | Probabilistic |
| 3 | Multilayer Perceptron | Neural Network |
| 4 | Support Vector Machine | Kernel-based |
| 5 | Decision Tree | Tree-based |
| 6 | AdaBoost | Ensemble |
| 7 | Random Forest | Ensemble |
| 8 | Convolutional Neural Network | Deep Learning |

---

## 📊 Evaluation Metrics

| Metric | What it measures |
|--------|-----------------|
| **Accuracy** | Overall correct predictions out of all emails |
| **Precision** | Of emails flagged as spam, how many truly were |
| **Recall** | Of all actual spam, how many were caught |

---

## 📂 Dataset

| Property | Detail |
|----------|--------|
| Name | SpamBase |
| Source | [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/spambase) |
| Size | 4,601 emails · 57 numerical features |
| Split | 80% training / 20% testing |

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| Python 3.8+ | Core language |
| NumPy & Pandas | Data handling |
| Scikit-learn | Classical ML models |
| Keras | CNN / deep learning |
| Matplotlib | Result visualizations |
| Tkinter | Desktop GUI |

---

## ▶️ Getting Started

```bash
# Clone the repo
git clone https://github.com/sanjay-narra/Spam-Email-Classifier.git
cd Spam-Email-Classifier

# Set up virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Launch the app
python SpamFilter.py
```

**Inside the app:**
1. Click **Upload SpamBase Dataset** → select `spambase.data`
2. Click **Preprocess Dataset**
3. Run each algorithm group using its button
4. Click any graph button to compare model performance

---

## 🔮 Roadmap

- [ ] LSTM and BERT-based classifiers
- [ ] Real-time email classification API
- [ ] Email client integration (Gmail / Outlook)
- [ ] Web app deployment

---

## 👨‍💻 Author

<div align="center">

**Narra Sanjay** · B.Tech Computer Science Engineering, 2026

[![GitHub](https://img.shields.io/badge/GitHub-sanjay--narra-181717?style=for-the-badge&logo=github)](https://github.com/sanjay-narra/Spam-Email-Classifier)&nbsp;&nbsp;[![Email](https://img.shields.io/badge/Email-narrasanjayigy7@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:narrasanjayigy7@gmail.com)

</div>

---

<div align="center">
<sub>Licensed under the <a href="LICENSE">MIT License</a></sub>
</div>
