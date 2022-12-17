from controllers.conversion import gettingCNF

triangularTable = {}
# g = None
# previousNode = None

def is_accepted(inputString):
    triangularTable.clear()
    Rules = gettingCNF()
    temp = inputString.lower().split(" ")
    inputString = temp
    for i in range(1,len(inputString)+1):
        for j in range(i, len(inputString)+1):
            triangularTable[(i,j)] = []
    for i in reversed(range(1, len(inputString)+1)):
        for j in range(1, i+1):
            if (j == j + len(inputString) - i):
                tempList = []
                for key, value in Rules.items():
                    for val in value:
                        if (val == inputString[j-1] and key not in tempList):
                            tempList.append(key)
                triangularTable[(j, j + len(inputString) - i)] = tempList
            else:
                tempList = []
                resultList = []
                for k in range(len(inputString) - i):
                    first = triangularTable[(j,j+k)]
                    second = triangularTable[(j+k+1,j+len(inputString) - i)]
                    for fi in first:
                        for se in second:
                            if (fi + " " + se not in tempList):
                                tempList.append(fi + " " + se)
                for key, value in Rules.items():
                    for val in value:
                        if (val in tempList and key not in resultList):
                            resultList.append(key)
                triangularTable[(j,j+len(inputString) - i)] = resultList
    if "K" in triangularTable[(1, len(inputString))]:
        return True
    else:
        return False

print(is_accepted("saya sedang bermain di kota"))