### Jingchao Yang
# Feb. 26 2018
# Data Mining 787
# Some credit goes to https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator

# function for data loading
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)[1:]  # skip header
        print(dataset)
        for x in range(len(dataset)):
            # convert all data to float
            for y in range(len(dataset[x])):
                dataset[x][y] = float(dataset[x][y])
            # split the data to 10 groups, 9 are using for training
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

# using euclidean distance for searching knn
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

# filter to select neighbors
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1 # which is 2, we have 2 columns for classification in the cvs
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# majority of the neighbor attribute goes to the testing instance
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    # sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


# def getAccuracy(testSet, predictions):
#     correct = 0
#     for x in range(len(testSet)):
#         if testSet[x][-1] == predictions[x]:
#             correct += 1
#     return (correct / float(len(testSet))) * 100.0

# get the overall accuracy, and the confusion matrix
# ----------------
# |    1    0    |
# |1   TP   FN   |
# |0   FP   TN   |
# ----------------
#
def getAccuracy1(testSet, predictions):
    correct = 0
    TP, TN, FP, FN = 0,0,0,0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
            if testSet[x][-1] == 1.0:
                TP +=1
            if testSet[x][-1] == 0.0:
                TN +=1
        if testSet[x][-1] != predictions[x]:
            if testSet[x][-1] == 1.0:
                FP +=1
            if testSet[x][-1] == 0.0:
                FN +=1
    Precision = TP/(TP+FP)
    Recall = TP/(TP+FN)
    return (correct / float(len(testSet))) * 100.0 , Precision * 100, Recall * 100

def main():
    # prepare data
    trainingSet = []
    testSet = []
    split = 0.9
    loadDataset('Data/filteredLocation.csv', split, trainingSet, testSet)
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    # generate predictions
    predictions = []
    k = 8
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy, precision, recall = getAccuracy1(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    print('Precision: ' + repr(precision) + '%')
    print('Recall: ' + repr(recall) + '%')
    print('f-score: ' + repr((2*precision*recall)/(precision+recall)) + '%')

main()
