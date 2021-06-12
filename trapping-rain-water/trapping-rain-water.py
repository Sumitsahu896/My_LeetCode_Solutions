class Solution:
    def trap(self, height: List[int]) -> int:
        # By two pointers
        # areas = 0
        # max_l = max_r = 0
        # l = 0
        # r = len(height)-1
        # while l < r:
        #     if height[l] < height[r]:
        #         if height[l] > max_l:
        #             max_l = height[l]
        #         else:
        #             areas += max_l - height[l]
        #         l +=1
        #     else:
        #         if height[r] > max_r:
        #             max_r = height[r]
        #         else:
        #             areas += max_r - height[r]
        #         r -=1
        # return areas
        
        # By dynamic Programming - Table making
        
        n = len(height)
        ans = 0
        if n == 0:
            return ans
        
        l_max, r_max = [0]*n, [0]*n
        
        max_height = height[0]
        
        for i in range(1, n):
            l_max[i] = max_height
            max_height = max(max_height, height[i])
            
        max_height = height[n - 1]
        
        for i in range(n - 2, -1, -1):
            r_max[i] = max_height
            max_height = max(max_height, height[i]) 
            
        
        for i in range(n):
            area = min(l_max[i], r_max[i]) - height[i]
            ans = ans + (area if area > 0 else 0)
            
        return ans