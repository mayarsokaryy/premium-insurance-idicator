# 🏥 Insurance Premium Estimator

**Student:** Mayar Sheri Elsakary  
**Project No:** 60  
**Project Title:** Insurance Premium Estimator  
**Category:** Tabular Data - Regression  
**Deployment:** Web App

---

## 📁 Project Structure

```
insurance_estimator/
│
├── insurance.csv          ← البيانات (Data)
├── train_model.py         ← كود تدريب النموذج
├── model.pkl              ← النموذج المحفوظ (يتم إنشاؤه تلقائياً)
└── app.py                 ← الـ Web App (Streamlit)
```

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install pandas scikit-learn streamlit numpy
```

### 2. Download Dataset
Download `insurance.csv` from [Kaggle Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) and place it in this directory.

### 3. Train the Model
```bash
python train_model.py
```
This will create `model.pkl`

### 4. Run the Web App
```bash
streamlit run app.py
```
Open browser at `http://localhost:8501`

---

## 📊 Dataset Columns

| Column | Description | Type |
|--------|------------|------|
| age | العمر | Integer |
| sex | الجنس (male/female) | Categorical |
| bmi | مؤشر كتلة الجسم | Float |
| children | عدد الأطفال | Integer |
| smoker | هل يدخن (yes/no) | Categorical |
| region | المنطقة الجغرافية | Categorical |
| charges | **تكلفة التأمين (Target)** | Float |

---

## 🤖 Model Performance

- **Algorithm:** Random Forest Regressor
- **Expected R² Score:** ~0.87
- **Training/Test Split:** 80/20

---

## 🌐 Deployment

### Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy your app
4. Share the live URL!

---
