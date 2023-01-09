class Solution:
    def numSplits(self, s: str) -> int:
        output = 0

        # Use two dicts to count occurances of characters on the left and right side of the split
        #   Initially, the left is empty and the right contains all the letters
        dleft = {}
        dright = {}

        for char in s:
            dright[char] = dright.get(char, 0) + 1

        # Then loop through each character in s, adding its occurance to the left dictionary and removing it
        #   from the right. Then compare the length of the sets of keys of the dictionary (which counts distinct
        #   characters) and increment `output` if they are equal.
        for i in range(len(s)):
            dleft[s[i]] = dleft.get(s[i], 0) + 1
            
            if dright[s[i]] == 1: 
                del dright[s[i]]
            else: 
                dright[s[i]] = dright.get(s[i]) - 1

            if len(dleft.keys()) == len(dright.keys()):
                output += 1

        return output