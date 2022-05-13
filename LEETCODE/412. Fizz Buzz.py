# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            updater = ""
            if i % 3 == 0:
                updater += "Fizz"
            if i % 5 == 0:
                updater += "Buzz"
            if updater == "":
                updater = str(i)
            answer.append(updater)
        return answer


example = Solution()
print(example.fizzBuzz(n=8))
