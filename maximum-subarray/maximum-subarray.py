class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
# Brute Force
#         max_subarray = -math.inf
#         for i in range(len(nums)):
#             current_subarray = 0
#             for j in range(i, len(nums)):
#                 current_subarray += nums[j]
#                 max_subarray = max(current_subarray, max_subarray)
            
#         return max_subarray

# Dynamic Programming

# Since we have to find the max or the min we will consider doing this with dynamic programming

    def maxSubArray(self, nums: List[int]) -> int:
        # Initializing current and max subarray
        current_subarray = max_subarray = nums[0]
        
        # Start interating from the 2nd element 
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
            
        return max_subarray