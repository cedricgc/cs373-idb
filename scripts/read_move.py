
import sys
import json
import requests

# Pass no arguments for the full list
# Pass one argument for a single entry
# Pass two arguments for a slice of the list
# Pass three or more to select multiple

def read_move( id_num ):

	url = "https://www.pokeapi.co/api/v2/move/" + str(id_num) + "/"
	r = requests.get(url)
	pokeapi = json.loads( r.text )

	move = {}

	move['id'] = pokeapi['id']
	move['name'] = pokeapi['name']
	move['power'] = pokeapi["power"]
	move['accuracy'] = pokeapi["accuracy"]
	move['power_points'] = pokeapi['pp']
	move['damage_class'] = pokeapi['damage_class']['name']

	for entry in pokeapi['effect_entries']:
		if entry['language']['name'] == 'en':
			move['short_effect'] = entry['short_effect']
			break

	for entry in pokeapi['flavor_text_entries']:
		if entry['language']['name'] == 'en':
			move['flavor_text'] = entry['flavor_text']
			break

	return move

# >>>

MOVE_TOTAL = 401

print("[")

if len(sys.argv) == 1:
	for id_num in range( 1,MOVE_TOTAL ):
		try:
			move = read_move( id_num ) 
			print( json.dumps(move) )
			print(',')
		except: 
			pass
	move = read_move( MOVE_TOTAL )
	print( json.dumps(move) )		

elif len(sys.argv) == 2:
	id_num = int(sys.argv[1])
	if (0 < id_num <= MOVE_TOTAL+1):
		move = read_move( id_num )
		print( json.dumps(move) )

elif len(sys.argv) == 3:
	
	min_num = int(sys.argv[1])
	min_num = max(1, min_num)
	min_num = min(min_num, MOVE_TOTAL)

	max_num = int(sys.argv[2])
	max_num = max(1, max_num)
	max_num = min(max_num, MOVE_TOTAL)
	
	if min_num > max_num:
		min_num, max_num = max_num, min_num

	for id_num in range( min_num, max_num ):
		try:
			move = read_move( id_num ) 
			print( json.dumps(move) )
			print(',')
		except: 
			pass
	move = read_move( max_num )
	print( json.dumps(move) )

else:
	
	id_num = int(sys.argv[1])
	try:
		move = read_move( id_num ) 
		print( json.dumps(move) )
	except: 
		pass

	for arg in sys.argv[2:]:
		id_num = int(arg)
		try:
			move = read_move( id_num ) 
			print(',')
			print( json.dumps(move) )
		except: 
			pass

print(']')