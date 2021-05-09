class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # n = len(nums)
        # result = [0] * n
        # left = 0
        # right = n - 1
        # for i in range(n - 1, -1, -1):
        #     if abs(nums[left]) < abs(nums[right]):
        #         square = nums[right]
        #         right -= 1
        #     else:
        #         square = nums[left]
        #         left += 1
        #     result[i] = square * square
        # return result
        
        return_array = [0] * len(A)
        write_pointer = len(A) - 1
        left_read_pointer = 0
        right_read_pointer = len(A) - 1
        left_square = A[left_read_pointer] ** 2
        right_square = A[right_read_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                return_array[write_pointer] = left_square
                left_read_pointer += 1
                left_square = A[left_read_pointer] ** 2
            else:
                return_array[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = A[right_read_pointer] ** 2
            write_pointer -= 1
        return return_array