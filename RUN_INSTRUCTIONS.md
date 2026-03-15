# Car Resale Price Prediction – Run Instructions

## Step 1: Virtual environment activate karein

**PowerShell:**
```powershell
cd "d:\MyPersonel-main\CV_Project\CarResalePricePredictionSystem-main"
.\myenv\Scripts\Activate.ps1
```

**CMD:**
```cmd
cd "d:\MyPersonel-main\CV_Project\CarResalePricePredictionSystem-main"
myenv\Scripts\activate.bat
```

## Step 2: Dependencies install karein (agar pehle nahi ki)

```powershell
pip install -r requirements.txt
```

## Step 3: Model train karein (sirf pehli dafa ya jab model nahi hai)

Project **root** folder se:

```powershell
python Muawwaz.py
```

Yeh script `Gradient Boosting_model.pkl` bana degi (agar `car_data.csv` maujood hai).

## Step 4: Flask API run karein

```powershell
cd project
python app.py
```

Browser mein open karein: **http://127.0.0.1:5000**

- Home: http://127.0.0.1:5000/
- Prediction API: POST http://127.0.0.1:5000/predict (JSON body ke sath)

---

**Shortcut (agar model pehle se hai):**

1. `.\myenv\Scripts\Activate.ps1`
2. `cd project`
3. `python app.py`
