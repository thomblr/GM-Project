import csv
import networkx as nx
import matplotlib.pyplot as plt

#
#  METADATA 2013 (ID, Class, Gender)
#

with open('data/metadata_2013.txt', 'r') as meta: #
    data_2013 = meta.read()                       # Load the file
    data_2013 = data_2013.split('\n')             #

    # Add the data to a dictionary
    complete_data = {}
    for line in data_2013[:-1]:
        info = line.split('\t')
        complete_data[int(info[0])] = {'class': info[1], 'gender': info[2]}

    # Graph of gender
    gender_labels = ['F', 'M', 'Unknown']
    genders = [0,0,0]
    for i in complete_data:
        genders[gender_labels.index(complete_data[i]['gender'])] += 1

    # plt.pie(genders, explode=(0.1, 0.1, 0.1), labels=gender_labels, autopct='%1.1f%%')

    # Graph of classes
    class_labels = []
    for i in complete_data:
        if complete_data[i]['class'] not in class_labels:
            class_labels.append(complete_data[i]['class'])

    classes = [0] * len(class_labels)
    for i in complete_data:
        classes[class_labels.index(complete_data[i]['class'])] += 1

    # plt.pie(classes, labels=class_labels, autopct='%1.1f%%')

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
        G.add_edge(int(line[0]), int(line[1]), weight=int(line[2]))

    # nx.draw(G, with_labels=True)

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

    #nx.draw(G, with_labels=True)
    

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

plt.show()