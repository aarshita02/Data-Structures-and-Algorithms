class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r*c:
            return mat
        ans = [[]]
        for i in range(0,len(mat)):
            for j in range(0, len(mat[0])):
                k = mat[i][j]
                if len(ans[-1]) < c:
                    ans[-1].append(k)
                else:
                    ans.append([k])
        return ans
"""
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

Input: mat = [[1,2],[3,4]], r = 1, c = 4

Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4

Output: [[1,2],[3,4]]
"""
