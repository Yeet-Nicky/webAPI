import api_functions as api

while True :
    print("\n_______________________________________________________________")
    print("welkom bij het keuzemenu")
    print("____________________________________________________________")
    print("1. geef een drankje in en krijg het recept.")
    print("2. krijg een random drankje en het recept er van. ")
    keuze = input("\nMaak een keuze: ")
    print("_______________________________________________________________")

    ## LAAT GEBRUIKER DRANKJE OPZOEKEN ##
    if keuze == "1":
        ## GET drankje op basis van input gebruiker. ##
        search = input("Van welk soort drankje wilt u het recept weten: ")
        drankje = api.get_first_search_drink(search)

        if drankje == False:
            print(f"Drankje {search} bestaat niet in mijn DB...")
            continue
        print(f"Volgend drankje gevonden: {drankje["strDrink"]}")

        ## Vraag of gebruiker het recept voor dit drankje wilt weten. ##
        antwoord = input("\nWilt u het recept van dit drankje zien (y/n)? ")
        if antwoord != "y":
            continue
        print(drankje["strInstructions"])

        ## Vraag of gebruiker ingredienten voor dit drankje wilt weten. ##
        antwoord = input("\nWilt u ook de ingredienten van dit drankje weten (y/n)? ")
        if antwoord != "y":
            continue

        print(f"De ingredienten zijn...")
        for i in range(1,16):
            ingredient, hoeveelheid = drankje[f"strIngredient{i}"], drankje[f"strMeasure{i}"]
            if ingredient == None:
                break
            
            print(f"    - {ingredient}: {hoeveelheid}")

    ## HAAL RANDOM DRANKJE OP  ##
    elif keuze == "2":
        print("We halen een random drankje voor u op...")
        drankje = api.get_random_drink()
        print(f"Volgend drankje gevonden: {drankje["strDrink"]}")

        ## Vraag of gebruiker het recept voor dit drankje wilt weten. ##
        antwoord = input("\nWilt u het recept van dit drankje zien (y/n)? ")
        if antwoord != "y":
            continue
        print(drankje["strInstructions"])

        ## Vraag of gebruiker ingredienten voor dit drankje wilt weten. ##
        antwoord = input("\nWilt u ook de ingredienten van dit drankje weten (y/n)? ")
        if antwoord != "y":
            continue

        print(f"De ingredienten zijn...")
        for i in range(1,16):
            ingredient, hoeveelheid = drankje[f"strIngredient{i}"], drankje[f"strMeasure{i}"]
            if ingredient == None:
                break
            
            print(f"    - {ingredient}: {hoeveelheid}")

    else:
        print("Ongeldige input. Probeer opnieuw...")
        print("_______________________________________________________________")
