import numpy as np
from sklearn.cluster import DBSCAN

def find_discontinuous_clusters(points, eps, min_samples):
    """Use DBSCAN to find discontinuous clusters in spatial data."""
    clusters = DBSCAN(eps=eps, min_samples=min_samples).fit_predict(points)
    return clusters

# Generate some discontinuous spatial data
data = np.random.rand(1000, 2)
data = np.concatenate([data, 10 * np.random.rand(100, 2)])

# Find discontinuous clusters
clusters = find_discontinuous_clusters(data, eps=0.1, min_samples=10)
