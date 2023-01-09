class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        #purely iterative bottom-up DP Approach
        ans = []
        #for our table, we will keep track of power for each integer we did compute!(hashmap)
        hm = {}
        for i in range(lo, hi+1):
            cur = i
            #steps will tell how many times we have to transform to get integer i -> 1!
            steps = 0 
            #as long as we did not reduce curent integer to 1, we will do so iteratively!
            while cur != 1:
                #memo base case to break out of loop!
                if(cur in hm):
                    #to reduce given integer i, overall steps is (steps needed to reduce i to cur) + (steps needed to red. cur to 1, which is cached!)
                    steps += hm[cur]
                    break
                #even: halve it
                elif(cur % 2 == 0):
                    cur = cur // 2
                else:
                    cur = (cur * 3) + 1
                steps += 1
            #we will add to ans array a tuple element: (power, integer)
            ans.append((steps, i))
            hm[i] = steps
        #sort ans array in-place by ascending order of power as well as integer values itself!
        ans.sort(key = lambda x: (x[0], x[1]))
        #kth integer will be at index k-1 in ans!
        return ans[k-1][1]