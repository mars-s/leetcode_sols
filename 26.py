from operator import indexOf
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        index = 0
        for x in range(len(nums)):
            if nums[x] not in s:
                nums[index] = nums[x]
                index += 1
            s.add(nums[x])
        return index
                