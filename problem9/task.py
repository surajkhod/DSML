"""
Write a program to do the following: You have given a collection of 8
points. P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16, 0.85]
P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]. Perform the k-mean
clustering with initial centroids as m1=P1 =Cluster#1=C1 and
m2=P8=cluster#2=C2. Answer the following 1] Which cluster does P6
belong to? 2] What is the population of a cluster around m2? 3] What is
the updated value of m1 and m2?
"""
import math
import numpy as np

data = [
    [0.1, 0.6, "P1"],   # P1
    [0.15, 0.71, "P2"], # P2
    [0.08, 0.9, "P3"],  # P3
    [0.16, 0.85, "P4"], # P4
    [0.2, 0.3, "P5"],   # P5
    [0.25, 0.5, "P6"],  # P6
    [0.24, 0.1, "P7"],  # P7
    [0.3, 0.2, "P8"]    # P8
]

k = 2
cluster1 = []
cluster2 = []

centroid = [
    data[0][:2],
    data[7][:2]
]

while(True):
    currc1 = []
    currc2 = []

    for p in data:
        p1 = math.sqrt((p[0] - centroid[0][0])**2 + (p[1] - centroid[0][1])**2)
        p2 = math.sqrt((p[0] - centroid[1][0])**2 + (p[1] - centroid[1][1])**2)

        if p1 < p2:
            currc1.append(p)
        else:
            currc2.append(p)

    if currc1 == cluster1 and currc2 == cluster2:
        break
    cluster1 = currc1
    cluster2 = currc2


    p1mean = np.mean([point[:2] for point in currc1], axis=0)
    p2mean = np.mean([point[:2] for point in currc2], axis=0)

    centroid = [
        p1mean,
        p2mean
    ]

print("Final elements in cluster 1: ", cluster1)
print()
print("Final elements in cluster 2: ", cluster2)
print()
print("Updated Centroid: ")
print(centroid[0], centroid[1])
