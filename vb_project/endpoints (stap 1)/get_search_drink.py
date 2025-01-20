import requests, json

""" OPGELET!
Er zijn twee json-bestanden voor dit endpoint.
Dit omdat is opgevallen dat de structuur er anders uit ziet als geen drankje gevonden is.
"""

# Om te searchen, vul na 's=' de input van de gebruiker aan.
gebruiker = "cocktail"
url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={gebruiker}"
response_json = requests.get(url).json()

with open(r"endpoints (stap 1)\get_search_drink.json", "w") as fp:
    json.dump(response_json, fp)

