def encode_OneShot(categoricalFeatures, numericalFeatures, data_list):
    categoriesDump =  [[data[feature] for data in data_list] for feature in categoricalFeatures]

    uniqueCategories = []

    for groups in categoriesDump:
        uniqueCategories += set(groups)

    numericalData = [] 
    for data in data_list:
        
        tempDict = {}
        
        for category in uniqueCategories:
            tempDict[category] = 0
        
        for feature in categoricalFeatures:
            tempDict[data[feature]] = 1

        for feature in numericalFeatures:
            tempDict[feature] = data[feature]
            
        numericalData.append(tempDict)

    return numericalData
