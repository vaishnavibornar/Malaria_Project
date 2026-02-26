# 🦠 Malaria Detection Using Deep Learning

## 📌 Project Overview
Malaria is one of the world’s deadliest infectious diseases, affecting millions of people every year. Early and accurate detection is critical for proper treatment.

This project uses **Deep Learning (CNN + Transfer Learning)** to automatically detect malaria parasites from microscopic blood smear cell images.

The model classifies blood cells into:

- 🧬 **Parasitized (Infected)**
- 🩸 **Uninfected (Healthy)**

The system is designed to assist medical professionals by providing fast and scalable malaria detection.

---

## 🚀 Features

✔ Deep Learning based image classification  
✔ Transfer Learning using **MobileNetV2**  
✔ Automatic dataset loading using ImageDataGenerator  
✔ Training & Validation split  
✔ Accuracy visualization  
✔ Saved trained model  
✔ Flask web application (image upload & prediction)

---

## 🧠 Tech Stack

- Python
- TensorFlow / Keras
- MobileNetV2 (Transfer Learning)
- NumPy, Matplotlib
- Flask
- Jupyter Notebook
- Anaconda Environment

---

## 📂 Project Structure
Malaria_Project/
│
├── app.py # Flask backend
├── train_model.ipynb # Model training notebook
├── templates/ # HTML files
├── static/ # CSS / assets
├── malaria_model.keras # Trained model (local)
├── dataset/ # Dataset (ignored from GitHub)
└── README.md

---

## 📊 Dataset

Dataset used: **Cell Images for Detecting Malaria**

- Source: Kaggle  
- Link: https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria

### Dataset Details

- Total images: 27,558
- Image Type: Microscopic thin blood smear images
- Classes:
  - Parasitized
  - Uninfected

---

## ⚙️ Model Architecture

Transfer Learning with **MobileNetV2**
MobileNetV2 (Frozen Layers)
↓
GlobalAveragePooling2D
↓
Dense (Sigmoid Output)

---

## 📈 Training Results

- Training Accuracy: ~93%
- Validation Accuracy: ~92%

Accuracy Graph:

![Training Graph](static/accuracy.png)

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash id="o4jty4"
git clone https://github.com/vaishnavibornar/Malaria_Project.git
cd Malaria_Project
