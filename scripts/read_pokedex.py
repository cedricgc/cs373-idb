
import sys
import json
import requests

# Pass no arguments for the full list
# Pass one argument for a single entry
# Pass two arguments for a slice of the list
# Pass three or more to select multiple

def read_pokedex( id_num ):

	url = "https://www.pokeapi.co/api/v2/pokedex/" + str(id_num) + "/"
	r = requests.get(url)
	pokeapi = json.loads( r.text )

	pokedex = {}

	pokedex['id'] = pokeapi['id']
	pokedex['name'] = pokeapi['name']

	if pokeapi['region'] != None:
		pokedex['region'] = pokeapi['region']['name']
	else:
		pokedex['region'] = None

	for entry in pokeapi['descriptions']:
		if entry['language']['name'] == 'en':
			pokedex['description'] = entry['description']
			break

	for entry in pokeapi['names']:
		if entry['language']['name'] == 'en':
			pokedex['official_name'] = entry['name']
			break

	return pokedex

# >>>

POKEDEX_TOTAL = 15

print("[")

if len(sys.argv) == 1:
	for id_num in range( 1,POKEDEX_TOTAL ):
		try:
			pokedex = read_pokedex( id_num ) 
			print( json.dumps(pokedex) )
			print(',')
		except: 
			pass
	pokedex = read_pokedex( POKEDEX_TOTAL )
	print( json.dumps(pokedex) )		

elif len(sys.argv) == 2:
	id_num = int(sys.argv[1])
	if (0 < id_num <= POKEDEX_TOTAL+1):
		pokedex = read_pokedex( id_num )
		print( json.dumps(pokedex) )

elif len(sys.argv) == 3:
	
	min_num = int(sys.argv[1])
	min_num = max(1, min_num)
	min_num = min(min_num, POKEDEX_TOTAL)

	max_num = int(sys.argv[2])
	max_num = max(1, max_num)
	max_num = min(max_num, POKEDEX_TOTAL)
	
	if min_num > max_num:
		min_num, max_num = max_num, min_num

	for id_num in range( min_num, max_num ):
		try:
			pokedex = read_pokedex( id_num ) 
			print( json.dumps(pokedex) )
			print(',')
		except: 
			pass
	pokedex = read_pokedex( max_num )
	print( json.dumps(pokedex) )

else:
	
	id_num = int(sys.argv[1])
	try:
		pokedex = read_pokedex( id_num ) 
		print( json.dumps(pokedex) )
	except: 
		pass

	for arg in sys.argv[2:]:
		id_num = int(arg)
		try:
			pokedex = read_pokedex( id_num ) 
			print(',')
			print( json.dumps(pokedex) )
		except: 
			pass

print(']')