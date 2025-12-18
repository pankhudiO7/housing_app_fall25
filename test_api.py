import requests

data = {"instances":[{"pclass":3,"sex":"male","age":22,"fare":7.25,"embarked":"S"}]}
response = requests.post("http://127.0.0.1:8000/predict", json=data)

print(response.status_code)
print(response.json())

