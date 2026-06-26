class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i in range(0, len(nums)):
            t = target - nums[i]
            if t in hash_map:
                return [hash_map[t], i]
            hash_map[nums[i]] = i
        return []
        