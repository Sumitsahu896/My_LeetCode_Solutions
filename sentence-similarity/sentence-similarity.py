class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        for i in range(len(sentence1)):
            combo1 = [sentence1[i], sentence2[i]]
            combo2 = [sentence2[i], sentence1[i]]
            
            if not (sentence1[i] == sentence2[i] or combo1 in similarPairs or combo2 in similarPairs):
                return False
            
        return True