class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        frontSum, backSum = [0], [0]
        
        for n in cardPoints:
            frontSum.append(frontSum[-1]+n)
        for n in cardPoints[::-1]:
            backSum.append(backSum[-1]+n)
            
        allCombinations = [frontSum[i] + backSum[k-i] for i in range(k+1)]
        
        return max(allCombinations)

#         frontSum, backSum = 0, 0
    
#         for i in range(k):
#             frontSum += cardPoints[i]
            
#         maxScore = frontSum
        
#         for i in range(k - 1,0,-1):
#             backSum += cardPoints[len(cardPoints) - (k - i)]
#             frontSum -= cardPoints[i]
#             currentScore = backSum + frontSum
#             maxScore = max(maxScore, currentScore)
            
            
#         return maxScore