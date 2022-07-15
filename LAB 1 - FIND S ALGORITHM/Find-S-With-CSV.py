import pandas as pd #supports for multi dimensional array # built on top of Numpy
import numpy as np

# to read the data in the csv file
data = pd.read_csv("data.csv")
print(data)

# making an array of all the attributes
d = np.array(data)[:, :-1]
print("\n The attributes are: ", d)

# segragating the target that has positive and negative examples
target = np.array(data)[:, -1]
print("\n The target is: ", target)


# training function to implement find-s algorithm
def train(c, t):
    specific_hypothesis= []
    for i, val in enumerate(t):
        if val == "YES":
            specific_hypothesis = c[i].copy()
            print("\n initial Hypothesis is ", specific_hypothesis)
            break

    for i, val in enumerate(c):
        if t[i] == "YES":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass

    return specific_hypothesis


# obtaining the final hypothesis
print("\n The final hypothesis is:", train(d, target))
