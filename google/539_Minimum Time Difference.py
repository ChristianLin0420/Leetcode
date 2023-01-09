class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr=[]
        ovtm=24*60

        for i in range(0,len(timePoints)):
            th=int(timePoints[i][0:2])*60
            tm=int(timePoints[i][3:5])
            arr.append(th+tm) 

        arr.sort()
        mina=ovtm-arr[-1]+arr[0]

        for i in range(1,len(arr)):
            mina=min(mina,arr[i]-arr[i-1])
            
        return mina