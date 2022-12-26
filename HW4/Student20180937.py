import numpy as np
import operator
import os
import sys

tmp = sys.argv

currentpath = os.getcwd()
path_test = "./" + tmp[len(tmp)-1]
path_training = "./" + tmp[len(tmp)-2]
file_lst = os.listdir(path_training)
file_lst1 = os.listdir(path_test)
def createDataSet():
    group = np.array([])
    labels = []
    for f in file_lst:
        labels.append(f[0])
        f = path_training + "/" + f
        f_read = open(f, "rt")
        ap_list = []
        for ln in f_read:
            f_list = list(ln)
            f_list = f_list[:-1]
            f_list = list(map(int, f_list))
            ap_list = ap_list + f_list
        ap = np.array(ap_list)
        group = np.append(group, np.array(ap_list), axis= 0)
    group = group.reshape(-1, len(ap))
    return group, labels

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

if __name__ == "__main__":
    group, labels = createDataSet()
    for k in range(1, 21):
        corr = 0
        for f in file_lst1:
            lab = f[0]
            f = path_test + "/" + f
            f_test = open(f, "rt")
            ap_list = list()
            for ln in f_test:
                f_list = list(ln)
                f_list = f_list[:-1]
                f_list = list(map(int, f_list))
                ap_list = ap_list + f_list
            if(int(classify0(ap_list, group, labels, k)) == int(lab)):
                corr = corr + 1
        print(100 - int(corr/len(file_lst1)*100))
