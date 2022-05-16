# https://leetcode.com/problems/check-if-n-and-its-double-exist/


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] * 2 in arr[:i] + arr[i + 1:]:
                return True
        return False


obj1 = Solution()
print(obj1.checkIfExist(arr=[10, 2, 6, 3]))
