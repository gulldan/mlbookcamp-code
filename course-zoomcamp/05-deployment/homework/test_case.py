import requests

url = "http://localhost:1234/predict"

q4 = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
print('q4 - ', requests.post(url, json=q4).json())

q6 = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
print('q6 - ', requests.post(url, json=q6).json())
