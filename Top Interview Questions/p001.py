# https://leetcode.com/problem-list/top-interview-questions/
# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):  # 1
            print(f"Step i:{i} ==> remaining: target({target}) - nums[{i}]({nums[i]})  ")
            remaining = target - nums[i]  # 2
            print(f"remaining: {remaining}")

            if remaining in seen:  # 3
                print(f"return {[i, seen[remaining]]}")
                return [i, seen[remaining]]  # 4
            else:
                seen[value] = i  # 5
                print(f"seen: {seen}")


s = Solution()
print(s.twoSum([11, 6, 15, 3], 9))
