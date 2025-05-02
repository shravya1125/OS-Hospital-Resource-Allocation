from flask import Flask
from core.routes import init_routes

app = Flask(__name__)
init_routes(app)

if __name__ == '__main__':
    print("✅ Hospital Resource Management API running on http://127.0.0.1:5000")
    app.run(debug=True)
