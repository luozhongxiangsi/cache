import sys, os
import numpy as np
import operator


class KNN_test():
    def __init__(self, absPath):
        self.absPath = absPath

    def file2matrix(self, filename):
        fr = open(self.absPath+'/'+filename)
        arrayOLines = fr.readlines()
        numberOfLines = len(arrayOLines)
        returnMat = np.zeros((numberOfLines, 3))
        classLabelVector = []
        index = 0
        for line in arrayOLines:
            line = line.strip()
            listForomLine = line.split('\t')
            returnMat[index, :] = listForomLine[-1]
            classLabelVector.append(int(listForomLine[-1]))
            index += 1
        return returnMat, classLabelVector