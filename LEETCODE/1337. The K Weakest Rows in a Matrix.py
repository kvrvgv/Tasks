# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        for i in range(len(mat)):
            mat[i] = sum(mat[i])
        answer = []
        for i in sorted(mat):
            index = mat.index(i)
            answer.append(index)
            mat[index] = str(i)
        return answer[:k]


example = Solution()
print(example.kWeakestRows(
    mat=[[1, 1, 0, 0, 0],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1]],
    k=3))
