import requests, json
from PIL import Image

im = Image.open(requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png", stream=True).raw)
im.show()