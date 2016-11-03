
import sys
import json
import requests


# Pass in the id to look up the pokemon

if len(sys.argv) < 2:
    num = 1
else:
    num = sys.argv[1]

url = "https://www.pokeapi.co/api/v2/pokemon-species/" + str(num) + "/"
r = requests.get(url)
msg = str(r.content)[2:-1]


"""
# Test saved json file
file = open("test_pokemon.json")
pokeapi = json.load(file)
"""

keys = ['id', 'name', 'habitat', 'color', 'shape']
named_keys = ['habitat', 'color', 'shape']

pokeapi = json.loads(msg)
pokemon = {}
for key in keys:
    pokemon[key] = pokeapi[key]
for key in named_keys:
    pokemon[key] = pokemon[key]['name']
for entry in pokeapi['flavor_text_entries']:
    if entry['language']['name'] == 'en':
        pokemon['flavor_text'] = entry['flavor_text']
        break

print(json.dumps(pokemon))
