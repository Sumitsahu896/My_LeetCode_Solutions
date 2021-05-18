class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array
        length = len(nums)
        
        # The left and the right array with the answer
        answer = [0]*length
        
        # The left array holds the product of all the elements to the left.
        # Since there is no elements in the left of the first array, hence
        answer[0] = 1
        
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
            
        # The right array holds the product of all the elements to the right.
        # Since there is no elementsin the right of the last element, hence
        R= 1
        
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
            
        return answer
    