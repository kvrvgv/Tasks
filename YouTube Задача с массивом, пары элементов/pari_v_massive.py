# Найти элемент без пары, такой элемент всего 1


import json


file = open("input.txt", "r")
INPUT = json.loads(file.read())
file.close()

while INPUT:
    iter = INPUT[0]
    INPUT.remove(iter)
    try:
        INPUT.remove(iter)
    except:
        print(iter)


# то же самое только нашел эту задачу в LeetCode
# https://leetcode.com/problems/single-number/submissions/
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        while nums:
            iter = nums[0]
            nums.remove(iter)
            try:
                nums.remove(iter)
            except:
                return iter


obj1 = Solution()
print(obj1.singleNumber(nums=[2, 2, 1]))
