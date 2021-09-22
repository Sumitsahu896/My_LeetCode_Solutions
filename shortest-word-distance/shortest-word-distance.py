class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dist = len(wordsDict)
        curr_word, idx = None, 0
        for i, w in enumerate(wordsDict):
            if w not in (word1, word2): continue
            if curr_word and w != curr_word:
                min_dist = min(min_dist, i - idx)
            curr_word, idx = w, i
        return min_dist