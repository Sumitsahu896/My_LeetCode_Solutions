class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Start form a table say it is only 3 in the array
        # We store the maximum amount of points i can get or store in the value
        # Which is 3
        
        # Then we increase the number to 3 and 4 and figure out which is the max point
        # value, which is either deleting 3 and then deleting 4 to get total points as 4
        
        # Now we can add another number as 2 and then think of which number should be added
        # or deleted so we can do is we can delete 3 and then delete 2 to get 3 + 4 which will 
        # be 7 points
        
        if not nums:
            return 0
        
        freq = [0] * (max(nums) + 1)
        for n in nums:
            freq[n] += n
            
        dp = [0] * len(freq)
        dp[1] = freq[1]
        
        for i in range(2 ,  len(freq)):
            dp[i] = max(freq[i] + dp[i - 2], dp[i - 1])
            
        return dp[len(freq) - 1]