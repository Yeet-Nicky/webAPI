import requests, json
from PIL import Image

while True:
    # informatie zoeken over een pokemon 
    print("----------------------------------------------")
    vraag_gebruiker = input(f"welke pokemon zou je willen opzoeken: ")
    print("-----------------------------------------------")
    # een link over de gevraagde pokemon 
    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{vraag_gebruiker}"
    response_json = requests.get(url_pokemon).json()
    with open("json_files/pokemon.json", "w") as fp:
        json.dump(response_json, fp)
    #de gebruiker vragen waar over hij informatie wilt hebben 
    print(f"wat wil je van {vraag_gebruiker} te weten komen")
    print("--------------------------------------")
    print(f"1) de typing van {vraag_gebruiker}")
    print(f"2) de foto van {vraag_gebruiker}")
    print("--------------------------------------")
    keuze = input("welke keuze kies je: ")
    # dit is keuze 1 
    if keuze == "1":
        types = response_json["types"]
        print("Deze pokemon heeft als types: ")
        for index, type in enumerate(types):
            print(f"- {type['type']['name']}")
        meer_informatie = input(f"over welke type wil je meer informatie hebben : ")

        # link van de gevraagde type
        url_type = f"https://pokeapi.co/api/v2/type/{meer_informatie}/"
        types = requests.get(url_type).json()

        with open("json_files/pokemon_type.json", "w") as fp:
            json.dump(types, fp)

        # je kiest als je de zwaktes of de sterktes krijgt
        print("--------------------------------")
        zwakes_stektes = input("wil je meer informatie over de (sterktes/ zwaktes): ")
        print("---------------------------------")
        # dit is de code om de sterktes te krijgen
        if zwakes_stektes == "sterktes":
            sterktes_to = types["damage_relations"]["double_damage_to"]
            sterktes_from = types["damage_relations"]["half_damage_from"]
            no_damage_from = types["damage_relations"]["no_damage_from"]
            print("double_damage_to")
            for sterkte_to in sterktes_to:
                print(f"-{sterkte_to['name']}")
            print("half_damage_from")
            for damage_from in sterktes_from:
                print(f"-{damage_from['name']}")
            print("no_damahe_from")
            for no_damage_f in no_damage_from:
                print(f"-{no_damage_f['name']}")
        # dit is de code om de zwaktes de krijgen
        elif zwakes_stektes == "zwaktes":
            zwaktes_to = types["damage_relations"]["double_damage_from"]
            zwaktes_from = types["damage_relations"]["half_damage_to"]
            no_damage_to = types["damage_relations"]["no_damage_to"]
            print("double_damage_from")
            for zwakte_to in zwaktes_to:
                print(f"-{zwakte_to['name']}")
            print("half_damage_to")
            for damage_to in zwaktes_from:
                print(f"-{damage_to['name']}")
            print("no_damahe_to")
            for no_damage_t in no_damage_to:
                print(f"-{no_damage_t['name']}")
    # keuze 2
    if keuze == '2' :
        # de foto van de pokemon 
        foto = response_json['sprites']['front_default']
        pokemon_im = Image.open(requests.get(foto, stream=True).raw)
        pokemon_im.show() 

        shiny_of_nie = input('wil je de shiny variant zien (y/n): ')
        if shiny_of_nie == 'y':
            # een foto van de gevraagde pokemon in de shiny form
            foto_shiny = response_json['sprites']['front_shiny']
            pokemon_shiny_im = Image.open(requests.get(foto_shiny, stream=True).raw)
            pokemon_shiny_im.show()
        if shiny_of_nie == 'n':
            continue
        # vraag de gebruiker om veder te gaan 
        vraag_gebruiker_om_te_stoppen = input('wil je veder gaan (y/n): ')
        if vraag_gebruiker_om_te_stoppen == 'y':
            continue
        elif vraag_gebruiker_om_te_stoppen == 'n':
            break