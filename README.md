# EEG-Based Emotion Recognition using Deep Learning

A deep learning-based system that recognizes human emotions from EEG (Electroencephalogram) signals using a hybrid CNN–LSTM architecture, with real-time deployment via Flask.

---

## 📌 Overview

Emotion recognition plays a crucial role in brain-computer interfaces (BCI), healthcare, and human-computer interaction. Unlike traditional approaches (facial expressions or speech), EEG signals provide direct insights into brain activity, making emotion detection more reliable.

This project proposes a hybrid deep learning model (CNN + LSTM + Attention) to classify emotions from EEG signals with high accuracy and efficiency.

---

## 🚀 Features

- EEG-based emotion classification  
- Hybrid CNN–LSTM architecture  
- Multi-class emotion prediction  
- Real-time prediction using Flask  
- High accuracy and efficient processing  

---

## 🧩 Problem Statement

Traditional emotion recognition systems rely on facial expressions and speech signals, which are subjective and unreliable. EEG-based systems provide direct brain activity but face challenges like noise and complexity.

This project aims to build an accurate and automated EEG-based emotion recognition system.

---

## 🎯 Objectives

- Develop EEG-based emotion classification system  
- Implement CNN + LSTM deep learning model  
- Achieve high accuracy  
- Deploy model using Flask for real-time predictions  

---

## 🏗️ System Architecture

1. Data Collection (GAMEEMO Dataset)  
2. Preprocessing (Noise removal & segmentation)  
3. Feature Extraction using CNN  
4. Temporal Learning using LSTM  
5. Attention Mechanism for feature importance  
6. Emotion Classification  
7. Flask Deployment  

---

## 📊 Dataset

**GAMEEMO Dataset**

EEG channels used:
AF3, AF4, F3, F4, F7, F8, FC5, FC6, O1, O2, P7, P8, T7, T8  

Emotions classified:
- Happy  
- Sad  
- Angry  
- Neutral  

---

## 🤖 Model Architecture

- Convolutional Neural Network (CNN)  
- Long Short-Term Memory (LSTM)  
- Attention Layer  

### Advantages:
- Learns spatial and temporal features  
- Handles complex EEG patterns  
- Improves prediction accuracy  

---

## 📈 Performance Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  

The model shows strong performance across all evaluation metrics.

---

## ⚖️ Comparison with Traditional Models

| Model | Limitation |
|------|------------|
| SVM | Manual feature extraction |
| KNN | Poor scalability |
| Random Forest | Limited temporal learning |

**Proposed Model Advantages:**
- Automatic feature extraction  
- Better accuracy  
- Handles temporal dependencies  

---

## 🖥️ Deployment

The model is deployed using Flask.

### Functionality:
- Input EEG features  
- Predict emotion  
- Display confidence score  

---

## 📌 Results

- High classification accuracy  
- Reliable predictions  
- Efficient real-time performance  

---

## 🔮 Future Scope

- Real-time EEG data acquisition  
- Integration with wearable devices  
- Multimodal emotion recognition (EEG + Facial + Speech)  
- Transformer-based models  

---

## 👨‍💻 Team Members

- C. Venkata Sunil  
- T. Venu Madhava  
- B. Rahithya  

---

## 👩‍🏫 Guide

Dr. K. Samunnisa  
Assistant Professor, CSE (Data Science)

---

## 🏫 Institution

Rajeev Gandhi Memorial College of Engineering & Technology  
Department of CSE (Data Science)

---

## ⚙️ Installation & Usage

bash
# Clone repository
git clone https://github.com/VenkataSunil18/EEG-Based-Emotion-Recognition.git

# Go to project folder
cd eeg-emotion-recognition

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
