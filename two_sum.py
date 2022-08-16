from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if hash_map.get(target - nums[i]) is not None:
                return hash_map.get(target - nums[i]), i
            else:
                hash_map[nums[i]] = i