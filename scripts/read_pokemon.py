
import sys
import json
import requests

# Pass no arguments for the full list
# Pass one argument for a single entry
# Pass two arguments for a slice of the list
# Pass three or more to select multiple

def read_pokemon( id_num ):

	url = "https://www.pokeapi.co/api/v2/pokemon-species/" + str(id_num) + "/"
	r = requests.get(url)
	pokeapi = json.loads( r.text )

	pokemon = {}

	pokemon['id'] = pokeapi['id']
	pokemon['name'] = pokeapi['name']
	pokemon['color'] = pokeapi['color']['name']
	pokemon['shape'] = pokeapi['shape']['name']

	if pokeapi['habitat'] != None:
		pokemon['habitat'] = pokeapi['habitat']['name']
	else:
		pokemon['habitat'] = None

	for entry in pokeapi['flavor_text_entries']:
		if entry['language']['name'] == 'en':
			pokemon['flavor_text'] = entry['flavor_text']
			break

	return pokemon

# >>>

POKEMON_TOTAL = 721	

print("[")

if len(sys.argv) == 1:
	for id_num in range( 1,POKEMON_TOTAL ):
		try:
			pokemon = read_pokemon( id_num ) 
			print( json.dumps(pokemon) )
			print(',')
		except: 
			pass
	pokemon = read_pokemon( POKEMON_TOTAL )
	print( json.dumps(pokemon) )		

elif len(sys.argv) == 2:
	id_num = int(sys.argv[1])
	if (0 < id_num <= POKEMON_TOTAL+1):
		pokemon = read_pokemon( id_num )
		print( json.dumps(pokemon) )

elif len(sys.argv) == 3:
	
	min_num = int(sys.argv[1])
	min_num = max(1, min_num)
	min_num = min(min_num, POKEMON_TOTAL)

	max_num = int(sys.argv[2])
	max_num = max(1, max_num)
	max_num = min(max_num, POKEMON_TOTAL)
	
	if min_num > max_num:
		min_num, max_num = max_num, min_num

	for id_num in range( min_num, max_num ):
		try:
			pokemon = read_pokemon( id_num ) 
			print( json.dumps(pokemon) )
			print(',')
		except: 
			pass
	pokemon = read_pokemon( max_num )
	print( json.dumps(pokemon) )

else:
	
	id_num = int(sys.argv[1])
	try:
		pokemon = read_pokemon( id_num ) 
		print( json.dumps(pokemon) )
	except: 
		pass

	for arg in sys.argv[2:]:
		id_num = int(arg)
		try:
			pokemon = read_pokemon( id_num ) 
			print(',')
			print( json.dumps(pokemon) )
		except: 
			pass

print(']')