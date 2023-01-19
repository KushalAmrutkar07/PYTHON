# Iris Dataset with K-mean algorithm using clustering

# importing the libraries

import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import pandas as pd

def MarvellousKMean():
    print("__________________________________________")

    # set three centers, the model should predict similar results
    
    center_1 = np.array([1,1])
    print(center_1)
    print("__________________________________________")
    center_2 = np.array([5,5])
    print(center_2)
    print("__________________________________________")
    center_3 = np.array([8,1])
    print(center_3)
    print("__________________________________________")

    # Generate random data and center it to the three centers

    data_1 = np.random.randn(7,2) + center_1
    print("Element of first cluster with size"+str(len(data_1)))
    print(data_1)
    print("__________________________________________")

    data_2 = np.random.randn(7,2) + center_2
    print("Element of Second cluster with size"+str(len(data_2)))
    print(data_2)
    print("__________________________________________")
    
    data_3 = np.random.randn(7,2) + center_3
    print("Element of Third cluster with size"+str(len(data_3)))
    print(data_3)
    print("__________________________________________")

    data = np.concatenate((data_1,data_2,data_3),axis = 0)
    print("Size of complete data set"+str(len(data)))
    print(data)
    print("__________________________________________")

    plt.scatter(data[:,0],data[:,1],s=7)
    plt.title('Marvellous Infosystem : Input Dataset')
    plt.show()
    print("__________________________________________")
    
    # Number of Clusters
    k = 3

    n = data.shape[0]
    print("Total number of elements are",n)
    print("__________________________________________")
    
    # Number of Features in data

    c = data.shape[1]
    print("Total number of feature are",c)
    print("__________________________________________")

    # Generate random centers, here we use sigma and mean to ensure it represent the whole data

    mean = np.mean(data,axis = 0)
    print("Value of mean",mean)
    print("__________________________________________")

    # Calculate standard deviation

    std = np.std(data , axis = 0)
    print("Value of std",std)
    print("__________________________________________")

    centers = np.random.randn(k,c)*std + mean
    print("Random points are",centers)
    print("__________________________________________")

    # Plot the data and the centers generated as random
    plt.scatter(data[:,0],data[:,1], c ='r',s = 7)
    plt.scatter(centers[:,0],centers[:,1],marker = '*',c ='g',s = 150)
    plt.title('Marvellous Infossystems : Input dataset with random centroid *')
    plt.show()
    print("__________________________________________")

    centers_old = np.zeros(centers.shape) # to store old centers
    centers_new = deepcopy(centers) # store new centers

    print("Values of old centroids")
    print(centers_old)
    print("__________________________________________")

    print("Values of new centroids")
    print(centers_new)
    print("__________________________________________")

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n,k))

    print("Initial distance are")
    print(distances)
    print("__________________________________________")

    error = np.linalg.norm(centers_new - centers_old)
    print("value of error is",error)

    # When after an update the estimate of that center stays the same,exit loop

    while error != 0:
        print("Value of error is ",error)

    # Measure the distance to every center
        print("Measure the distance to every center")
        for i in range(k):

            print("Iteration number",i)
            distances[:,i] = np.linalg.norm(data - centers[i],axis = 1)

    # Assign all training data to closest center
        clusters = np.argmin(distances,axis = 1)    
    
        centers_old = deepcopy(centers_new)

    # Calculate mean for every cluster and update the center 

        for i in range(k):
            centers_new[i] = np.mean(data[clusters == i],axis = 0)
        error = np.linalg.norm(centers_new - centers_old)

    # end of while
    centers_new

    # Plot the data and the centers genereated as random
    plt.scatter(data[:,0],data[:,1],s = 7)
    plt.scatter(centers_new[:,0],centers_new[:,1],marker = '*',c ='g',s = 150)
    plt.title('Marvellous Infossystems : Final data with  centroid ')
    plt.show()         
    
def main():
    print("-------Marvellous Infosystem by Piyush Khairnar-------")

    print("Unsupervised ML")

    print("Clustering using K Mean Algorithm ")

    MarvellousKMean()


if __name__ =="__main__":
    main()    