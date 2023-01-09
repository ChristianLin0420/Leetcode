class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = [1] * 5

        for j in range(n):
            for i in range(5):
                vowels[i] = sum(vowels[i:])
                
        return vowels[0]