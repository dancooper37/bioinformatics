from toolkit.utilities import unpackFASTAToList

dataList = unpackFASTAToList("../compute_data/rosalind_lcsm.txt")
print(dataList)


def longestCommonSubSeq(dnaSeqList):
    subStr = ''
    if len(dnaSeqList) > 1 and len(dnaSeqList[0]) > 0:
        for i in range(len(dnaSeqList[0])):
            for j in range(len(dnaSeqList[0]) - i + 1):
                if j > len(subStr) and checkSubStr(dnaSeqList[0][i:i + j], dnaSeqList):
                    subStr = dnaSeqList[0][i:i + j]
    return subStr


def checkSubStr(searchStr, data):
    if len(data) < 1 and len(searchStr) < 1:
        return False
    for i in range(len(data)):
        if searchStr not in data[i]:
            return False
    return True


print(longestCommonSubSeq(dataList))

