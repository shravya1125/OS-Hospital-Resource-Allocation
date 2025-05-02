# 🚑 Dynamic Resource Allocation Framework for Hospital Management


## 🧠 Description

An **intelligent hospital resource management system** that leverages **machine learning** for risk-aware patient triaging, **interrupt-driven emergency scheduling**, and a **real-time dashboard** built with Flask and Chart.js.


## 🚀 Features

* 🔬 **ML-Based Risk Prediction**
  Uses medical indicators (fever, low BP, diabetes) to predict patient risk.

* 📊 **Priority-Based Resource Allocation**
  Allocates ICU beds, ventilators, and doctors to high-risk patients based on classification.

* ⚡ **Interrupt-Driven Emergency Handling**
  Critical patients can override the normal allocation flow.

* 📈 **Live Dashboard**
  Interactive interface to monitor resource availability and patient risk scores in real-time.


## 🛠️ Tech Stack

* **Backend**: Python, Flask, threading
* **Machine Learning**: scikit-learn, Pandas, NumPy
* **Frontend**: HTML, CSS, JavaScript, Chart.js
* **Rendering**: Flask templates (`Jinja2`)


## 📂 Folder Structure

.
├── app.py                  # Entry point for Flask app
├── images/
│   └── screenshot.png
├── core/                   # Core logic and API routes
│   ├── model.py            # ML model setup and prediction
│   ├── resource_manager.py # Resource allocation and emergency logic
│   └── routes.py           # Flask routes
├── templates/
│   └── dash.html           # Dashboard UI
├── requirements.txt        # Python dependencies
└── README.md


## 📦 Installation & Setup

1. **Clone the repository**

   git clone https://github.com/your-username/OS-Hospital-Resource-Allocation.git
   cd OS-Hospital-Resource-Allocation
   
2. **Install dependencies**

   pip install -r requirements.txt

3. **Run the Flask App**

   python app.py

4. **View the Dashboard**
   Open your browser and go to:
   👉 [http://127.0.0.1:5000/dashboard](http://127.0.0.1:5000/dashboard)

## 📸 Screenshot

Here is a screenshot of the dashboard:

![Dashboard Screenshot](images/screenshot.png)

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

