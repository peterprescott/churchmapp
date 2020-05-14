# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,rmd//Rmd,scripts//py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx

churches = ['mossleyhill','sthelens','gateway','stoneycroftsalvationarmy']

location = {'mossleyhill' : 'L18 8DB',
            'sthelens' : 'WA10 2DT',
            'gateway' : 'L24 9HJ',
            'stoneycroftsalvationarmy': 'L13 3BT'}

mile = 1609 # metres

pcdlatlng = pd.read_csv('../data/csv/pcdlatlng.csv')


def get_coords(postcode):
    "Lookup coordinates from conversion table."
    row = pcdlatlng.loc[pcdlatlng.postcode==postcode].iloc[0]
    return row.latitude, row.longitude


def get_street_names(coords, miles):
    neighbourhood_graph = ox.project_graph(ox.graph_from_point(coords, distance=miles*mile, network_type='drive'))
    ints = ox.clean_intersections(neighbourhood_graph)

    gdf = gpd.GeoDataFrame(ints, columns=['geometry'], crs=neighbourhood_graph.graph['crs'])
    X = gdf['geometry'].map(lambda pt: pt.coords[0][0])
    Y = gdf['geometry'].map(lambda pt: pt.coords[0][1])

    nodes = ox.get_nearest_nodes(neighbourhood_graph, X, Y, method='kdtree')
    nearby_streets = {'Rose Lane'}
    for n in nodes:
        for nbr in nx.neighbors(neighbourhood_graph, n):
            for d in neighbourhood_graph.get_edge_data(n, nbr).values():
                if 'name' in d:
                    if type(d['name']) == str:
                        nearby_streets.add(d['name'])
                    elif type(d['name']) == list:
                        for name in d['name']:
                            nearby_streets.add(name)
                    else:
                        pass
                else:
                    pass

    return nearby_streets


streets = {}
for church in churches:
    streets[church] = get_street_names(get_coords(location[church]), 1)

for church in churches:
    print(church)
    print(f'{len(streets[church])} streets within 1 mile')
    print(streets[church])
    print('\n')
