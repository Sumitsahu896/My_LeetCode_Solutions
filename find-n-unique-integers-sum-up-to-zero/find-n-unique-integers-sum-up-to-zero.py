class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        # if not n:
        #     return answer
        
        for i in range(1, n//2 + 1):
            answer.append(i)
            answer.append(i * -1)
            
        if n%2 == 1:
            answer.append(0)
            
        return answer