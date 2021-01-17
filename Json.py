from Grafo import Grafo
import json

def Write(graph):
    nodes = graph.GetVertices()
    edges = graph.GetAristas()
    data = {}
    data['vertices'] = []
    data['edges'] = []
    i = 1
    for v in nodes:
        data['vertices'].append({
            'name': nodes[i].GetName(),
            'v': str(nodes[i].GetV()),
            't':str(nodes[i].GetT()),
            'a':str(nodes[i].GetA()),
            'posx':str(nodes[i].GetPos()[0]),
            'posy':str(nodes[i].GetPos()[1])
        })
        i += 1
    for e in edges:
        data['edges'].append({
            'inicio':e[0],
            'fin':e[1],
            'valor':e[2]
        })

    with open('graph.json','w') as file:
        json.dump(data,file)

def Read():
    with open('graph.json') as json_file:
        graph = json.load(json_file)
        new_graph = Grafo()
        for v in graph['vertices']:
            if v['t'] == "True":
                new_graph.AgregarVertice(v['name'],int(v['v']),int(v['a']),True,[int(v['posx']),int(v['posy'])])
            else:
                new_graph.AgregarVertice(v['name'], int(v['v']), int(v['a']), False, [int(v['posx']),int(v['posy'])])

        for a in graph['edges']:
            new_graph.AgregarArista(a['inicio'],a['fin'],a['valor'])
        return new_graph

"""
def WriteEx():
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


def ReadEx():
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            print("Name: " + p['name'])
            print("Age: " + p['age'])
            print("From: " + p['from'])
            print('')
"""