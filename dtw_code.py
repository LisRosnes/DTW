import math
import numpy as np

#calculate euclidean distance
def euclidean(A, B):
    d = []
    for i in range(len(A)):
        d.append(abs(A[i] - B[i]))

    return sum(d)


#DTW: create distance matrix, fill out first column and first row
#Create distance matrix dist(i, j) = abs(A[i] - B[j])
def distanceMatrix(A, B):
    n, m = len(A), len(B)
    dist = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            dist[i,j] = abs(A[i] - B[j])

    return dist

#cost matrix
def dtw(dist):
    #initialize cost matrix
    n, m = dist.shape   
    cost = np.zeros((n+1, m+1))
    cost[0,0] = dist[0,0] #starting point
    for i in range(1, n+1):
        cost[i, 0] = np.inf
    for j in range(1, m+1):
        cost[0,i] = np.inf

    #find cost and fill in matrix
    for i in range(n):
        for j in range(m):
            minValue =  min(cost[i, j], cost[i, j+1], cost[i+1, j])
            costValue = dist[i, j] + minValue
            cost[i+1, j+1] = costValue

    return (cost[n - 1, m - 1])

def dtwDist(path, costMatrix):
    d = 0
    for a, b in path:
        d += abs(costMatrix[a] - costMatrix[b])

    return d

A = [3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 2, 3, 2, 1]
B = [1, 2, 3, 2, 1, 3, 4, 2, 1, 2, 1, 3, 2, 1]

euclideanDist = euclidean(A, B)
distMatrix = distanceMatrix(A, B)
costValueDTW = dtw(distMatrix)
print(f"The euclidean Distance: {euclideanDist}")
print(f"DTW: {costValueDTW}")
