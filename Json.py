import json

"""
def Write():
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Sergio',
        'age': '18',
        'from': 'San Jose'
    })

    data['people'].append({
        'name': 'David',
        'age': '18',
        'from': 'Cartago'
    })

    data['people'].append({
        'name': 'Paola',
        'age': '18',
        'from': 'Unknown'
    })

    with open('data.json','w') as outfile:
        json.dump(data,outfile)


def Read():
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            print("Name: " + p['name'])
            print("Age: " + p['age'])
            print("From: " + p['from'])
            print('')
            
"""

def Write(graph, nodes, powers, edges):
    data = {}
    for node in graph:
        data['graph'].append({

        })