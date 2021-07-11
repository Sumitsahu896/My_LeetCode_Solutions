# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def getMatch(self,word1, word2):
        count = 0
        for x,y in zip(word1,word2):
            if x == y:
                count +=1
        return count
                
        
    def findSecretWord(self, wordList, master):
        i = 0
        matches = 0
        while i < 10 and matches != 6:
            index = random.randint(0,len(wordList)-1)
            word = wordList[index]
            matches = master.guess(word)
            
            candidates = []
            for w in wordList:
                if matches == self.getMatch(word, w):
                    candidates.append(w)
            wordList = candidates
            
        return word