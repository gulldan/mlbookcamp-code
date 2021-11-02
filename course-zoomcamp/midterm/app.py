import pickle
from os import environ
from flask import Flask, request, jsonify

model_file = environ.get("FILE_PATH", 'xgboost.pickle.dat')

with open(model_file, 'rb') as f_in:
    _model = pickle.load(f_in)

app = Flask('midterm')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    y_pred = _model.predict(data).clip(0, 20)

    result = {
        'price': y_pred
    }

    return jsonify(result)


@app.route('/test', methods=['GET'])
def test():
    result = {
        'debug_info': 'ok',
        'price': 1
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=1234)
