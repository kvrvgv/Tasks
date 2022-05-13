# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            count += 1
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
        return count
        # не делать по очевидному. уверен это как то через div или mod делать чтоб упростить вычисления


example = Solution()
print(example.numberOfSteps(num=8))
