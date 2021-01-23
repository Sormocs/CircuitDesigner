from Grafo import Grafo
import json

def Write(graph, nodes, s_edges,r_names,r_values,p_names,p_values,name):
    vertexes = graph.GetVertices()
    edges = graph.GetAristas()
    data = {}
    data['vertices'] = []
    data['edges'] = []
    data['nodes'] = []
    data['s_edges'] = []
    data['r_names'] = []
    data['r_values'] = []
    data['p_names'] = []
    data['p_values'] = []
    data['c_type'] = []

    i = 1
    for v in vertexes:
        data['vertices'].append({
            'name': vertexes[i].GetName(),
            'v': str(vertexes[i].GetV()),
            't':str(vertexes[i].GetT()),
            'a':str(vertexes[i].GetA()),
            'posx':str(vertexes[i].GetPos()[0]),
            'posy':str(vertexes[i].GetPos()[1])
        })
        i += 1
    for e in edges:
        data['edges'].append({
            'inicio':e[0],
            'fin':e[1],
            'valor':e[2]
        })
    if nodes != []:
        for n in nodes:
            data['nodes'].append({
                'posx':n[0],
                'posy':n[1]
            })

    if s_edges != []:
        for e in s_edges:
            data['s_edges'].append({
                'start':e[0],
                'end':e[1]
            })

    if r_names != []:
        for rn in r_names:
            data['r_names'].append({
                'r_name':rn
            })

            data['c_type'].append({
                'node': 'res'
            })

    if r_values != []:
        for rv in r_values:
            data['r_values'].append({
                'r_value':rv
            })

    if p_names != []:
        for pn in r_names:
            data['p_names'].append({
                'p_name': pn
            })

            data['c_type'].append({
                'node':'power'
            })

    if p_values != []:
        for pv in r_values:
            data['p_values'].append({
                'p_value': pv
            })

    # #node2, power_supply1, b_resistor, y_power_supply, node3, node4,node5, power_supply2, b_resistorV, y_power_supplyH
    # for c in c_type:
    #     data['c_type'].append({

    #    })
    with open(name+'.json','w') as file:
        json.dump(data,file)

def Read(name):
    with open(name+'.json') as json_file:
        graph = json.load(json_file)
        new_graph = Grafo()
        nodes = []
        s_edges = []
        r_names = []
        r_values = []
        p_names = []
        p_values = []
        c_type = []
        for v in graph['vertices']:
            if v['t'] == "True":
                new_graph.AgregarVertice(v['name'],int(v['v']),int(v['a']),True,[int(v['posx']),int(v['posy'])])
            else:
                new_graph.AgregarVertice(v['name'], int(v['v']), int(v['a']), False, [int(v['posx']),int(v['posy'])])

        for a in graph['edges']:
            new_graph.AgregarArista(a['inicio'],a['fin'],a['valor'])

        for n in graph['nodes']:
            nodes.append((n['posx'],n['posy']))

        for e in graph['s_edges']:
            s_edges.append((e['start'],e['end']))

        for n in graph['r_names']:
            r_names.append(n['r_name'])

        for v in graph['r_values']:
            r_values.append(v['r_value'])

        for pn in graph['p_names']:
            p_names.append(pn['p_name'])

        for pv in graph['p_values']:
            p_values.append(pv['p_value'])

        for c in graph['c_type']:
            c_type.append(c['node'])

        comps = [new_graph,nodes,s_edges,r_names,r_values,p_names,p_values,c_type]
        return comps

