import pandas as pd #supports for multi dimensional array # built on top of Numpy
import numpy as np


Row=int(input("Ënter the number of rows:"))
C = int(input("Enter the number of columns:"))
 
# Initialize matrix
data = []
print("Enter the entries rowwise:")
 
# For user input
for i in range(Row):          # A for loop for row entries
    a = input("Enter the Data Separated by commas : ").split(",")
    
    data.append(a)
 
print(data)


d = np.array(data)[:, :-1]
print("n The attributes are: ", d)


target = np.array(data)[:, -1]
print("n The target is: ", target)

def FindS(c, t):
    specific_hypothesis = []
    for i, val in enumerate(t):
        if val == "YES":
            specific_hypothesis = c[i].copy()
            print("sh is ", specific_hypothesis)
            break

    for i, val in enumerate(c):
        if t[i] == "YES":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass

    return specific_hypothesis
FindS(d,target)
