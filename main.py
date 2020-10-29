import csv
import networkx as nx
import matplotlib.pyplot as plt

with open('data/Friendship-network_data_2013.csv', 'r') as f:
    reader = csv.reader(f, delimiter=' ')

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

    plt.subplot(121)
    plt.pie(genders, explode=(0.1, 0.1, 0.1), labels=gender_labels, autopct='%1.1f%%')

    # Graph of classes
    class_labels = []
    for i in complete_data:
        if complete_data[i]['class'] not in class_labels:
            class_labels.append(complete_data[i]['class'])

    classes = [0] * len(class_labels)
    for i in complete_data:
        classes[class_labels.index(complete_data[i]['class'])] += 1

    plt.subplot(122)
    plt.pie(classes, labels=class_labels, autopct='%1.1f%%')
    plt.show()