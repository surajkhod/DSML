# Write a program to cluster a set of points using K-means for IRIS
# dataset. Consider, K=4, clusters. Consider Euclidean distance as the
# distance measure. Randomly initialize a cluster mean as one of the data
# points. Iterate at least for 10 iterations. After iterations are over, print the
# final cluster means for each of the clusters.

import pandas as pd
import numpy as np

# Load the Iris dataset
iris_data = pd.read_csv('/home/surajkhod/Coding/DSML/datasets/IRIS.csv')

# Extract only the numeric features for clustering
features = iris_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

# Define the number of clusters and iterations
K = 4
iterations = 10

# Step 1: Randomly initialize cluster centroids
np.random.seed(42)  # For reproducibility
random_indices = np.random.choice(features.shape[0], K, replace=False)
centroids = features[random_indices]

# K-means clustering algorithm
for i in range(iterations):
    # Step 2: Assign each point to the nearest cluster centroid
    distances = np.array([[np.linalg.norm(point - centroid) for centroid in centroids] for point in features])
    labels = np.argmin(distances, axis=1)
    
    # Step 3: Recalculate cluster centroids
    new_centroids = np.array([features[labels == k].mean(axis=0) if np.any(labels == k) else centroids[k] for k in range(K)])
    
    # Check for convergence (optional)
    if np.allclose(centroids, new_centroids):
        print(f"Converged after {i+1} iterations.")
        break
    
    centroids = new_centroids

# Step 4: Print final cluster centroids
print("Final cluster means (centroids):")
for cluster_id, centroid in enumerate(centroids):
    print(f"Cluster {cluster_id + 1}: {centroid}")
