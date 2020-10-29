# GM-Project
Project of Graph Mining

The project consists in an analyse of the dataset concerning children in highschool and their relations.

## Data Explanation

# *Contact-diaries-network_data_2013.csv*

Format of the file : "i j w"

Meaning : *i* spent *x(w)* time with *j*

- **i** ID i of a person (int)
- **j** ID j of another person (int)
- **w** Duration of contact between i and j (int)
    - *w = 1* : at most 5 minutes
    - *w = 2* : between 5 and 15 minutes
    - *w = 3* : between 15 minutes and 1 hour
    - *w = 4* : more than 1 hour

# *Facebook-known-pairs_data_2013.csv*

Format of the file : "i j w"

Meaning : *i* is friend or not on Facebook with *j*

- **i** ID i of a person (int)
- **j** ID j of another person (int)
- **w** Status of Facebook friendship (bool)

# *Friendship-network_data_2013.csv*

Format of the file : "i j"

Meaning : *i* reported a friendship with *j*

- **i** ID i of a person (int)
- **j** ID j of another person (int)

# *High-School_data_2013*

Format of the file : "t i j Ci Cj"

Meaning : *i* from class *Ci* and *j* from class *Cj* where together at interval *[t - 20s, t]*

- **t** Contact between i and j at time [t - 20s, t] (int)
- **i** ID i of a person (int)
- **j** ID j of another person (int)
- **Ci** Class Ci of the person i (str)
- **Cj** Class Cj of the person j (str)

# *metadata_2013.txt*

Format of the file : "i Ci Gi"

Meaning : The person *i* is in the class *Ci* and has a gender *Gi*

- **i** ID of the person (int)
- **Ci** Class Ci of the person (str)
- **Gi** Gender Gi of the person (str)


*Source of the data : [Source](http://www.sociopatterns.org/datasets/high-school-contact-and-friendship-networks/)*
