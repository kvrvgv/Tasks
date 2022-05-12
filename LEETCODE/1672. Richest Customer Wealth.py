# https://leetcode.com/problems/richest-customer-wealth/


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])
        return max(accounts)


example = Solution()
print(example.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
