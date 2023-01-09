class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        theDict = defaultdict(int) #Introduce the dictionary
        
        for i in nums:
            if i not in theDict:
                theDict[i] = 1 # add 1 as the value for an element encountered for the first time
            elif i in theDict:
                theDict[i] = theDict[i] + 1 # add 1 to the value for every time we encounter the same element

        sortedNos = sorted(theDict.items(), key=lambda x:x[1]) # sort the elements of the dictionary w.r.t. values (ascending) and create a list
        finalList = [] 
        for i in sortedNos[len(sortedNos) - k:]: # since the the list is ascending, we want the "keys" of the last k elements
            finalList.append(i[0]) # the "keys"
        return(finalList)