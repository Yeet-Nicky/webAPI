# DIT IS STAP 2 VAN HET STAPPENPLAN

import requests

""" OPGELET!
Je kan aan dit bestand ook functies toevoegen die de response van een API verder verwerken.
Bijvoorbeeld een functie die voor een drankje alle ingredienten print.
Door dit te doen hoe je de code in het app-bestand kort en leesbaar!
"""

def get_first_search_drink(search:str) -> dict:
    " Geef het eerste drankje gevonden op basis van de 'search' "
    url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search}"
    response_json = requests.get(url).json()

    if response_json == {"drinks": None}:
        return False
    return response_json["drinks"][0]

def get_random_drink() -> dict:
    " Geef een random drankje "
    url= f"https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response_json = requests.get(url).json()
    return response_json["drinks"][0]