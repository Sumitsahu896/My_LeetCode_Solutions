class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list_set = set(nums)
        
        answer = []
        
        for num in range(1, len(nums) + 1):
            if num not in list_set:
                answer.append(num)
                
        return answer

        