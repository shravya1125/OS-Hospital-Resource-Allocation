import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ------------------- A. Machine Learning Risk Prioritization -------------------
data = pd.DataFrame({
    'fever': [1, 0, 1, 1, 0],
    'bp_low': [0, 1, 1, 0, 1],
    'diabetes': [1, 1, 0, 1, 0],
    'risk': [1, 1, 1, 1, 0]
})

X = data[['fever', 'bp_low', 'diabetes']]
y = data['risk']
model = DecisionTreeClassifier()
model.fit(X, y)

def classify_risk(patient_data):
    patient_df = pd.DataFrame([patient_data])
    return model.predict(patient_df)[0]
