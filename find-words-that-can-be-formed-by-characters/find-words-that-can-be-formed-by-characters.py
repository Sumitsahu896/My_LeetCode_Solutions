class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        total_sum, chars_counter = 0, collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                total_sum += len(word)
        return total_sum
        