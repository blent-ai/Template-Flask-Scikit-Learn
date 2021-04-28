import pandas as pd
from flask import Flask, request, jsonify
from src.model import load_artifacts, predict

app = Flask(__name__)

load_artifacts()

@app.route('/', methods=['GET'])
def route_home():
    return "OK !", 200

@app.route('/predict', methods=['POST'])
def route_predict():
    body = request.get_json()
    df = pd.DataFrame.from_dict(body)
    results = {'prices': list(predict(df).flatten())}
    return jsonify(results), 200

if __name__ == "__main__":
    app.run(port=5000)