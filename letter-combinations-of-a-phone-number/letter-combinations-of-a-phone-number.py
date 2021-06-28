class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create a hashset for all the numbers from 2 to 9 so that it will be easy to get the values from it
        # in O(n) time. A fter taht we can iterate through the digits string one bby one and do the permutation 
        # of all the possible combinations.
        
        answer = []
        
        if len(digits) == 0:
            return answer
        
        letters = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        if len(digits) == 1:
            return list(letters[digits[0]])
        
        prev = self.letterCombinations(digits[:-1])
        additional = letters[digits[-1]]
        
        return [p + a for p in prev for a in additional]
        