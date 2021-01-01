import csv
import networkx as nx
import community as cl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from networkx.algorithms import approximation

#
#  METADATA 2013 (ID, Class, Gender)
#

meta_complete = {}
meta_gender_based = {}
meta_class_based = {}

with open('data/metadata_2013.txt', 'r') as meta: #
    data_2013 = meta.read()                       # Load the file
    data_2013 = data_2013.split('\n')             #

    # Add the data to a dictionary
    complete_data = {}
    for line in data_2013[:-1]:
        info = line.split('\t')
        complete_data[int(info[0])] = {'class': info[1], 'gender': info[2]}
        meta_complete[int(info[0])] = {'class': info[1], 'gender': info[2]}

    # Graph of gender
    meta_gender_based = {'F': [], 'M': [], 'Unknown': []}
    for i in complete_data:
        meta_gender_based[complete_data[i]['gender']].append(i)

    # Graph of classes
    meta_class_based = {}
    for i in complete_data:
        if complete_data[i]['class'] not in meta_class_based:
            meta_class_based[complete_data[i]['class']] = []
        meta_class_based[complete_data[i]['class']].append(i)

print(meta_complete)
print('---')
print(meta_gender_based)
print('---')
print(meta_class_based)

#
# Contact Diaries Network Data 2013 (ID, ID, contact_duration(w))
#

with open('data/Contact-diaries-network_data_2013.csv', 'r') as f:
    contact = csv.reader(f, delimiter=' ')
    
    G = nx.DiGraph()
    actors = []
    for line in contact:
        if int(line[0]) not in actors:
            actors.append(int(line[0]))
            G.add_node(int(line[0]))
        G.add_edge(int(line[0]), int(line[1]), weight=(1/int(line[2])))

    #nx.draw(G, with_labels=True)

#
# Facebook known pairs (ID, ID, bool)
#

with open('data/Facebook-known-pairs_data_2013.csv', 'r') as f:
    contact = csv.reader(f, delimiter=' ')
    
    G = nx.Graph()
    actors = []
    for line in contact:
        if int(line[0]) not in actors:
            actors.append(int(line[0]))
            G.add_node(int(line[0]))
        if(int(line[2]) == 1):
            G.add_edge(int(line[0]), int(line[1]), weight=int(line[2]))

    partition = cl.best_partition(G)
    pos = nx.spring_layout(G)
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40, cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    #plt.show()
    

#
# Friendship network data 2013 (ID, ID)
#

with open('data/Friendship-network_data_2013.csv', 'r') as f:
    network = csv.reader(f, delimiter=' ')

    G = nx.DiGraph()
    actors = []
    for line in network:
        if int(line[0]) not in actors:
            actors.append(int(line[0]))
            G.add_node(int(line[0]))
        G.add_edge(int(line[0]), int(line[1]))

    #nx.draw(G, with_labels=True)


#
# High School data 2013 (t, ID, ID, Class, Class)
#

with open('data/High-School_data_2013.csv', 'r') as f:
    network = csv.reader(f, delimiter=' ')

    G = nx.Graph()
    classes = {}
    actors = []

    for line in network:
        if line[3] not in classes:
            classes[line[3]] = "color"
        if line[4] not in classes: 
            classes[line[4]] = "color"
        if int(line[1]) not in actors:
            actors.append(int(line[1]))
            G.add_node(int(line[1]))
        if int(line[2]) not in actors: 
            actors.append(int(line[2]))
            G.add_node(int(line[2]))
        G.add_edge(int(line[1]), int(line[2]))

    # nx.draw(G, with_labels=True)
