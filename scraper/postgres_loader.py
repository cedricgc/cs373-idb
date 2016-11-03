import psycopg2

try:
    connect_str = "dbname='OUR_DB' user='OUR_USER' host='localhost' " + \
                  "password='OUR_PW'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Pokemon, Pokedex, Move;")
    cursor.execute("CREATE TABLE Pokemon(id INTEGER PRIMARY KEY, name VARCHAR(20), color VARCHAR(20), shape VARCHAR(20), habitat VARCHAR(20), flavor_text VARCHAR(20));")
    cursor.execute("CREATE TABLE Pokedex(id INTEGER PRIMARY KEY, name VARCHAR(20), region VARCHAR(20), official_name VARCHAR(20), description VARCHAR(20));")
    cursor.execute("CREATE TABLE Move(id INTEGER PRIMARY KEY, name VARCHAR(20), power INTEGER, accuracy INTEGER, power_points INTEGER, short_effect VARCHAR(20), damage_class VARCHAR(20), flavor_text VARCHAR(20));")

    with open('pokemon-species.json') as infile:
        pokemon = json.load(infile)
        for p in pokemon:
            cur.execute("INSERT INTO Pokemon(id, name, color, shape, habitat, flavor_text) VALUES ({}, {}, {}, {}, {}, {})".format(
                p['id'], p['name'], p['color'], p['shape'], p['habitat'], p['flavor_text_entries'][1]))

    with open('pokedex.json') as infile:
        pokedex = json.load(infile)
        for p in pokedex:
            cur.execute("INSERT INTO Pokedex(id, name, region, official_name, description) VALUES ({}, {}, {}, {}, {})".format(
                p['id'], p['name'], p['region']['name'], p['names'][2], p['official_name'], p['descriptions'][2]))

    with open('move.json') as infile:
        moves = json.load(infile)
        for m in move:
            cur.execute("INSERT INTO move(id, name, power, accuracy, power_points, short_effect, damage_class) VALUES ({}, {}, {}, {}, {}, {}, {})".format(
                m['id'], m['name'], m['power'], m['accuracy'], m['pp'], m['effect_entries']['short_effect'], m['damage_class']['name']))

    conn.commit()
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
