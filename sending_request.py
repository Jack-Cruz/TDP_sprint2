import json
import requests

print('Hello world!')

def run_prediction(data, headers, endpoint):
    json_response = requests.post(endpoint, data=data, headers=headers)
    prediction = json.loads(json_response.text)
    return prediction

x = [10.0, 20.0, 5.0]
endpoint = 'http://localhost:8501/v1/models/half_plus_two:predict'
data = json.dumps({"instances": x})
headers = {"content-type": "application/json"}
response = run_prediction(data, headers, endpoint)
print(response)
