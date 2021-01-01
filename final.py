import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx 
import colorsys

#
# Loading data
#

contact = pd.read_csv('data/Contact-diaries-network_data_2013.csv', sep=' ', names=['i', 'j', 'w'])
print(contact.head())

# Inversing the weight : people spending more time together are closer
contact['w_'] = 1 / contact['w']
print(contact.head())

infos = pd.read_table('data/metadata_2013.txt', names=['i', 'class', 'gender'])
print(infos.head())

G = nx.from_pandas_edgelist(contact, source='i', target='j', edge_attr='w_', create_using=nx.DiGraph())

print(nx.info(G))
plt.hist(dict(G.degree()).values())
plt.show()

classes = infos['class'].unique()
genders = infos['gender'].unique()

print(classes)
print(genders)

N = len(classes)
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

styles = ['dotted', 'dashdot', 'dashed', 'solid']

for e in G.edges(data=True):
    width = e[2]['w_']
    style = styles[int((1 / width) - 1)]
    pos = nx.spring_layout(G)
    nx.draw_networkx_edges(G, pos, edgelist=[e], width=width, style=style)

for node in G.nodes():
    imsize = (G.in_degree(node, weight='w_') / max(dict(G.in_degree(weight='w_')).values()))
    nx.draw_networkx_nodes(G, pos)

#pos = nx.layout.fruchterman_reingold_layout(G, k=1, wiehgt='w_', iterations=1000, scale=2)
nx.draw_networkx(G)
#plt.show()