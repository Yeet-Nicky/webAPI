import requests, json

url= f"https://www.thecocktaildb.com/api/json/v1/1/random.php"
response_json = requests.get(url).json()

with open(r"endpoints (stap 1)\get_random_drink.json", "w") as fp:
    json.dump(response_json, fp)