# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            nehvatka = target - i
            i_index = nums.index(i)
            without_i = (nums[:i_index] + [None] + nums[i_index + 1:])
            if nehvatka in without_i:
                return [i_index, without_i.index(nehvatka)]


example = Solution()
print(example.twoSum(nums=[3, 2, 4], target=6))
