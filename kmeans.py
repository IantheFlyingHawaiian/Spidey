# -*- coding: utf-8 -*-
#from sklearn.cluster import KMeans
#import numpy as np

#X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
#kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

#kmeans.predict([[0,0],[4,4]])
#kmeans.cluster_centers_
#print(kmeans)


import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# Incorrect number of clusters
#y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

#plt.subplot(221)
#plt.scatter(X[:, 0], X[:, 1], c=y_pred)
#plt.title("Incorrect Number of Blobs")

# Anisotropicly distributed data
#transformation = [[ 0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
#X_aniso = np.dot(X, transformation)
#y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_aniso)

#plt.subplot(222)
#plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
#plt.title("Anisotropicly Distributed Blobs")

# Different variance
X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)
#print (X_varied)                    
X_varied = np.array([[0, 0.0], [0, 0.0], [0, 0.0], [0, 0.70], [0, 0.46], [0, 0.00], [0, 0.0],[0, 0.08] ,[0, 0.21], [0, 0.21]])                                
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(X_varied)
print(kmeans)
kmeans.labels_
kmeans.predict([[0,0], [4,4]])
kmeans.cluster_centers_


y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X_varied)
print(y_pred)
plt.plot()
plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
#plt.title("Unequal Variance")
plt.title("Kmeans Clustering")

# Unevenly sized blobs
#X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
#y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_filtered)

#plt.subplot(224)
#plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
#plt.title("Unevenly Sized Blobs")

plt.show()