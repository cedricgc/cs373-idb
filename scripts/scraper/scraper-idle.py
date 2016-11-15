import urllib.parse
import urllib.request
import json
import os

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
base_url = 'http://pokeapi.co/api/v2/'

resources = ['pokemon', 'pokemon-species', 'pokedex', 'move']
for resource in resources:
    url = base_url + resource + '/'
    req = urllib.request.Request(url, headers=headers)
    limit = None

    with urllib.request.urlopen(req) as response:
        response_data = json.loads(response.read().decode('utf-8'))
        limit = response_data['count']

    url = url + '?limit=' + str(limit)
    req = urllib.request.Request(url, headers=headers)
    agg_results = list()
    resource_file = resource + '.json'

    try:
        if os.path.isfile(resource_file):
            with open(resource_file) as infile:
                agg_results = json.load(infile)

        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode('utf-8'))
            results = response_data['results']

            for i in range(len(agg_results), len(results)):
                result = results[i]
                result_url = result['url']
                print(result_url)
                result_req = urllib.request.Request(result_url, headers=headers)

                with urllib.request.urlopen(result_req) as result_response:
                    agg_results.append(json.loads(
                        result_response.read().decode('utf-8')))

    finally:
        with open(resource_file, 'w') as outfile:
            json.dump(agg_results, outfile, indent=4)
