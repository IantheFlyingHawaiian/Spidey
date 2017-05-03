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
        #print '----------------------X VARIED------------------'
        #print(X_varied)
        #print(kmeans)
        kmeans.labels_
        kmeans.predict([[0,0], [4,4]])
        kmeans.cluster_centers_
        
        y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X_varied)
        #print(y_pred)
        plt.plot()
        plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
        #plt.title("Unequal Variance")
        plt.title("Kmeans Clustering")
        
        #plt.show()
        
        
        
    def setNpArray(self, frequencies):
        self.X_Varied = np.array(frequencies)
        print '----------------------set NP Array frequencies------------------'
        print np.array(frequencies)
        print '----------------------set NP Array X_Varied------------------'
        print self.X_Varied
        return self.X_Varied
        
    def reverseYPred(self, y_pred2):
        count = 0;
        y_pred3 = y_pred2.copy()
        for i in y_pred3:
            if i == 0:
                print 'REVERSE'
                print  y_pred3[count]
                print y_pred3
                y_pred3[count] = 1
                y_pred3 = y_pred3
                print  y_pred3[count]
            else:
                print 'REVERSE'
                print  y_pred3[count]
                print y_pred3
                y_pred3[count]= 0
                y_pred3 = y_pred3
                print  y_pred3[count]
                print  y_pred3
            count = count + 1
        print '------------------------Y_Pred----------------------'
        print y_pred3
        print y_pred2
        return y_pred3
    
    def cleanYPred(self, y_pred2):
        print '--------------clean Y Pred ----------------------'
        count = 0
        reverse = False
        for i in y_pred2:
            print i
            if i == 0:
                #REVERSE THE Y_PRED IF THE HIGH VALUES ARE SET AS ZERO
                print 'REVERSE THE Y_PRED IF THE HIGH VALUES ARE SET AS ZERO'
                print self.X_Varied[count][1]
                if (self.X_Varied[count][1] > 0 and i == 0):
                    print '--------------- reverse y_pred--------------'
                    print self.X_Varied[count][1]
                    print count
                    reverse = True
            count = count + 1
            if reverse == True:
                y_pred3 = self.reverseYPred(y_pred2)
                print 'After reverse'
                print y_pred3
                return y_pred3
        
        
        return y_pred2
        
        
    def calc(self):
        #print '----------------------X VARIED------------------'
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
        
        y_pred = self.cleanYPred(y_pred)
        
        return y_pred
        
#k = KmeansTest()
#a = [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0 , 0.90], [0.0, 0.46], [0.0, 0.00], [0.0, 0.0],[0.0, 0.08] ,[0.0, 0.21], [0.0, 0.21]
#print '------------------------- a -------------------------------'
#print a
#X_varied = np.array(a)
#print '------------------------- x after setNpArray -------------------------------'
#print X_varied
#k.X_Varied = X_varied
#print '-------------------------- k CALC -------------------------'
#k.calc() 