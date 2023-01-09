class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        hash_map = {}
        for i, char in enumerate(source):
            if char not in hash_map:
                hash_map[char] = [i]
            else:
                hash_map[char].append(i)

        print(hash_map)
        
        def binary_search(char, low, high, target):
            if low > high:
                return low
            mid = (low + high)//2
            if target >= hash_map[char][mid]:
                return binary_search(char, mid+1, high, target)
            else:
                return binary_search(char, low, mid-1, target)
            
        curr_pos = -1
        ans, i = 1, 0
        while i < len(target):
            if target[i] not in hash_map:
                return -1
            idx = binary_search(target[i], 0, len(hash_map[target[i]])-1, curr_pos)
            if 0 <= idx < len(hash_map[target[i]]) and hash_map[target[i]][idx] > curr_pos:
                curr_pos = hash_map[target[i]][idx]
                i+=1
            else:
                print('inside else')
                ans+=1
                curr_pos = -1
        return ans