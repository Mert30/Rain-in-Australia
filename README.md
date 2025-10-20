# Rain Prediction in Australia ☔

This project predicts whether it will rain tomorrow in Australia based on weather data. Users can input weather features through a user-friendly **Streamlit** interface, and the app will predict rain using a trained **Logistic Regression** model.

---

## Dataset

The dataset was obtained from **Kaggle** and contains various weather features such as temperature, rainfall, wind, humidity, pressure, and cloud coverage for different locations in Australia.

---

## Data Preprocessing

- Exploratory Data Analysis (EDA) was performed to understand the dataset.
- Missing values were handled and categorical variables were encoded.
- Numerical features were scaled using **StandardScaler**.
- Categorical features were transformed using **One-Hot Encoding** (dummies).

---

## Model

- **Algorithm:** Logistic Regression  
- **Accuracy:** 0.85  
- The model was trained on the processed dataset and saved using **joblib** for deployment.

---

## Streamlit App

- Users can input weather features such as temperature, rainfall, wind speed/direction, humidity, pressure, cloud coverage, and date.
- The app predicts if it will rain tomorrow (`Yes`/`No`).
- Input data is processed in the same way as during training to ensure correct predictions.
- The app is interactive and visually appealing, built with **Streamlit**.

---

## Deployment

- The project is deployed on **Streamlit Cloud**, accessible via a web interface.
- Users can try different inputs to see the rain prediction in real-time.

---

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Mert30/Rain-in-Australia.git
cd Rain-in-Australia
