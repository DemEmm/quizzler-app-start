import requests

api_param = {
    "amount" : 10,
    "type": "boolean"
}
try:
    request_my = requests.get(url="https://opentdb.com/api.php",params=api_param)
    request_my.raise_for_status()
    # request_my.status_code
    data = request_my.json()
except:
    raise print("Error: Connection problem with api endpoint :_(")
else:
    question_data = data["results"]
