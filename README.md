
# Crop Prediction

This project is a **web-based application** that predicts the most suitable crop for farming based on user-provided soil and environmental parameters. It uses a machine learning model trained on a dataset of crop recommendations.

---

## 🌟 Features

- **User Input Form**: Enter values for Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.
- **Crop Recommendation**: Predicts the best crop based on the input parameters.
- **Interactive Web Interface**: Built using Flask and HTML templates.

---

## 📂 Project Structure
```
.
├── app.py                          # Flask application
├── crop_prediction.py              # Script to train and save the model
├── crop_recommendation_model.pkl   # Trained machine learning model
├── Crop_recommendation.csv         # Dataset used for training
├── README.md                       # Project documentation
├── static/
│   └── style.css                   # CSS for styling the web interface
└── templates/
    └── index.html                  # HTML template for the web interface
```

---

## ✅ Requirements

- Python 3.x
- Flask
- NumPy
- Pandas
- Scikit-learn

---

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Cropprediction
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure the dataset `Crop_recommendation.csv` is in the root directory.

---

## ▶️ Usage

1. Train the model (if not already trained):
```bash
python crop_prediction.py
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

4. Enter the required parameters in the form and get the crop recommendation.

---

## 📊 Dataset

The dataset `Crop_recommendation.csv` contains information about various crops and the environmental conditions suitable for their growth.

---

## 🧠 Model

The machine learning model is a **Random Forest Classifier** trained on the dataset. It predicts the most suitable crop based on the input parameters.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

- Dataset source: [Kaggle](https://www.kaggle.com/)
- Libraries: Flask, NumPy, Pandas, Scikit-learn
