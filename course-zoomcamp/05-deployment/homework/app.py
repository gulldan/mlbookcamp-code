import pickle
from os import environ
from flask import Flask, request, jsonify

dv_file = environ.get("FILE_PATH", 'dv.bin')
model_file = environ.get("FILE_PATH", 'model1.bin')

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)
with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('homework-05')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    return jsonify(result)


@app.route('/test', methods=['GET'])
def test():
    customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    result = {
        'debug_info': 'ok',
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=1234)
