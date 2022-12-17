MapVariableProduction = {}

def removeUnitProduction(keyList):
    for key, value in MapVariableProduction.items():
        if key in keyList:
            tempList = []
            for production in value:
                if len(production.split(" ")) == 2:
                    tempList.append(production)
                else:
                    for i in MapVariableProduction[production]:
                        if i not in tempList:
                            tempList.append(i)
            MapVariableProduction[key] = tempList

def gettingCNF():
    MapVariableProduction.clear()
    f = open("./variableList.txt", "r", encoding="utf-8")
    
    for lines in f:
        line = lines.splitlines()
        line = line[0].split(" -> ")
        lhs = line[0]
        rhs = line[1].split(" | ")
        if lhs in MapVariableProduction.keys():
            MapVariableProduction[lhs].extend(rhs)
        else:
            MapVariableProduction[lhs] = rhs
    f.close()
    
    
    for key, value in MapVariableProduction.items():
        if key == "PropNoun":
            temp = []
            for val in value:
                if val not in temp:
                    temp.append(val.lower())
            MapVariableProduction[key] = temp
            
    frasa = ["NumP", "AdvP", "AdjP", "PP", "NP", "VP"]
    notasi = ["S", "P", "O", "Pel", "Ket"]
    
    removeUnitProduction(frasa)
    removeUnitProduction(notasi)
    
    temp = []
    tempMap = {}
    
    i = 1
    for key, value in MapVariableProduction.items():
        if key == "K":
            for val in value:
                if len(val.split(" ")) > 2:
                    temp = val.split(" ")
                    while len(temp) > 2:
                        check = temp[0] + " " + temp[1]
                        isFound = False
                        for k, v in tempMap.items():
                            if check == v:
                                isFound = True
                                temp.pop(0)
                                temp.pop(0)
                                temp.insert(0, k)
                                break
                        if not isFound:
                            tempMap["K" + str(i)] = check
                            temp.pop(0)
                            temp.pop(0)
                            temp.insert(0, "K" + str(i))
                            i += 1
                    temp.append(" ".join(temp))
                else:
                    temp.append(val)
            MapVariableProduction[key] = temp
    for key, value in tempMap.items():
        MapVariableProduction[key] = [value]
        
    return MapVariableProduction
