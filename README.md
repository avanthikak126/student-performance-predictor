# Student Performance Predictor

A beginner-friendly Machine Learning project that predicts a student's expected exam marks based on:
- Study hours per day
- Attendance percentage
- Previous exam marks

## Project Structure

```
student-performance-predictor/
├── dataset.csv        # Sample student data
├── train_model.py     # Trains and saves the ML model
├── app.py             # Streamlit web app
├── requirements.txt   # Python dependencies
└── README.md
```

## Setup & Run Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the model

Run this once to train the Linear Regression model and save it as `model.pkl`:

```bash
python train_model.py
```

You should see: `Model trained and saved as model.pkl`

### 3. Launch the web app

```bash
streamlit run app.py
```

A browser window will open automatically. Use the sliders to enter student details and click **Predict Marks** to see the result.

## How It Works

1. `dataset.csv` contains 25 sample student records with realistic data.
2. `train_model.py` loads the dataset, trains a **Linear Regression** model using scikit-learn, and saves it with joblib.
3. `app.py` loads the saved model and provides a simple Streamlit UI for predictions.
