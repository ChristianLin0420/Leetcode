class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def convert_to_index(word):
            alphabet_indices = {}
            converted_word = []
            current_count = 0

            for w in word:
                if w not in alphabet_indices:
                    alphabet_indices[w] = current_count
                    current_count += 1
                converted_word.append(alphabet_indices[w])

            return converted_word
        
        converted_pattern = convert_to_index(pattern)

        return [word for word in words if convert_to_index(word) == converted_pattern]