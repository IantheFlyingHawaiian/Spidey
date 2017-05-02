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

class KmeansTest:
    
    def __init__(self):
        self.X_Varied = []
        
        plt.figure(figsize=(12, 12))
        n_samples = 1500
        random_state = 170
        
        X, y = make_blobs(n_samples=n_samples, random_state=random_state)
                        
        X_varied = np.array([[0, 0.0], [0, 0.0], [0, 0.0], [0, 0.70], [0, 0.46], [0, 0.00], [0, 0.0],[0, 0.08] ,[0, 0.21], [0, 0.21]])                                
        kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
        print '----------------------X VARIED------------------'
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
        
        #plt.show()
        
        
        
    def setNpArray(self, frequencies):
        self.X_varied = np.array(frequencies)
        print np.array(frequencies)
        print self.X_Varied
        return self.X_Varied
        
    def calc(self):
        print '----------------------X VARIED------------------'
        '''print self.X_Varied
        plt.figure(figsize=(12, 12))
        n_samples = 1500
        random_state = 170
        X, y = make_blobs(n_samples=n_samples, random_state=random_state)
                                                 
        kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
        print(self.X_varied)
        print(kmeans)
        kmeans.labels_
        kmeans.predict([[0,0], [4,4]])
        kmeans.cluster_centers_
        
        #X_Varied = np.array(self.X_Varied)
        print '---------------------- X VARIED --------------------'
        print(self.X_varied)
        y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(self.X_Varied)
        
        print(y_pred)
        plt.plot()
        plt.scatter(self.X_varied[:, 0], self.X_varied[:, 1], c=y_pred)
        #plt.title("Unequal Variance")
        plt.title("Kmeans Clustering")
        plt.show()'''
        
        plt.figure(figsize=(12, 12))
        n_samples = 1500
        random_state = 170
        
        X, y = make_blobs(n_samples=n_samples, random_state=random_state)
                        
        #X_varied = np.array([[0, 0.0], [0, 0.0], [0, 0.0], [0, 0.70], [0, 0.46], [0, 0.00], [0, 0.0],[0, 0.08] ,[0, 0.21], [0, 0.21]]) 
        X_varied  = self.X_Varied
        kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
        print '----------------------X VARIED------------------'
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
        
        plt.show()
        
k = KmeansTest()
a = [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0 , 0.90], [0.0, 0.46], [0.0, 0.00], [0.0, 0.0],[0.0, 0.08] ,[0.0, 0.21], [0.0, 0.21]
print '------------------------- a -------------------------------'
print a
X_varied = np.array(a)
print '------------------------- x after setNpArray -------------------------------'
print X_varied
k.X_Varied = X_varied
print '-------------------------- k CALC -------------------------'
k.calc()