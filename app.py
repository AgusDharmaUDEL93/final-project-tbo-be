from flask import Flask
from flask_cors import CORS
from routes.config import configRoute

app = Flask(__name__)
CORS(app)

configRoute(app)

if __name__ == "__main__":
    app.run(debug=True)