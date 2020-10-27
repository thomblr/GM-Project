import csv

with open('data/Friendship-network_data_2013.csv', 'r') as f:
    reader = csv.reader(f, delimiter=' ')

    for line in reader:
        print(line)