class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority_count = len(nums)//2
        # for num in nums:
        #     count = sum(1 for elem in nums if elem == num)
        #     if count > majority_count:
        #         return num
        
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
        
        # nums.sort()
        # max_number_index = len(nums)//2
        # return nums[max_number_index]
        
        # Boyer Moore Algorithm
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate