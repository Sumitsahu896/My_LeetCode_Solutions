class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # h = {}
        # for i, num in enumerate(nums):
        #     n = target - num
        #     if n not in h:
        #         h[num] = i
        #     else:
        #         return [h[n], i]
        
        hash_map = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference not in hash_map:
                hash_map[num] = index
            else:
                return [hash_map[difference], index]