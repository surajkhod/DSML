"""
Write a program to do the following: You have given a collection of 8
points. P1=[2, 10] P2=[2, 5] P3=[8, 4] P4=[5, 8] P5=[7,5] P6=[6, 4] P7=[1, 2]
P8=[4, 9]. Perform the k-mean clustering with initial centroids as m1=P1
=Cluster#1=C1 and m2=P4=cluster#2=C2, m3=P7 =Cluster#3=C3. Answer
the following 1] Which cluster does P6 belong to? 2] What is the
population of a cluster around m3? 3] What is the updated value of m1,
m2, m3?
"""

import math
import numpy as np

# Input data points
data = [
    [2, 10, "P1"], # P1
    [2, 5, "P2"],  # P2
    [8, 4, "P3"],  # P3
    [5, 8, "P4"],  # P4
    [7, 5, "P5"],  # P5
    [6, 4, "P6"],  # P6
    [1, 2, "P7"],  # P7
    [4, 9, "P8"]   # P8
]

# Initial centroids
k = 3
centroid = [
    data[0][:2], # m1 = P1 = Cluster#1
    data[3][:2], # m2 = P4 = Cluster#2
    data[6][:2]  # m3 = P7 = Cluster#3
]

cluster1, cluster2, cluster3 = [], [], []

while True:
    currc1, currc2, currc3 = [], [], []

    # Assign each point to the nearest centroid
    for p in data:
        distances = [
            math.sqrt((p[0] - centroid[0][0])**2 + (p[1] - centroid[0][1])**2), # Distance to m1
            math.sqrt((p[0] - centroid[1][0])**2 + (p[1] - centroid[1][1])**2), # Distance to m2
            math.sqrt((p[0] - centroid[2][0])**2 + (p[1] - centroid[2][1])**2)  # Distance to m3
        ]
        min_distance_index = distances.index(min(distances))
        if min_distance_index == 0:
            currc1.append(p)
        elif min_distance_index == 1:
            currc2.append(p)
        else:
            currc3.append(p)

    # Check for convergence
    if currc1 == cluster1 and currc2 == cluster2 and currc3 == cluster3:
        break

    cluster1, cluster2, cluster3 = currc1, currc2, currc3

    # Update centroids
    centroid = [
        np.mean([point[:2] for point in cluster1], axis=0) if cluster1 else centroid[0],
        np.mean([point[:2] for point in cluster2], axis=0) if cluster2 else centroid[1],
        np.mean([point[:2] for point in cluster3], axis=0) if cluster3 else centroid[2]
    ]

# Output results
print("Final elements in Cluster#1 (C1):", cluster1)
print("Final elements in Cluster#2 (C2):", cluster2)
print("Final elements in Cluster#3 (C3):", cluster3)
print("\nUpdated Centroids:")
print("m1 (C1):", centroid[0])
print("m2 (C2):", centroid[1])
print("m3 (C3):", centroid[2])

# Answers
p6_cluster = None
for cluster, label in zip([cluster1, cluster2, cluster3], ["C1", "C2", "C3"]):
    if any(p[2] == "P6" for p in cluster):
        p6_cluster = label
        break

print(f"\n1] P6 belongs to: {p6_cluster}")
print(f"2] Population of cluster around m3 (C3): {len(cluster3)}")
