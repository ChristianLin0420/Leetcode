class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m=0 #max length of window
        c=0 #count of 0 found
        i=0 #initial window index
        j=0 #window's end's index

        while j<len(nums):
            if nums[j]==0: #count if 0 found
                c+=1

            if c==k: #if 0's equal to k in window then store the max
                m=max(m,j-i+1) #j-i+1 <- valid window length
            elif c>k: #if somehow 0's > k in window then move the window one step forward
                if nums[i]==0: #on moving the index i, its necessaray to check if that's 0 or not
                    c-=1 #decrement the count if it is
                i+=1 #and move the index

            j+=1  #increment everytime, its making the window

        if c<k: #if 0's count < k  in window, return whole nums length -> forms valid substring
            return len(nums)
            
        #else return max window length
        return m