class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i<j:
            sum_two = numbers[i] + numbers[j]
            if sum_two == target:
                return [i+1, j+1]
            elif sum_two > target:
                j -=1
            else:
                i +=1
        return []