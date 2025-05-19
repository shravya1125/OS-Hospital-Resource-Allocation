from flask import Flask, render_template, request
from core.model import predict_risk
from core.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        bp = int(request.form['bp'])
        heart_rate = int(request.form['heart_rate'])
        comorbidity_score = int(request.form['comorbidity_score'])
        input_data = {
            'age': age,
            'bp': bp,
            'heart_rate': heart_rate,
            'comorbidity_score': comorbidity_score
        }
        risk, prob = predict_risk(input_data)
        return render_template('result.html', risk=risk, probability=f"{prob:.2f}")
    except Exception as e:
        return render_template('result.html', risk="Error", probability=str(e))

if __name__ == "__main__":
    app.run(debug=True)
