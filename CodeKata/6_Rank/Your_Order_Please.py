def order(sentence):
    
    if sentence != "":
    
        sentenceList = sentence.split(" ")
        resultString = None
        resultDict = {}
        resultList = []

        for i in sentenceList:
            
            for j in i:
                
                if j.isdigit():
                    resultDict.update({int(j):i})

        # resultString = ''.join(i for i in resultDict.values())

        for i in range(len(sentenceList)):
            a = i+1
            resultList.append(resultDict[a])
            
        resultString = ' '.join(i for i in resultList)
        
        return resultString
    else:
        return sentence