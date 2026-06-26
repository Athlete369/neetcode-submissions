class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n

        i = 1
        while i < n:
            left_product[i] = left_product[i - 1] * nums[i - 1]
            i +=1

        i = n - 2
        while i > -1:
            right_product[i] = right_product[i + 1] * nums[i + 1]
            i -=1

        for i in range(0, n):
            nums[i] = left_product[i] * right_product[i]
        return nums