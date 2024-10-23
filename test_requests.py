import requests

url = "http://20.61.171.129:8001/predict"
data = {"size": 130, "bedrooms": 3, "garden": 1}
response = requests.post(url, json=data)
print(response.json())
